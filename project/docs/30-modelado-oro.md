# Modelo de negocio (capa oro)

## Objetivo
Poder contestar a preguntas como:
- ¿cuánto se ha gastado por área y partida?
- ¿cuánto estaba presupuestado?
- ¿qué porcentaje de ejecución tiene cada área?
- ¿cómo evoluciona el gasto mes a mes?

---

## Tablas oro

### 1. `kpi_ejecucion` (fuente de oro)
- **Granularidad:** área × partida.
- **Origen:** join entre presupuesto limpio (`presupuesto_clean`) y gasto agregado válido (`gastos_clean`).
- **Campos principales:**
  - `area`
  - `partida`
  - `presupuesto` (DECIMAL(18,2))
  - `gasto_acumulado` (DECIMAL(18,2))
  - `kpi_ejecucion` = `gasto_acumulado / presupuesto`
  - `area_normalizada`, `partida_normalizada`
- **Uso:** reportes de ejecución por área y por partida.

### 2. `tendencia_mensual` (tabla/vista de agregación)
- **Granularidad:** mes × área.
- **Origen:** agregación de `gastos_clean` por `year_month` y `area`.
- **Campos:**
  - `year_month` (YYYY-MM)
  - `area`
  - `gasto_mensual`
- **Uso:** seguir la evolución del gasto en el tiempo.

### 3. Vista `vw_kpi_area` (en SQLite)
- **Granularidad:** área.
- **Origen:** agregación sobre `kpi_ejecucion`.
- **Campos:**
  - `area`
  - `gasto_total`
  - `presupuesto_total`
  - `kpi_ejecucion_area` (= gasto_total / presupuesto_total)
- **Uso:** ranking rápido de áreas más/menos ejecutadas.

---

## Métricas (KPI)

1. **Gasto acumulado**
   ```text
   gasto_acumulado = SUM(importe) sobre gastos_clean agrupado por (area, partida)
   ```

2. **Presupuesto**
   ```text
   presupuesto = valor declarado en presupuesto_clean para (area, partida)
   ```

3. **KPI de ejecución**
   ```text
   kpi_ejecucion = gasto_acumulado / presupuesto
   ```
   - Si `presupuesto = 0` → KPI = NULL.
   - Interpretación:
     - `< 1` → por debajo del presupuesto
     - `= 1` → ejecutado al 100%
     - `> 1` → sobre-ejecución

4. **KPI de ejecución por área** (vista)
   ```text
   kpi_ejecucion_area = SUM(gasto_acumulado) / SUM(presupuesto) por área
   ```

5. **Tendencia de gasto**
   ```text
   gasto_mensual = SUM(importe) por (year_month, area)
   ```

---

## Supuestos

- **Moneda:** importes en una única moneda (implícita, EUR).
- **Impuestos:** los importes se consideran **sin IVA** o ya normalizados (lo documenta el reporte).
- **Dedupe:** antes de llegar a oro se aplica la política **“último gana por `_ingest_ts`”** tanto en presupuesto como en gastos.
- **Catálogo de partidas/áreas:** la referencia válida es la que viene en `presupuesto_clean`; los gastos con partidas/áreas fuera de ese dominio se van a **quarantine**.
- **Trazabilidad:** se conservan `_ingest_ts`, `_source_file`, `_batch_id` desde bronze hasta oro (en oro como `last_ingest_ts` y `source_files`).

---

## Consultas base (SQL conceptual)

### 1. Ejecución por área y partida
```sql
SELECT
    area,
    partida,
    presupuesto,
    gasto_acumulado,
    kpi_ejecucion
FROM kpi_ejecucion
ORDER BY area, partida;
```

### 2. Ejecución agregada por área
*(equivalente a la vista `vw_kpi_area` que creas en SQLite)*

```sql
SELECT
    area,
    SUM(gasto_acumulado) AS gasto_total,
    SUM(presupuesto) AS presupuesto_total,
    CASE
        WHEN SUM(presupuesto) = 0 THEN NULL
        ELSE ROUND(SUM(gasto_acumulado) * 1.0 / SUM(presupuesto), 4)
    END AS kpi_ejecucion_area
FROM kpi_ejecucion
GROUP BY area
ORDER BY kpi_ejecucion_area DESC;
```

### 3. Tendencia mensual de gasto
```sql
SELECT
    year_month,
    area,
    gasto_mensual
FROM tendencia_mensual
ORDER BY year_month, area;
```

### 4. Áreas sobre-ejecutadas (>100%)
```sql
SELECT
    area,
    presupuesto,
    gasto_acumulado,
    kpi_ejecucion
FROM kpi_ejecucion
WHERE kpi_ejecucion > 1
ORDER BY kpi_ejecucion DESC;
```

---

## Notas

- Lo que en el ejemplo era `clean_ventas` aquí es **tu** `kpi_ejecucion` + el detalle de `gastos_clean`/`presupuesto_clean` en silver.
- Lo que en el ejemplo era `ventas_diarias` aquí es **tu** `tendencia_mensual`.
- Las métricas están centradas en **ejecución presupuestaria**, no en ventas.
