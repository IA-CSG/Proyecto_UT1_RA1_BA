\newpage
# Plantilla de reporte (resumen ejecutivo) <Br> (40-reporte-plantilla.md)

**Titular:**  
Ejecución presupuestaria del periodo — Ej.: *El gasto total alcanza el 92% del presupuesto (+5 pp vs mes previo), impulsado por el área de Operaciones. Revisar partidas con sobre-ejecución >100%.*

---

## 1. Métricas clave

| Indicador | Valor | Variación | Comentario |
|------------|--------|------------|-------------|
| **Presupuesto total** | ___ € | — | — |
| **Gasto acumulado** | ___ € | — | — |
| **Ejecución global (KPI)** | ___ % | (↑/↓ vs periodo anterior) | — |
| **Áreas sobre-ejecutadas (>100%)** | ___ | — | Revisión prioritaria |
| **Áreas sub-ejecutadas (<80%)** | ___ | — | Potencial de re-asignación |

---

## 2. Contribución por área

| Área | Presupuesto (€) | Gasto (€) | KPI (%) | Estado |
|------|------------------|-----------|---------|--------|
| Finanzas | — | — | — | — |
| Operaciones | — | — | — | — |
| Comercial | — | — | — | — |
| RRHH | — | — | — | — |
| **Total** | — | — | — | — |

> Áreas en **verde**: ejecución dentro del rango (90–100%)  
> Áreas en **rojo**: sobre-ejecución (>100%) o sub-ejecución (<80%)

---

## 3. Tendencia mensual

**Ejemplo de evolución (últimos 6 meses):**

| Mes | Gasto mensual (€) | Variación % | Comentario |
|-----|--------------------|--------------|-------------|
| Jul 2025 | — | — | — |
| Ago 2025 | — | — | — |
| Sep 2025 | — | — | — |
| Oct 2025 | — | — | — |
| Nov 2025 | — | — | Pico por cierre de proyectos |
| Dic 2025 | — | — | Previsto cierre de año |

> **Señalar picos o valles** en el gasto mensual e indicar causas conocidas (campañas, mantenimientos, adquisiciones, etc.).

---

## 4. Calidad de datos

| Capa | Filas procesadas | Validez |
|------|------------------|----------|
| **Bronze (raw)** | ___ | — |
| **Silver (clean)** | ___ | — |
| **Quarantine** | ___ | — |

**Motivos principales de quarantine:**
- Fechas inválidas o fuera de rango  
- Importes negativos o nulos  
- Partidas no presentes en presupuesto  
- Áreas no reconocidas  

> % de cuarentena aceptable < 5%. Si supera el 10%, revisar la fuente.

---

## 5. Próximos pasos

- **Acción 1:** Revisar partidas con ejecución >110% en áreas críticas.
- **Acción 2:** Validar si los gastos fuera de dominio corresponden a nuevas partidas no presupuestadas.
- **Acción 3:** Analizar tendencia mensual y ajustar presupuestos para diciembre.
- **Acción 4:** Automatizar alertas de sobre-ejecución semanal.

---

## 6. Notas
- Todos los valores expresados en **EUR**.
- Importes sin IVA, periodificados según fecha de gasto.
- KPI principal: `kpi_ejecucion = gasto_acumulado / presupuesto`.
