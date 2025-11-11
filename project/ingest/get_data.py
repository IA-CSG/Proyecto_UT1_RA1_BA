import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
from tqdm import trange
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

DROPS = ROOT / "data" / "drops"
DROPS.mkdir(parents=True, exist_ok=True)

AREAS = ["RRHH", "IT", "Marketing", "Ventas", "Operaciones", "Calidad", "Contabilidad", "Direccion", "Administracion", "I+D"]
PARTIDAS = ["Personal", "Software", "Hardware", "Formacion", "Viajes", "Publicidad", "Suministros", "Alquileres", "Mantenimiento", "Seguros"]

# INYECTAR ERRORES
def inyectar_error(registro: dict, df_presup: pd.DataFrame):
    # Modifica el dict 'registro' metiendo un error aleatorio.    
    tipo_error = random.randint(1, 7)

    if tipo_error == 1:     # area mal
        registro["area"] = "XXX-AREA MALA"

    elif tipo_error == 2:   # partida nula
        registro["area"] = np.nan        

    if tipo_error == 3:     # partida mal
        registro["partida"] = "XXX-PARTIDA MALA"

    elif tipo_error == 4:   # partida nula
        registro["partida"] = np.nan

    elif tipo_error == 5:   # fecha incorrecta
        registro["fecha"] = "2025-13-40"

    elif tipo_error == 6:
        # importe fuera del intervalo negativo
        registro["importe"] = -500.0
    elif tipo_error == 7:
        # importe fuera del intervalo
        # si sabemos el area/partida podemos buscar el presupuesto para exagerar
        #presup_row = df_presup[(df_presup["area"] == registro["area"]) & (df_presup["partida"] == registro["partida"])]
        #if not presup_row.empty:
            #presup = presup_row.iloc[0]["presupuesto"]
            # algo muy por encima
            #registro["importe"] = round(presup * 2.5, 2)
        #else:
            # si no hay presupuesto, ponemos algo muy alto
            registro["importe"] = 10_000_000.0

    return registro

# 1. Generar presupuestos.csv
presup_data = []
for area in AREAS:
    for partida in PARTIDAS:
        presup = random.randint(10000, 200000)
        presup_data.append({
            "area": area,
            "partida": partida,
            "presupuesto": presup
        })

df_presup = pd.DataFrame(presup_data)
df_presup.to_csv(DROPS / "presupuesto.csv", index=False, encoding="utf-8", sep=";")
print(f"✓ {DROPS / 'presupuesto.csv'} ({len(df_presup)} filas)")

# 2. Generar gastos.csv
gastos_data = []
start = datetime(2025, 1, 1)
N = 10000
PROB_ERROR = 0.10  # 10%
errores = 0 # errores generados

for i in trange(N, desc="Generando gastos"):
    # fecha correcta
    fecha = start + timedelta(days=random.randint(0, (datetime.now() - start).days))
    area = random.choice(AREAS)
    partida = random.choice(PARTIDAS)

    # calcular importe "normal"
    presup_row = df_presup[(df_presup["area"] == area) & (df_presup["partida"] == partida)]
    if not presup_row.empty:
        presup = presup_row.iloc[0]["presupuesto"]
        importe = random.uniform(100, presup * 0.1)
    else:
        importe = random.uniform(100, 5000)

    registro = {
        "fecha": fecha.strftime("%Y-%m-%d"),
        "area": area,
        "partida": partida,
        "importe": round(importe, 2)
    }

    # aquí decidimos si metemos error
    if random.random() <= PROB_ERROR:
        registro = inyectar_error(registro, df_presup)        
        errores += 1  # incrementa el contador

    gastos_data.append(registro)

print(f"Se generaron {errores} registros con errores de un total de {N} registros.")

# Errores manuales:
# gastos_data.append({"fecha": "2025-03-15", "area": " rrhh ", "partida": "Personal", "importe": 1500.50})

df_gastos = pd.DataFrame(gastos_data)
df_gastos.to_csv(DROPS / "gastos.csv", index=False, encoding="utf-8", sep=";")
print(f"✓ {DROPS / 'gastos.csv'} ({len(df_gastos)} filas)")
