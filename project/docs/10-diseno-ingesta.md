# Diseño de Ingestión <Br> 10-diseno-ingesta.md

## Resumen
- Los datos de **presupuesto** y **gastos** entran desde ficheros CSV depositados en una ruta controlada (`data/drops/`).
- La ingesta se ejecuta en modo **batch** (por archivo) y es **idempotente**: si un archivo ya fue procesado, no se vuelve a cargar.
- La trazabilidad se registra mediante `_ingest_ts`, `_source_file`, `_batch_id` y se mantiene un **manifest** de ingestas para evitar duplicados.
- Las filas inválidas se envían a **cuarentena** `data/quarantine`con los motivos.

---

## Fuente

- **Origen:**  
  - `data/drops/gastos.csv`  
  - `data/drops/presupuesto.csv`
- **Formato:** CSV (UTF-8, separado por `;`)
- **Frecuencia esperada:** batch manual.  

---

## Estrategia

- **Modo:** batch por archivo.
- **Incremental:** controlado por archivo mediante **hash del archivo**. No se reingesta el mismo archivo (con mismo path, tamaño y mtime).
- **Particionado:** no se particiona físicamente en disco por fecha; se guarda en Parquet en capas (`bronze/`, `silver/`, `gold/`).  

---

## Idempotencia y deduplicación

- **batch_id:**  
  - Se calcula como `md5(path + tamaño + mtime)` lo que garantiza que si el archivo no cambia, el `batch_id` es el mismo.
  - Se persiste en `bronze/ingest_manifest.parquet`.
- **Clave natural (lógica):**  
  - Para **gastos**: (`fecha`, `area_normalizada`, `partida_normalizada`)  
  - Para **presupuesto**: (`area_normalizada`, `partida_normalizada`)
- **Política de deduplicación:**  
  - **último gana por `_ingest_ts`**.  
  - Se ordenan los registros por `_ingest_ts` ascendente y se hace `drop_duplicates(..., keep="last")` en silver.
  - Esto permite reinyectar el mismo registro corregido en una ingesta posterior.

---

## Checkpoints y trazabilidad

- **Checkpoint / manifest:**  
  - `bronze/ingest_manifest.parquet` guarda: `_batch_id`, `_source_file`, `_ingest_ts`, `n_rows`.
  - Antes de ingerir un archivo nuevo, se consulta este manifest y si el `batch_id` ya existe, se omite.
- **Trazabilidad:**  
  - Cada fila ingerida lleva:
    - `_ingest_ts`: timestamp UTC de la ingesta
    - `_source_file`: nombre del CSV origen
    - `_batch_id`: identificador único del archivo (hash md5)
  - En capa oro no se conserva la trazabilidad.
- **Quarantine:**  
  - Ruta: `data/quarantine/`
  - Ficheros: `gastos_invalidos.parquet`, `presupuesto_invalidos.parquet`
  - Motivos registrados en `_quarantine_cause`:
    - `fecha_invalida`
    - `importe_invalido`
    - `importe_excesivo`
    - `area_no_valida`
    - `partida_no_valida`
    - `partida_no_en_presupuesto`

---

## SLA (Service Level Agreement)

- **Disponibilidad:** bajo demanda cuando haya nuevos CSV.
- **Retries / alertas:** el manifest evita reprocesos, pero no hay alerta automática si un CSV viene vacío o todo va a cuarentena. Esto se puede cubrir leyendo el conteo de inválidos tras la ejecución y notificando.

---

## Riesgos / Antipatrones

- **Batch con latencia de segundos:** el diseño actual es por archivo; si se requiere casi-real-time habría que pasar a micro-batch programado (cada 1–5 min) o a un origen tipo cola.
- **Falta de clave natural en el CSV:** la clave natural deriva de (`fecha`, `area_normalizada`, `partida_normalizada`). Si en el futuro hay dos gastos distintos el mismo día para la misma partida y área, se añadiría una columna (ej. `nro_doc`) a la clave.
- **CSV con cambio de estructura:** el `read_csv` actual asume columnas esperadas; un cambio de encabezado rompería la ingesta y debería registrarse en quarantine o en un log aparte.
