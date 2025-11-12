# ETL Finanzas — Presupuesto vs Gastos

## 1. Objetivo
Implementar un **proceso ETL ligero e idempotente** para comparar **presupuesto vs gasto** por área y partida, con el fin de:
- Calcular el **KPI de ejecución presupuestaria** (`gasto_acumulado / presupuesto`).
- Detectar **sobre-ejecuciones** y **sub-ejecuciones**.
- Generar un **reporte automatizado** y trazable para la toma de decisiones financieras.

> **Problema que resuelve:**  
> La falta de un control sobre la ejecución presupuestaria, dependiente de hojas de cálculo manuales y sin trazabilidad.

## 2. Estructura del proyecto

```text
project/
├─ data/
│  ├─ drops/               # CSV de entrada (presupuesto.csv, gastos.csv)
│  ├─ quarantine/          # registros inválidos
│  └─ storage/
│     ├─ bronze/           # ingesta cruda, con batch_id y manifest
│     ├─ silver/           # datos limpios (clean)
│     └─ gold/             # indicadores listos para explotar
├─ docs/                   # documentación proyecto
├─ ingest/
│  ├─ get_data.py          # genera los CSV de ejemplo
│  └─ run.py               # programa principal: parquet + sqlite + reporte.md
├─ output/
│  └─ reporte.md           # informe generado
└─ sql/
   └─ finanzas.db          # SQLite con tablas y vista
```

## 3. Flujo resumido

| Etapa | Descripción | Output |
|-------|--------------|--------|
| **1. BRONZE – Ingesta** | Lee `presupuesto.csv` y `gastos.csv` desde `data/drops/`.<br>Añade `_source_file`, `_ingest_ts`, `_batch_id`.<br>Evita duplicar con `ingest_manifest.parquet`. | `data/storage/bronze/*.parquet` |
| **2. SILVER – Limpieza** | Normaliza textos, valida áreas/partidas, tipos y rangos. <br>Separa registros válidos (clean) e inválidos (quarantine). | `data/storage/silver/*.parquet` y `data/quarantine/*.parquet` |
| **3. GOLD – Indicadores** | Calcula **KPI de ejecución** (`gasto/presupuesto`).<br>Calcula **tendencia mensual** del gasto por área. | `data/storage/gold/*.parquet` |
| **4. SQLite** | Guarda tablas `kpi_ejecucion`, `tendencia_mensual`.<br>Crea vista `vw_kpi_area` con resumen por área. | `sql/finanzas.db` |
| **5. Reporte** | Genera informe Markdown con resumenes, tendencias y filas inválidas. | `output/reporte.md` |

---

## 4. Ejecución
```bash
pip install -r project/requirements.txt
python ingest/get_data.py      # genera los CSV de ejemplo
python ingest/run.py           # programa principal: parquet + sqllite + reporte.md
```
---

## 5. Publicación web (GitHub)
- https://github.com/IA-CSG/Proyecto_UT1_RA1_BA/tree/main/project