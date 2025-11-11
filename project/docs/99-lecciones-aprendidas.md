# Lecciones aprendidas

## ✅ Qué salió bien

- **Diseño modular del ETL:** la separación por capas (bronze → silver → gold) facilitó la depuración y permitió validar cada etapa por separado.  
- **Idempotencia implementada correctamente:** el uso del `batch_id` (hash del archivo) evitó duplicados y permitió reejecuciones seguras.  
- **Quarantine con causa documentada:** permitió detectar errores comunes (fechas inválidas, partidas fuera de dominio) sin interrumpir el flujo completo.  
- **Reporte automático en Markdown:** el informe final consolidó KPIs, calidad de datos y notas de interpretación, mejorando la trazabilidad del proceso.  
- **Trazabilidad técnica clara:** `_ingest_ts`, `_source_file`, `_batch_id` propagados hasta capa oro.  
- **Uso de SQLite + Parquet:** combinó velocidad de consulta con persistencia portable, ideal para pruebas locales.  

---

## ⚙️ Qué mejorar

- **Automatización del pipeline:** actualmente la ejecución es manual; podría orquestarse con cron o un workflow (Airflow, Dagster, Prefect).  
- **Alertas y monitoreo:** falta un control automatizado de % de cuarentena o de sobre-ejecución presupuestaria (notificación por correo/Slack).  
- **Validación temprana de esquema:** agregar validación de columnas esperadas al leer CSV para evitar errores silenciosos.  
- **Particionado temporal:** particionar los Parquet por `year/month` para acelerar consultas históricas.  
- **Control de versiones de datos:** versionar los datasets ingeridos en `bronze/` junto con su `batch_id` para auditoría.  
- **Documentación técnica:** completar el README con dependencias exactas (versión de pandas, pyarrow, sqlite3, etc.).

---

## 🔜 Siguientes pasos

1. **Programar ejecución automática** (diaria o semanal) con logs centralizados.  
2. **Añadir validaciones adicionales** (p. ej., control cruzado de totales entre gastos y presupuesto).  
3. **Visualización interactiva**: generar dashboard en Power BI / Streamlit a partir de los Parquet de oro.  
4. **Ampliar el modelo** para incluir presupuestos plurianuales o comparativos interanuales.  
5. **Integrar control de calidad en CI/CD** (GitHub Actions, Quartz o similar).  

---

## 📎 Apéndice (evidencias)

**Capturas de ejecución / Actions**
- [ ] Captura del log de ejecución mostrando la detección de archivos nuevos y el batch_id.  
- [ ] Screenshot del paso “build Quartz” o pipeline CI que ejecuta el ETL.  

**Fragmentos de log con errores resueltos**
```
2025-11-09 03:10:15 [INFO] Ingesta: presupuesto.csv → batch_id=5d9f...
2025-11-09 03:10:16 [WARN] 2 filas a quarantine (importe_invalido)
2025-11-09 03:10:18 [INFO] Bronze → Silver completado.
2025-11-09 03:10:19 [INFO] KPI generado: kpi_ejecucion.parquet (38 filas)
```

**Evidencias complementarias**
- [ ] Archivos Parquet de cada capa (`bronze/`, `silver/`, `gold/`)
- [ ] Reporte generado: `output/reporte.md`
- [ ] Captura de la vista `vw_kpi_area` desde SQLite

---

### ✍️ Nota final
El flujo ETL demostró ser reproducible, auditable y extensible. Las próximas iteraciones deben centrarse en la **automatización y observabilidad**, manteniendo la simplicidad lograda en esta versión.
