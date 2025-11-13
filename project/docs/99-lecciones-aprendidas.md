\newpage
# Lecciones aprendidas <Br> (99-lecciones-aprendidas.md)

## 1. Qué salió bien

- **Diseño modular del ETL:** la separación por capas (bronze → silver → gold) facilitó la depuración y permitió validar cada etapa por separado.

- **Idempotencia implementada correctamente:** el uso del `batch_id` (hash del archivo) evitó duplicados y permitió reejecuciones seguras.

- **Quarantine con causa documentada:** permitió detectar errores comunes (fechas inválidas, partidas fuera de dominio) sin interrumpir el flujo completo.

- **Reporte automático en Markdown:** el informe final consolidó KPIs, calidad de datos y notas de interpretación, mejorando la trazabilidad del proceso.

- **Trazabilidad técnica clara:** en **bronze** y **silver** mediante `_ingest_ts`, `_source_file`, `_batch_id`.

- **Uso de SQLite + Parquet:** combinó velocidad de consulta con persistencia portable, ideal para pruebas locales.

---

## 2. Qué mejorar

- **Automatización del pipeline:** actualmente la ejecución es manual.

- **Alertas y monitoreo:** falta un control automatizado de % de cuarentena o de sobre-ejecución presupuestaria (notificación por correo).

- **Validación temprana de esquema:** agregar validación de columnas esperadas al leer CSV para evitar errores silenciosos.

- **Particionado temporal:** particionar los Parquet por `año/mes` para acelerar consultas históricas.

---

## 3. Siguientes pasos

1. **Programar ejecución automática** (diaria o semanal) con logs centralizados.

2. **Añadir validaciones adicionales**: control cruzado de totales entre gastos y presupuesto.

3. **Visualización interactiva**: generar dashboard en Power BI.

4. **Ampliar el modelo** para incluir presupuestos plurianuales o comparativos interanuales.

---

## 4. Apéndice (evidencias)

**Evidencias complementarias**

- Archivos Parquet de cada capa (`bronze/`, `silver/`, `gold/`)

- Reporte generado: `output/reporte.md`

- Vista `vw_kpi_area` en **SQLite** con agregación por área

---

