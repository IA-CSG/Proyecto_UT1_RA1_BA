\newpage
# Reglas de Limpieza y Calidad <Br> (20-limpieza-calidad.md)

## Tipos y formatos

| Campo | Tipo esperado | Validación / Formato |
|--------|----------------|----------------------|
| `fecha` | `datetime` ISO (`YYYY-MM-DD` o `TIMESTAMP UTC`) | Se convierte con `pd.to_datetime(..., errors="coerce")`. Filas con fecha inválida → **quarantine**. |
| `importe`, `presupuesto` | `DECIMAL(18,2)` | Numérico ≥ 0. <Br> Se redondea a 2 decimales. |
| `area`, `partida` | texto normalizado | Se limpian tildes, espacios, se pasa a minúsculas. <Br> Campos vacíos → **quarantine**. |

---

## Nulos

**Campos obligatorios:**
- `fecha`
- `area`
- `partida`
- `importe` / `presupuesto` (según dataset)

**Tratamiento:**

- Si cualquiera de estos campos es nulo o no convertible al tipo esperado, la fila se marca con `_quarantine_cause` indicando el motivo (ejemplo: `fecha_invalida`, `partida_vacia`).

- Puede haber varios motivos por los que una fila no es válida, se registran todos en `_quarantine_cause`

- Las filas inválidas se envían a:

  - `data/quarantine/gastos_invalidos.parquet`

  - `data/quarantine/presupuesto_invalidos.parquet`

---

## Rangos y dominios

| Regla | Descripción |
|--------|--------------|
| `importe >= 0` y `presupuesto >= 0` | Importes negativos no permitidos. |
| `importe ≤ 300_000` | Protección contra valores atípicos o errores de carga. |
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

Cada fila procesada en **bronze** y **silver** conserva metadatos técnicos:

| Campo | Descripción |
|--------|--------------|
| `_ingest_ts` | Timestamp UTC de la ingesta. (se genera al leer el CSV) |
| `_source_file` | Nombre del archivo origen (gastos.csv o presupuesto.csv). |
| `_batch_id` | Identificador único del archivo (hash MD5 basado en ruta, tamaño y fecha de modificación). |

**Nota**:

- En las capas **bronze** y **silver** se conservan los metadatos `_ingest_ts`, `source_files` y `_batch_id` para cada fila.

- En la capa **oro**, se agregan los datos limpios sin estos campos técnicos (no se conserva trazabilidad a nivel de fila).

---

## QA (Quality Assurance) --- NO IMPLEMENTADO ---

QA es el conjunto de prácticas y controles que se aplican para garantizar que los datos sean correctos, coherentes y útiles antes de usarlos para análisis o decisiones.

