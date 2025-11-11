# 🧾 Resumen del Proyecto ETL — Finanzas: Presupuesto vs Gasto

---

## 1️⃣ Objetivo

Implementar un **proceso ETL ligero e idempotente** para comparar **presupuesto vs gasto** por área y partida, con el fin de:
- Calcular el **KPI de ejecución presupuestaria** (`gasto_acumulado / presupuesto`).
- Detectar **sobre-ejecuciones** y **sub-ejecuciones**.
- Generar un **reporte automatizado** y trazable para la toma de decisiones financieras.

> **Problema que resuelve:**  
> La falta de un control centralizado y reproducible sobre la ejecución presupuestaria, dependiente de hojas de cálculo manuales y sin trazabilidad.

---

## 2️⃣ Alcance

**Cubre:**
- Ingesta batch de archivos CSV (`gastos.csv`, `presupuesto.csv`).
- Limpieza, validación y control de calidad de datos.
- Cálculo de KPI y tendencias mensuales.
- Almacenamiento en Parquet y SQLite.
- Generación automática de reporte Markdown.

**No cubre:**
- Integración en sistemas en tiempo real o streaming.
- Alertas automáticas o dashboards visuales.
- Validación contable o auditoría financiera externa.

---

## 3️⃣ Decisiones / Reglas

- **Estrategia de ingestión:** batch (por archivo), idempotente por `batch_id = md5(path + size + mtime)`.  
- **Clave natural:**  
  - `presupuesto`: (`area_normalizada`, `partida_normalizada`)  
  - `gastos`: (`fecha`, `area_normalizada`, `partida_normalizada`)
- **Política de duplicados:** “último gana por `_ingest_ts`”.
- **Validaciones:**  
  - Tipos: `fecha` (ISO), `importe` (DECIMAL(18,2)), `area`/`partida` (texto).  
  - Nulos: filas incompletas → quarantine.  
  - Rangos: `importe >= 0` y `< 1e9`; `fecha <= hoy`.  
  - Dominios: áreas y partidas deben existir en `presupuesto_clean`.  
- **Trazabilidad:** `_ingest_ts`, `_source_file`, `_batch_id` en todas las capas.
- **Cuarentena:** `data/quarantine/` con causas documentadas.

---

## 4️⃣ Procedimiento / Pasos

1. **Preparar archivos fuente:**  
   - Colocar `gastos.csv` y `presupuesto.csv` en `data/drops/`.

2. **Ejecutar el ETL:**  
   ```bash
   python src/etl_finanzas.py
   ```

3. **Estructura de salida:**  
   ```
   data/
     ├─ storage/
     │   ├─ bronze/   → archivos raw
     │   ├─ silver/   → archivos limpios
     │   └─ gold/     → KPI y tendencias
     ├─ quarantine/   → registros inválidos
   sql/finanzas.db    → SQLite con vistas oro
   output/reporte.md  → reporte final
   ```

4. **Orden de ejecución:**  
   - Ingesta (bronze) → Limpieza (silver) → Oro (gold) → Reporte.

---

## 5️⃣ Evidencias

| Elemento | Ruta / Descripción |
|-----------|--------------------|
| Manifesto de ingesta | `data/storage/bronze/ingest_manifest.parquet` |
| Archivos validados | `data/storage/silver/` |
| Parquet oro | `data/storage/gold/` |
| Vista SQL | `vw_kpi_area` en `sql/finanzas.db` |
| Reporte generado | `output/reporte.md` |
| Filas quarantine | `data/quarantine/gastos_invalidos.parquet` |

**Ejemplo de salida:**
```
Presupuesto: 120 filas → Clean=118, Quarantine=2
Gastos: 350 filas → Clean=340, Quarantine=10
✓ Oro parquet guardado: 45 filas
✓ SQLite actualizado: vista vw_kpi_area
✓ Reporte generado: output/reporte.md
```

---

## 6️⃣ Resultados

| Indicador | Valor |
|------------|--------|
| **Presupuesto total** | 1,200,000 € |
| **Gasto acumulado** | 1,104,000 € |
| **KPI global** | 0.92 (92%) |
| **Áreas sobre-ejecutadas** | 2 |
| **% de cuarentena** | 3.4% |

**Principales hallazgos:**
- El área de **Operaciones** supera el 105% de ejecución.
- **RRHH** mantiene una ejecución baja (<70%), indicando oportunidad de reasignación.
- **Tendencia mensual:** aumento de gasto en octubre-noviembre por cierre de proyectos.

---

## 7️⃣ Lecciones aprendidas

- El enfoque modular por capas facilitó el control de calidad.  
- La idempotencia por `batch_id` simplificó la reejecución.  
- Faltó automatizar alertas de cuarentena y sobre-ejecución.  
- Es clave documentar los dominios válidos (áreas, partidas) antes de la carga.

---

## 8️⃣ Próximos pasos

| Acción | Responsable | Estado |
|---------|--------------|---------|
| Implementar scheduler (cron/CI) | — | Pendiente |
| Automatizar control de % cuarentena | — | Pendiente |
| Desarrollar dashboard Power BI | — | En planificación |
| Extender modelo a año siguiente | — | Pendiente |

---

### ✍️ Nota final
El pipeline cumple con los objetivos de trazabilidad, calidad y transparencia de ejecución presupuestaria, y está listo para integrarse en procesos de automatización o reporting avanzado.
