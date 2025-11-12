# Reglas de Limpieza y Calidad

## Tipos y formatos

| Campo | Tipo esperado | Validación / Formato |
|--------|----------------|----------------------|
| `fecha` | `datetime` ISO (`YYYY-MM-DD` o `TIMESTAMP UTC`) | Se convierte con `pd.to_datetime(..., errors="coerce")`. Filas con fecha inválida → **quarantine**. |
| `importe`, `presupuesto` | `DECIMAL(18,2)` | Numérico ≥ 0. Se redondea a 2 decimales. |
| `area`, `partida` | texto normalizado | Se limpian tildes, espacios, se pasa a minúsculas. Campos vacíos → **quarantine**. |

---

## Nulos

**Campos obligatorios:**
- `fecha`
- `area`
- `partida`
- `importe` o `presupuesto` (según dataset)

**Tratamiento:**
- Si cualquiera de estos es nulo o no convertible al tipo esperado, la fila se marca con `_quarantine_cause` indicando el motivo (por ejemplo: `fecha_invalida`, `importe_invalido`, `partida_vacia`).
- Las filas inválidas se envían a:
  - `data/quarantine/gastos_invalidos.parquet`
  - `data/quarantine/presupuesto_invalidos.parquet`

---

## Rangos y dominios

| Regla | Descripción |
|--------|--------------|
| `importe >= 0` y `presupuesto >= 0` | Importes negativos no permitidos. |
| `importe ≤ 1_000_000` | Protección contra valores atípicos o errores de carga. |
| `fecha ≤ hoy` | No se admiten fechas futuras. |
| `area_normalizada` y `partida_normalizada` | Deben existir en las listas de presupuesto válidas. |

**Filas fuera de rango o dominio** → **quarantine** con causa.

---

## Deduplicación

- **Clave natural (por dataset):**
  - **Presupuesto:** (`area_normalizada`, `partida_normalizada`)
  - **Gastos:** (`fecha`, `area_normalizada`, `partida_normalizada`)
- **Política:**  
  - **Último gana por `_ingest_ts`**.
  - Se ordenan los registros por `_ingest_ts` ascendente y se ejecuta `drop_duplicates(..., keep="last")`.
  - Esto permite recargar el mismo registro con datos actualizados sin generar duplicados.

---

## Estandarización de texto

- Se aplica función `normalize_text()` que:
  - Elimina tildes y caracteres diacríticos (`NFKD`).
  - Convierte a **minúsculas**.
  - Aplica `strip()` para quitar espacios antes y después.
- Evita problemas de comparación entre "Finanzas", "finanzas" y "finánzas".

---

## Trazabilidad

Cada fila procesada en **bronze**, **silver** y **gold** conserva metadatos técnicos:

| Campo | Descripción |
|--------|--------------|
| `_ingest_ts` | Timestamp UTC de la ingesta. |
| `_source_file` | Nombre del archivo fuente (CSV). |
| `_batch_id` | Identificador único del archivo (hash md5). |
| `last_ingest_ts` / `source_files` | (en oro) Máximo `_ingest_ts` y lista de orígenes. |

Estos campos permiten rastrear cualquier valor desde la capa oro hasta su fuente original.

---

## QA (Quality Assurance) --- NO IMPLEMENTADO ---

QA es el conjunto de prácticas y controles que se aplican para garantizar que los datos sean correctos, coherentes y útiles antes de usarlos para análisis o decisiones.

