
# Instalar panda	            python -m pip install pandas
# Instalar una barra progresiva	python -m pip install tqdm
# Instalar parquet	            python.exe -m pip install pyarrow
# Usar Markdown                 python -m pip install tabulate 


# En la limpieza podría comprobar si el presup_df está vacío y entonces no hacer nada ya que se supone que se ha hecho
# Pero en este caso volvemos hacer la limpieza
#if presup_df.empty:
    #print("No hay presupuesto nuevo que limpiar, se salta la fase SILVER de presupuesto.")
#else:

"""
Pipeline finanzas: presupuesto vs gasto (ETL ligero)
Bronce → Plata → Oro → Quarantine → Reporte
"""

import hashlib
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd
import unicodedata

# ---------------------------------------------------------------------
# RUTAS BASE
# ---------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "data" / "drops"
QUARANTINE = ROOT / "data" / "quarantine"
STORAGE = ROOT / "data" / "storage"

BRONZE = STORAGE / "bronze"
SILVER = STORAGE / "silver"
GOLD = STORAGE / "gold"

OUT = ROOT / "output"
SQL = ROOT / "sql"

for folder in [BRONZE, SILVER, GOLD, QUARANTINE, OUT, SQL]:
    folder.mkdir(parents=True, exist_ok=True)

SQLITE_PATH = SQL / "finanzas.db"

# límites de control de calidad
MAX_PRESUPUESTO = 1_000_000   # tope máximo para los presupuestos
MAX_IMPORTE_GASTO = 300_000   # tope máximo para los gastos

AREAS = ["RRHH", "IT", "Marketing", "Ventas", "Operaciones", "Calidad", "Contabilidad", "Direccion", "Administracion", "I+D"]
PARTIDAS = ["Personal", "Software", "Hardware", "Formacion", "Viajes", "Publicidad", "Suministros", "Alquileres", "Mantenimiento", "Seguros"]

# ---------------------------------------------------------------------
# UTILIDADES
# ---------------------------------------------------------------------

# Pasar a minúsculas
# Quitar tildes y caracteres especiales
# Eliminar espacios extra
def normalize_text(text):
    if pd.isna(text) or not str(text).strip():
        return None
    text = str(text).strip().lower()
    text = ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if not unicodedata.combining(c)
    )
    return text


def create_file_batch_id(path: Path) -> str:
    stats = path.stat()
    absolute_path = path.resolve(strict=True)
    parts = [
        absolute_path.as_posix(),
        str(stats.st_size),
        str(stats.st_mtime_ns),
    ]
    data = "|".join(parts).encode("utf-8")
    hasher = hashlib.md5()
    hasher.update(data)
    return hasher.hexdigest()

# 2. Normalizamos las listas AREA y PARTIDAS
AREAS_NORM = {normalize_text(a) for a in AREAS}
PARTIDAS_NORM = {normalize_text(p) for p in PARTIDAS}

# -----------------------------------------------------
# 1. INGESTIÓN (BRONZE)
# -----------------------------------------------------
print("-" * 70)
print("RETO 1: INGESTIÓN - BRONZE (RAW)")
print("-" * 70)

presupuesto_csv = DATA / "presupuesto.csv"
gastos_csv = DATA / "gastos.csv"
# Listas vacías donde metemos los df nuevos
raw_gastos, raw_presup = [], []
# Marca de tiempo
utcnow = datetime.now(timezone.utc).isoformat()

# lleva el registro de qué ficheros se cargaron
manifest_path = BRONZE / "ingest_manifest.parquet"
# cargar manifest si existe
if manifest_path.exists():
    manifest = pd.read_parquet(manifest_path)
else:
    manifest = pd.DataFrame(columns=["_batch_id", "_source_file", "_ingest_ts", "n_rows"])

# ----- GASTOS -----
# 1. Comprobar si el archivo existe.
# 2. Calcular un batch_id basado en ruta, tamaño y mtime
# 3. Revisamos en el manifest si ese batch_id existe.
# 4. En caso de que no exista leemos el csv y le añadimos las columnas archivo, timestamp y batch
# 5. Metemos el df completo en la lista raw_gastos
# 6. Rellenamos el archivo manifest
# 7. Confirmamos que hay una ingesta nueva
ingesta_nueva_gastos = False
if gastos_csv.exists():
    batch_id = create_file_batch_id(gastos_csv)
    ya_ingerido = (manifest["_batch_id"] == batch_id).any()
    if ya_ingerido:
        print(f"- {gastos_csv.name} ya fue ingerido (batch_id={batch_id}), se omite.")
    else:
        df = pd.read_csv(gastos_csv, encoding="utf-8", sep=";")
        df["_source_file"] = gastos_csv.name
        df["_ingest_ts"] = utcnow
        df["_batch_id"] = batch_id
        raw_gastos.append(df)
        manifest = pd.concat([
            manifest,
            pd.DataFrame([{
                "_batch_id": batch_id,
                "_source_file": gastos_csv.name,
                "_ingest_ts": utcnow,
                "n_rows": len(df)
            }])
        ], ignore_index=True)
        
        ingesta_nueva_gastos = True
        print(f"✓ Ingesta: {gastos_csv.name} → batch_id={batch_id}")

# ----- PRESUPUESTO -----
# Los mismos procesos que en GASTOS
ingesta_nueva_presup = False
if presupuesto_csv.exists():
    batch_id = create_file_batch_id(presupuesto_csv)
    ya_ingerido = (manifest["_batch_id"] == batch_id).any()
    if ya_ingerido:
        print(f"- {presupuesto_csv.name} ya fue ingerido (batch_id={batch_id}), se omite.")
    else:
        df = pd.read_csv(presupuesto_csv, encoding="utf-8", sep=";")
        df["_source_file"] = presupuesto_csv.name
        df["_ingest_ts"] = utcnow
        df["_batch_id"] = batch_id
        raw_presup.append(df)
        manifest = pd.concat([
            manifest,
            pd.DataFrame([{
                "_batch_id": batch_id,
                "_source_file": presupuesto_csv.name,
                "_ingest_ts": utcnow,
                "n_rows": len(df)
            }])
        ], ignore_index=True)
        ingesta_nueva_presup = True
        print(f"✓ Ingesta: {presupuesto_csv.name} → batch_id={batch_id}")

# combinar ingestas
if raw_gastos:  # Si hay uno o más DataFrames nuevos
    gastos_raw = pd.concat(raw_gastos, ignore_index=True)
else:            # Si la lista está vacía
    gastos_raw = pd.DataFrame()

if raw_presup:  # Si hay uno o más DataFrames nuevos
    presup_raw = pd.concat(raw_presup, ignore_index=True)
else:            # Si la lista está vacía
    presup_raw = pd.DataFrame()    

# ----- GUARDAR EN PARQUET (BRONZE)-----
# si no hubo ingesta nueva, reutiliza lo que estaba guardado
gastos_bronze_path = BRONZE / "gastos_raw.parquet"
presupuesto_bronze_path = BRONZE / "presupuesto_raw.parquet"

if gastos_raw.empty and gastos_bronze_path.exists():
    gastos_raw = pd.read_parquet(gastos_bronze_path)
if presup_raw.empty and presupuesto_bronze_path.exists():
    presup_raw = pd.read_parquet(presupuesto_bronze_path)

# guardar bronze si hubo ingesta nueva
if ingesta_nueva_gastos and not gastos_raw.empty:
    gastos_raw.to_parquet(gastos_bronze_path, index=False)
if ingesta_nueva_presup and not presup_raw.empty:
    presup_raw.to_parquet(presupuesto_bronze_path, index=False)

# actualizar manifest
manifest.to_parquet(manifest_path, index=False)

print(f"\n✓ Bronze guardado: {BRONZE}")
print(f" - gastos_raw.parquet: {len(gastos_raw)} filas")
print(f" - presupuesto_raw.parquet: {len(presup_raw)} filas")
print(f" - manifest: {len(manifest)} batches registrados")

# -----------------------------------------------------
# 2. LIMPIEZA (SILVER)
# -----------------------------------------------------
print("\n" + "-" * 70)
print("RETO 2: LIMPIEZA - SILVER (CLEAN)")
print("-" * 70)

# --- PRESUPUESTO ---
# Creamos una copia del presupuesto original (presup_raw) para no modificar el DataFrame crudo.
presup_df = presup_raw.copy()
presup_df["area_normalizada"] = presup_df["area"].apply(normalize_text)
presup_df["partida_normalizada"] = presup_df["partida"].apply(normalize_text)
# Convierte la columna a tipo numérico. Si hay texto o valores inválidos los reemplaza por NaN.
presup_df["presupuesto"] = pd.to_numeric(presup_df["presupuesto"], errors="coerce")

# tenga área y partida válidas (no vacías)
# tenga presupuesto numérico
# que sea mayor o igual a 0
presup_valid = (
    presup_df["area_normalizada"].isin(AREAS_NORM) & #.notna()
    presup_df["partida_normalizada"].isin(PARTIDAS_NORM) & #.notna()
    presup_df["presupuesto"].notna() & 
    (presup_df["presupuesto"] >= 0) &
    (presup_df["presupuesto"] <= MAX_PRESUPUESTO)
)

presup_clean = presup_df.loc[presup_valid].copy()   # devuelve las filas con datos correctos
presup_quar = presup_df.loc[~presup_valid].copy()   # devuelve las filas con datos incorrectos (datos que van a cuarentena)

# conjunto de partidas válidas (normalizadas)
if not presup_clean.empty:
    # Ordeno por fecha de ingesta (para conservar el más reciente)
    presup_clean = presup_clean.sort_values("_ingest_ts", ascending=True)
    # aqui genero la clave natural
    # Si hay varias filas para la misma área/partida (múltiples ingestas o actualizaciones), 
    # Elimino duplicados de área + partida, me quedo con la última versión (keep="last").
    presup_clean = presup_clean.drop_duplicates(subset=["area_normalizada", "partida_normalizada"], keep="last")
    # Si hay datos en el presupuesto limpio, obtengo todas las partidas únicas y las guardo en un conjunto.
    valid_partidas_presupuesto = set(presup_clean["partida_normalizada"].unique())
else:
    # Si el DataFrame está vacío, crea un conjunto vacío.
    valid_partidas_presupuesto = set()

# --- GASTOS ---
gastos_df = gastos_raw.copy()
gastos_df["area_normalizada"] = gastos_df["area"].apply(normalize_text)
gastos_df["partida_normalizada"] = gastos_df["partida"].apply(normalize_text)
# fecha → tipo datetime (fechas inválidas se vuelven NaT)
gastos_df["fecha"] = pd.to_datetime(gastos_df["fecha"], errors="coerce")
#importe → numérico (errores se vuelven NaN)
gastos_df["importe"] = pd.to_numeric(gastos_df["importe"], errors="coerce")

gastos_df["_quarantine_cause"] = ""
gastos_df.loc[gastos_df["fecha"].isna(), "_quarantine_cause"] += "fecha_invalida; "
gastos_df.loc[gastos_df["importe"].isna() | (gastos_df["importe"] < 0), "_quarantine_cause"] += "importe_invalido; "
gastos_df.loc[gastos_df["importe"] > MAX_IMPORTE_GASTO, "_quarantine_cause"] += "importe_excesivo; "

gastos_df.loc[~gastos_df["area_normalizada"].isin(AREAS_NORM), "_quarantine_cause"] += "area_no_valida; "
gastos_df.loc[~gastos_df["partida_normalizada"].isin(PARTIDAS_NORM), "_quarantine_cause"] += "partida_no_valida; "

if valid_partidas_presupuesto:
    gastos_df.loc[~gastos_df["partida_normalizada"].isin(valid_partidas_presupuesto), "_quarantine_cause"] += "partida_no_en_presupuesto; "

gastos_df["_quarantine_cause"] = gastos_df["_quarantine_cause"].str.strip("; ").replace("", None)

gastos_quar = gastos_df[gastos_df["_quarantine_cause"].notna()].copy()
gastos_clean = gastos_df[gastos_df["_quarantine_cause"].isna()].copy()

if not gastos_clean.empty:
    gastos_clean = gastos_clean.sort_values("_ingest_ts", ascending=True)
    # aqui genero la clave natural
    gastos_clean = gastos_clean.drop_duplicates(subset=["fecha", "area_normalizada", "partida_normalizada"], keep="last")

print(f"Presupuesto: {len(presup_df)} → Clean={len(presup_clean)}, Quarantine={len(presup_quar)}")
print(f"Gastos: {len(gastos_df)} → Clean={len(gastos_clean)}, Quarantine={len(gastos_quar)}")

presup_clean.to_parquet(SILVER / "presupuesto_clean.parquet", index=False)
gastos_clean.to_parquet(SILVER / "gastos_clean.parquet", index=False)
if not presup_quar.empty:
    presup_quar.to_parquet(QUARANTINE / "presupuesto_invalidos.parquet", index=False)
if not gastos_quar.empty:
    gastos_quar.to_parquet(QUARANTINE / "gastos_invalidos.parquet", index=False)

# -----------------------------------------------------
# 3. ORO: KPI + TENDENCIA + PERSISTENCIA + REPORTE
# -----------------------------------------------------

# Esta función toma:
#  -los gastos limpios (gastos_clean)
#  - el presupuesto limpio (presup_clean)
# y devuelve un DataFrame que tiene, para cada área + partida:
#  - presupuesto
#  - gasto acumulado
#  - y el KPI de ejecución (gasto / presupuesto)

# Aquí se usan los datos SILVER, se construye Oro (df_kpi y monthly) y luego se pasas a guardar (punto 4) y a reporte (punto 5).

# Un KPI es una medida numérica que se usa para evaluar si una actividad, proceso o área está cumpliendo sus objetivos.
def build_kpi(df_gastos_valid: pd.DataFrame, df_pres: pd.DataFrame) -> pd.DataFrame:
    # Agrupa los gastos por área y partida
    gasto_agg = (
        df_gastos_valid
        .groupby(["area_normalizada", "partida_normalizada"], as_index=False)
        .agg(gasto_acumulado=("importe", "sum"))
    )

    #Prepara el presupuesto con las columnas indicadas
    pres_cols = ["area_normalizada", "partida_normalizada", "area", "partida", "presupuesto"]
    df_pres_small = df_pres[pres_cols].copy()

    # Para cada partida del presupuesto, coge lo que se ha gastado. Si no hubo gasto, queda NaN.
    df_kpi = df_pres_small.merge(
        gasto_agg,
        on=["area_normalizada", "partida_normalizada"],
        how="left"
    )
    
    # Rellena nulos y redondea
    df_kpi["gasto_acumulado"] = df_kpi["gasto_acumulado"].fillna(0).round(2)
    df_kpi["presupuesto"] = df_kpi["presupuesto"].fillna(0).round(2)

    # Calcula el KPI
    # Si el presupuesto es 0 → KPI = None (evita división por 0).
    # Si no, KPI = gasto / presupuesto.
    def calc_kpi(row):
        if row["presupuesto"] == 0:
            return None
        return round(row["gasto_acumulado"] / row["presupuesto"], 4)

    df_kpi["kpi_ejecucion"] = df_kpi.apply(calc_kpi, axis=1)
    print("✓ build_kpi completado")
    return df_kpi

# Esta función saca la tendencia mensual de gastos.
def build_monthly_trend(df_gastos_valid: pd.DataFrame) -> pd.DataFrame:
    # Copia el DataFrame de gastos limpios para no tocar el original.
    df = df_gastos_valid.copy()

    # Crea una columna de mes (ignorando el día)
    df["year_month"] = df["fecha"].dt.to_period("M").astype(str)

    # Esto garantia que area siempre exista
    if "area" not in df.columns or df["area"].isna().all():
        df["area"] = df["area_normalizada"]

    # Agrupa por mes y area    
    monthly = (
        df.groupby(["year_month", "area"], as_index=False)
        .agg(gasto_mensual=("importe", "sum"))
    )
    print("✓ build_monthly_trend completado")
    return monthly

# -----------------------------------------------------
# 4. ALMACENAMIENTO: SQLITE
# -----------------------------------------------------

# Guarda los resultados en formato Parquet (más rápido y ligero).
# Guarda los mismos datos en una base de datos SQLite, junto con una vista (VIEW) que resume los KPI por área.

# El formato Parquet es ideal para análisis posteriores:
# - Compacto y comprimido.
# - Lee y escribe rápido.
# - Compatible con pandas, Spark, Power BI, etc.

#  data/storage/gold/
#  ├─ kpi_ejecucion.parquet
#  └─ tendencia_mensual.parquet

def save_parquet(df_kpi: pd.DataFrame, monthly: pd.DataFrame):
    # Crea la carpeta Oro (GOLD) si no existe.
    GOLD.mkdir(exist_ok=True)
    df_kpi.to_parquet(GOLD / "kpi_ejecucion.parquet", index=False)
    monthly.to_parquet(GOLD / "tendencia_mensual.parquet", index=False)
    print(f"✓ Oro parquet guardado en: {GOLD}")


# SQLite es una base de datos liviana que se guarda en un solo archivo .db, sin necesidad de servidor.
# SQLite (sql/finanzas.db):
# Tablas:
#  - kpi_ejecucion
#  - tendencia_mensual
# Vista:
#  - vw_kpi_area

def save_sqlite(df_kpi: pd.DataFrame, monthly: pd.DataFrame):
    # Crea/abre la base de datos SQLite en sql/finanzas.db.
    conn = sqlite3.connect(SQLITE_PATH)
    # Si ya existen, las reemplaza (if_exists="replace").
    df_kpi.to_sql("kpi_ejecucion", conn, if_exists="replace", index=False)
    monthly.to_sql("tendencia_mensual", conn, if_exists="replace", index=False)

    # Crea una vista (VIEW)
    # Crea una “tabla virtual” llamada vw_kpi_area que resume los KPI por área (area, gasto_total, presupuesto_total, kpi_ejecucion_area)
    # Suma el gasto y presupuesto de cada área.
    # Calcula el KPI promedio (gasto/presupuesto).
    # Ordena de mayor a menor ejecución.
    create_view = """
    CREATE VIEW IF NOT EXISTS vw_kpi_area AS
    SELECT 
        area,
        SUM(gasto_acumulado) AS gasto_total,
        SUM(presupuesto) AS presupuesto_total,
        CASE
            WHEN SUM(presupuesto) = 0 THEN NULL
            ELSE ROUND(SUM(gasto_acumulado) / SUM(presupuesto), 4)
        END AS kpi_ejecucion_area
    FROM kpi_ejecucion
    GROUP BY area
    ORDER BY kpi_ejecucion_area DESC;
    """
    conn.execute(create_view)
    conn.commit()
    conn.close()
    print(f"✓ SQLite actualizado en: {SQLITE_PATH}")

# -----------------------------------------------------
# 5. REPORTE MARKDOWN
# -----------------------------------------------------
def generate_report(df_kpi: pd.DataFrame, monthly: pd.DataFrame, invalid_gastos: pd.DataFrame):
    report_path = OUT / "reporte.md"

    kpi_area = (
        df_kpi.groupby("area", as_index=False)
        .agg(
            presupuesto=("presupuesto", "sum"),
            gasto_acumulado=("gasto_acumulado", "sum")
        )
    )
    kpi_area["kpi_ejecucion"] = kpi_area.apply(
        lambda r: None if r["presupuesto"] == 0 else round(r["gasto_acumulado"]/r["presupuesto"], 4),
        axis=1
    )

    lines = []
    lines.append("# Informe de Ejecución Presupuestaria\n")
    lines.append(f"_Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n")
    lines.append("## 1. Contexto\n")
    lines.append("- Fuente: `gastos.csv` y `presupuesto.csv`.\n")
    lines.append("- Actualización: batch (ETL ligero) previo a capa oro.\n")
    lines.append("- Objetivo: medir la ejecución del presupuesto por área y partida.\n")

    lines.append("## 2. Definiciones de KPI\n")
    lines.append("- **gasto_acumulado**: suma de los importes registrados en `gastos.csv` para un área/partida.\n")
    lines.append("- **presupuesto**: importe planificado en `presupuesto.csv`.\n")
    lines.append("- **kpi_ejecucion** = gasto_acumulado / presupuesto.\n")
    lines.append("- **Interpretación**: valores > 1 implican sobre-ejecución.\n")

    lines.append("## 3. Ejecución por área\n")
    lines.append("| Área | Presupuesto | Gasto acumulado | KPI ejecución |\n")
    lines.append("|------|-------------|-----------------|---------------|\n")
    for _, r in kpi_area.iterrows():
        lines.append(
            f"| {r['area']} | {r['presupuesto']:.2f} | {r['gasto_acumulado']:.2f} | "
            f"{'' if pd.isna(r['kpi_ejecucion']) else f'{r['kpi_ejecucion']*100:.1f}%'} |\n"
        )

    lines.append("\n## 4. Ejecución por área y partida\n")
    lines.append("| Área | Partida | Presupuesto | Gasto acumulado | KPI |\n")
    lines.append("|------|---------|-------------|-----------------|-----|\n")
    for _, r in df_kpi.sort_values(["area", "partida"]).iterrows():
        lines.append(
            f"| {r['area']} | {r['partida']} | {r['presupuesto']:.2f} | {r['gasto_acumulado']:.2f} | "
            f"{'' if pd.isna(r['kpi_ejecucion']) else f'{r['kpi_ejecucion']*100:.1f}%'} |\n"
        )

    lines.append("\n## 5. Tendencia mensual de gasto (por área)\n")
    lines.append("| Mes | Área | Gasto mensual |\n")
    lines.append("|-----|------|----------------|\n")
    for _, r in monthly.sort_values(["year_month", "area"]).iterrows():
        lines.append(f"| {r['year_month']} | {r['area']} | {r['gasto_mensual']:.2f} |\n")

    if not invalid_gastos.empty:
        lines.append("\n## 6. Filas en cuarentena (gastos descartados)\n")
        lines.append("| fecha | area | partida | importe | causa |\n")
        lines.append("|-------|------|---------|---------|--------|\n")
        for _, r in invalid_gastos.iterrows():
            fecha = r["fecha"].date().isoformat() if pd.notna(r["fecha"]) else ""
            importe = f"{r['importe']:.2f}" if pd.notna(r["importe"]) else ""
            causa = r.get("_quarantine_cause", "")
            lines.append(
                f"| {fecha} | {r['area']} | {r['partida']} | {importe} | {causa} |\n"
            )

    with open(report_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"✓ Reporte generado en: {report_path}")


# ejecutar capa oro y reporte con lo que ya salió de silver
print("\n" + "-" * 70)
print("3. ORO: KPI + TENDENCIA + PERSISTENCIA + REPORTE")
print("-" * 70)
df_kpi = build_kpi(gastos_clean, presup_clean)
monthly = build_monthly_trend(gastos_clean)

print("\n" + "-" * 70)
print("4. ALMACENAMIENTO: SQLITE + VISTAS")
print("-" * 70)
save_parquet(df_kpi, monthly)
save_sqlite(df_kpi, monthly)

print("\n" + "-" * 70)
print("5. REPORTE MARKDOWN")
print("-" * 70)
generate_report(df_kpi, monthly, gastos_quar)


