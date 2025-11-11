# Informe de Ejecución Presupuestaria
_Generado: 2025-11-10 22:19_
## 1. Contexto
- Fuente: `gastos.csv` y `presupuesto.csv`.
- Actualización: batch (ETL ligero) previo a capa oro.
- Objetivo: medir la ejecución del presupuesto por área y partida.
## 2. Definiciones de KPI
- **gasto_acumulado**: suma de los importes registrados en `gastos.csv` para un área/partida.
- **presupuesto**: importe planificado en `presupuesto.csv`.
- **kpi_ejecucion** = gasto_acumulado / presupuesto.
- **Interpretación**: valores > 1 implican sobre-ejecución.
## 3. Ejecución por área
| Área | Presupuesto | Gasto acumulado | KPI ejecución |
|------|-------------|-----------------|---------------|
| Administracion | 1141600.00 | 4292035.29 | 376.0% |
| Calidad | 1089333.00 | 4121144.24 | 378.3% |
| Contabilidad | 980016.00 | 3961119.65 | 404.2% |
| Direccion | 965339.00 | 3726630.77 | 386.0% |
| I+D | 773811.00 | 2794115.05 | 361.1% |
| IT | 1185108.00 | 4680772.40 | 395.0% |
| Marketing | 1139605.00 | 4678507.67 | 410.5% |
| Operaciones | 1118341.00 | 4175823.16 | 373.4% |
| RRHH | 1401592.00 | 5580298.46 | 398.1% |
| Ventas | 969840.00 | 3770895.99 | 388.8% |

## 4. Ejecución por área y partida
| Área | Partida | Presupuesto | Gasto acumulado | KPI |
|------|---------|-------------|-----------------|-----|
| Administracion | Alquileres | 190389.00 | 790327.24 | 415.1% |
| Administracion | Formacion | 83796.00 | 300480.59 | 358.6% |
| Administracion | Hardware | 194325.00 | 717614.45 | 369.3% |
| Administracion | Mantenimiento | 73167.00 | 279985.61 | 382.7% |
| Administracion | Personal | 114984.00 | 443057.44 | 385.3% |
| Administracion | Publicidad | 148893.00 | 508339.88 | 341.4% |
| Administracion | Seguros | 121235.00 | 468645.25 | 386.6% |
| Administracion | Software | 28929.00 | 119733.77 | 413.9% |
| Administracion | Suministros | 76467.00 | 302075.81 | 395.0% |
| Administracion | Viajes | 109415.00 | 361775.25 | 330.7% |
| Calidad | Alquileres | 36674.00 | 158719.67 | 432.8% |
| Calidad | Formacion | 176658.00 | 684974.26 | 387.7% |
| Calidad | Hardware | 119655.00 | 461931.44 | 386.1% |
| Calidad | Mantenimiento | 92628.00 | 327165.31 | 353.2% |
| Calidad | Personal | 192155.00 | 705987.63 | 367.4% |
| Calidad | Publicidad | 155503.00 | 520232.97 | 334.6% |
| Calidad | Seguros | 15503.00 | 74759.10 | 482.2% |
| Calidad | Software | 48200.00 | 197831.80 | 410.4% |
| Calidad | Suministros | 134872.00 | 488643.64 | 362.3% |
| Calidad | Viajes | 117485.00 | 500898.42 | 426.3% |
| Contabilidad | Alquileres | 28169.00 | 128897.76 | 457.6% |
| Contabilidad | Formacion | 40011.00 | 151037.64 | 377.5% |
| Contabilidad | Hardware | 91477.00 | 367242.47 | 401.5% |
| Contabilidad | Mantenimiento | 166591.00 | 597188.38 | 358.5% |
| Contabilidad | Personal | 159688.00 | 623917.97 | 390.7% |
| Contabilidad | Publicidad | 36676.00 | 169865.24 | 463.1% |
| Contabilidad | Seguros | 182840.00 | 737737.33 | 403.5% |
| Contabilidad | Software | 172122.00 | 734256.89 | 426.6% |
| Contabilidad | Suministros | 26882.00 | 96499.90 | 359.0% |
| Contabilidad | Viajes | 75560.00 | 354476.07 | 469.1% |
| Direccion | Alquileres | 24958.00 | 83595.22 | 334.9% |
| Direccion | Formacion | 166121.00 | 613585.41 | 369.4% |
| Direccion | Hardware | 139592.00 | 586855.89 | 420.4% |
| Direccion | Mantenimiento | 173872.00 | 589881.05 | 339.3% |
| Direccion | Personal | 12239.00 | 55013.01 | 449.5% |
| Direccion | Publicidad | 10369.00 | 48595.15 | 468.7% |
| Direccion | Seguros | 11973.00 | 45303.94 | 378.4% |
| Direccion | Software | 165347.00 | 585018.43 | 353.8% |
| Direccion | Suministros | 140070.00 | 659712.16 | 471.0% |
| Direccion | Viajes | 120798.00 | 459070.51 | 380.0% |
| I+D | Alquileres | 143587.00 | 484773.70 | 337.6% |
| I+D | Formacion | 140960.00 | 508318.66 | 360.6% |
| I+D | Hardware | 15816.00 | 58592.51 | 370.5% |
| I+D | Mantenimiento | 77709.00 | 347950.85 | 447.8% |
| I+D | Personal | 128117.00 | 444479.02 | 346.9% |
| I+D | Publicidad | 23389.00 | 101061.22 | 432.1% |
| I+D | Seguros | 52183.00 | 187792.71 | 359.9% |
| I+D | Software | 71903.00 | 277685.37 | 386.2% |
| I+D | Suministros | 15345.00 | 63313.10 | 412.6% |
| I+D | Viajes | 104802.00 | 320147.91 | 305.5% |
| IT | Alquileres | 109722.00 | 398635.07 | 363.3% |
| IT | Formacion | 77193.00 | 335403.52 | 434.5% |
| IT | Hardware | 186348.00 | 698187.13 | 374.7% |
| IT | Mantenimiento | 146269.00 | 560879.92 | 383.5% |
| IT | Personal | 69065.00 | 286118.86 | 414.3% |
| IT | Publicidad | 48384.00 | 175795.10 | 363.3% |
| IT | Seguros | 147866.00 | 608559.25 | 411.6% |
| IT | Software | 130775.00 | 565615.80 | 432.5% |
| IT | Suministros | 108299.00 | 488618.00 | 451.2% |
| IT | Viajes | 161187.00 | 562959.75 | 349.3% |
| Marketing | Alquileres | 119935.00 | 602407.18 | 502.3% |
| Marketing | Formacion | 100058.00 | 402976.21 | 402.7% |
| Marketing | Hardware | 103670.00 | 468162.87 | 451.6% |
| Marketing | Mantenimiento | 169142.00 | 556484.46 | 329.0% |
| Marketing | Personal | 49986.00 | 217116.25 | 434.3% |
| Marketing | Publicidad | 72148.00 | 298187.58 | 413.3% |
| Marketing | Seguros | 110416.00 | 450997.81 | 408.5% |
| Marketing | Software | 176392.00 | 729425.02 | 413.5% |
| Marketing | Suministros | 174509.00 | 735162.45 | 421.3% |
| Marketing | Viajes | 63349.00 | 217587.84 | 343.5% |
| Operaciones | Alquileres | 125764.00 | 408541.61 | 324.9% |
| Operaciones | Formacion | 56116.00 | 175178.56 | 312.2% |
| Operaciones | Hardware | 134861.00 | 539256.01 | 399.9% |
| Operaciones | Mantenimiento | 150200.00 | 664450.26 | 442.4% |
| Operaciones | Personal | 54144.00 | 177976.39 | 328.7% |
| Operaciones | Publicidad | 105987.00 | 498437.05 | 470.3% |
| Operaciones | Seguros | 173168.00 | 602595.54 | 348.0% |
| Operaciones | Software | 63933.00 | 253938.49 | 397.2% |
| Operaciones | Suministros | 72796.00 | 286438.35 | 393.5% |
| Operaciones | Viajes | 181372.00 | 569010.90 | 313.7% |
| RRHH | Alquileres | 85812.00 | 344045.09 | 400.9% |
| RRHH | Formacion | 196861.00 | 635074.14 | 322.6% |
| RRHH | Hardware | 177617.00 | 715477.22 | 402.8% |
| RRHH | Mantenimiento | 155091.00 | 663356.00 | 427.7% |
| RRHH | Personal | 171982.00 | 648870.48 | 377.3% |
| RRHH | Publicidad | 113842.00 | 472692.14 | 415.2% |
| RRHH | Seguros | 13095.00 | 52599.63 | 401.7% |
| RRHH | Software | 197352.00 | 897658.81 | 454.8% |
| RRHH | Suministros | 181592.00 | 662258.91 | 364.7% |
| RRHH | Viajes | 108348.00 | 488266.04 | 450.6% |
| Ventas | Alquileres | 110062.00 | 494979.94 | 449.7% |
| Ventas | Formacion | 107954.00 | 408189.55 | 378.1% |
| Ventas | Hardware | 57331.00 | 233128.95 | 406.6% |
| Ventas | Mantenimiento | 148772.00 | 538634.21 | 362.0% |
| Ventas | Personal | 186605.00 | 709633.27 | 380.3% |
| Ventas | Publicidad | 194243.00 | 721121.17 | 371.2% |
| Ventas | Seguros | 61936.00 | 226313.79 | 365.4% |
| Ventas | Software | 17171.00 | 86850.01 | 505.8% |
| Ventas | Suministros | 63113.00 | 265485.30 | 420.7% |
| Ventas | Viajes | 22653.00 | 86559.80 | 382.1% |

## 5. Tendencia mensual de gasto (por área)
| Mes | Área | Gasto mensual |
|-----|------|----------------|
| 2025-01 | Administracion | 419177.61 |
| 2025-01 | Calidad | 373027.53 |
| 2025-01 | Contabilidad | 398675.46 |
| 2025-01 | Direccion | 298418.99 |
| 2025-01 | I+D | 276489.40 |
| 2025-01 | IT | 567548.25 |
| 2025-01 | Marketing | 442005.82 |
| 2025-01 | Operaciones | 430816.49 |
| 2025-01 | RRHH | 557815.24 |
| 2025-01 | Ventas | 352833.20 |
| 2025-02 | Administracion | 366816.03 |
| 2025-02 | Calidad | 369367.31 |
| 2025-02 | Contabilidad | 301953.11 |
| 2025-02 | Direccion | 308090.43 |
| 2025-02 | I+D | 329663.30 |
| 2025-02 | IT | 424294.31 |
| 2025-02 | Marketing | 493606.16 |
| 2025-02 | Operaciones | 371724.68 |
| 2025-02 | RRHH | 465723.69 |
| 2025-02 | Ventas | 320798.05 |
| 2025-03 | Administracion | 484889.39 |
| 2025-03 | Calidad | 441066.28 |
| 2025-03 | Contabilidad | 426669.96 |
| 2025-03 | Direccion | 421142.32 |
| 2025-03 | I+D | 259415.05 |
| 2025-03 | IT | 450034.09 |
| 2025-03 | Marketing | 443452.11 |
| 2025-03 | Operaciones | 405881.88 |
| 2025-03 | RRHH | 641391.36 |
| 2025-03 | Ventas | 443676.59 |
| 2025-04 | Administracion | 442365.54 |
| 2025-04 | Calidad | 388885.59 |
| 2025-04 | Contabilidad | 506430.03 |
| 2025-04 | Direccion | 438945.12 |
| 2025-04 | I+D | 256391.06 |
| 2025-04 | IT | 453721.01 |
| 2025-04 | Marketing | 421976.90 |
| 2025-04 | Operaciones | 399844.55 |
| 2025-04 | RRHH | 551117.36 |
| 2025-04 | Ventas | 419363.34 |
| 2025-05 | Administracion | 480903.15 |
| 2025-05 | Calidad | 426229.08 |
| 2025-05 | Contabilidad | 480618.47 |
| 2025-05 | Direccion | 290157.51 |
| 2025-05 | I+D | 270705.84 |
| 2025-05 | IT | 498015.99 |
| 2025-05 | Marketing | 474353.89 |
| 2025-05 | Operaciones | 380556.60 |
| 2025-05 | RRHH | 414395.23 |
| 2025-05 | Ventas | 307472.69 |
| 2025-06 | Administracion | 405738.24 |
| 2025-06 | Calidad | 488181.75 |
| 2025-06 | Contabilidad | 357568.30 |
| 2025-06 | Direccion | 293890.09 |
| 2025-06 | I+D | 253702.93 |
| 2025-06 | IT | 355231.35 |
| 2025-06 | Marketing | 504617.05 |
| 2025-06 | Operaciones | 446717.92 |
| 2025-06 | RRHH | 551536.41 |
| 2025-06 | Ventas | 327694.91 |
| 2025-07 | Administracion | 349925.13 |
| 2025-07 | Calidad | 339106.46 |
| 2025-07 | Contabilidad | 329922.97 |
| 2025-07 | Direccion | 341532.63 |
| 2025-07 | I+D | 281545.37 |
| 2025-07 | IT | 457111.91 |
| 2025-07 | Marketing | 431237.67 |
| 2025-07 | Operaciones | 380937.06 |
| 2025-07 | RRHH | 671243.34 |
| 2025-07 | Ventas | 348213.16 |
| 2025-08 | Administracion | 477322.62 |
| 2025-08 | Calidad | 411113.36 |
| 2025-08 | Contabilidad | 343150.27 |
| 2025-08 | Direccion | 430824.18 |
| 2025-08 | I+D | 289359.79 |
| 2025-08 | IT | 470356.15 |
| 2025-08 | Marketing | 434615.46 |
| 2025-08 | Operaciones | 371713.95 |
| 2025-08 | RRHH | 466498.73 |
| 2025-08 | Ventas | 347874.44 |
| 2025-09 | Administracion | 362174.13 |
| 2025-09 | Calidad | 383127.69 |
| 2025-09 | Contabilidad | 371733.44 |
| 2025-09 | Direccion | 333548.67 |
| 2025-09 | I+D | 237762.17 |
| 2025-09 | IT | 415818.98 |
| 2025-09 | Marketing | 400977.74 |
| 2025-09 | Operaciones | 391957.20 |
| 2025-09 | RRHH | 494691.54 |
| 2025-09 | Ventas | 471859.19 |
| 2025-10 | Administracion | 388860.37 |
| 2025-10 | Calidad | 339113.07 |
| 2025-10 | Contabilidad | 349931.11 |
| 2025-10 | Direccion | 455739.56 |
| 2025-10 | I+D | 280974.73 |
| 2025-10 | IT | 450912.74 |
| 2025-10 | Marketing | 503903.22 |
| 2025-10 | Operaciones | 411388.70 |
| 2025-10 | RRHH | 568045.43 |
| 2025-10 | Ventas | 330451.01 |
| 2025-11 | Administracion | 113863.08 |
| 2025-11 | Calidad | 161926.12 |
| 2025-11 | Contabilidad | 94466.53 |
| 2025-11 | Direccion | 114341.27 |
| 2025-11 | I+D | 58105.41 |
| 2025-11 | IT | 137727.62 |
| 2025-11 | Marketing | 127761.65 |
| 2025-11 | Operaciones | 184284.13 |
| 2025-11 | RRHH | 197840.13 |
| 2025-11 | Ventas | 100659.41 |

## 6. Filas en cuarentena (gastos descartados)
| fecha | area | partida | importe | causa |
|-------|------|---------|---------|--------|
| 2025-02-07 | Contabilidad | Mantenimiento | 10000000.00 | importe_excesivo |
|  | Ventas | Suministros | 3182.95 | fecha_invalida |
| 2025-03-09 | nan | Software | 2982.77 | area_no_valida |
| 2025-07-23 | Contabilidad | nan | 1855.03 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-18 | RRHH | nan | 11140.71 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-11 | XXX-AREA MALA | Publicidad | 799.91 | area_no_valida |
|  | RRHH | Suministros | 6519.16 | fecha_invalida |
| 2025-02-09 | I+D | Software | 10000000.00 | importe_excesivo |
|  | Ventas | Software | 1182.29 | fecha_invalida |
| 2025-08-25 | RRHH | Viajes | -500.00 | importe_invalido |
| 2025-04-15 | nan | Personal | 15024.42 | area_no_valida |
| 2025-05-11 | Ventas | nan | 6329.41 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-23 | nan | Viajes | 3861.14 | area_no_valida |
| 2025-04-04 | Calidad | XXX-PARTIDA MALA | 560.15 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-09 | Administracion | Seguros | -500.00 | importe_invalido |
| 2025-05-30 | RRHH | XXX-PARTIDA MALA | 5505.50 | partida_no_valida; partida_no_en_presupuesto |
|  | IT | Viajes | 848.63 | fecha_invalida |
| 2025-02-26 | XXX-AREA MALA | Personal | 14874.90 | area_no_valida |
|  | Calidad | Formacion | 11959.86 | fecha_invalida |
|  | Marketing | Suministros | 14507.01 | fecha_invalida |
| 2025-06-03 | nan | Alquileres | 5733.13 | area_no_valida |
| 2025-11-05 | nan | Personal | 815.06 | area_no_valida |
| 2025-04-24 | Administracion | XXX-PARTIDA MALA | 10248.87 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-15 | Administracion | XXX-PARTIDA MALA | 4809.40 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-19 | Marketing | Hardware | 10000000.00 | importe_excesivo |
| 2025-05-10 | nan | Formacion | 1249.24 | area_no_valida |
| 2025-04-11 | nan | Seguros | 877.11 | area_no_valida |
| 2025-04-25 | nan | Software | 6310.50 | area_no_valida |
| 2025-04-13 | Marketing | nan | 1769.04 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-30 | Administracion | Software | -500.00 | importe_invalido |
| 2025-05-22 | Operaciones | Seguros | -500.00 | importe_invalido |
|  | Contabilidad | Mantenimiento | 9859.02 | fecha_invalida |
| 2025-10-14 | nan | Suministros | 143.35 | area_no_valida |
|  | IT | Publicidad | 3720.35 | fecha_invalida |
| 2025-08-02 | Administracion | Viajes | 10000000.00 | importe_excesivo |
| 2025-02-13 | Administracion | Publicidad | -500.00 | importe_invalido |
| 2025-04-05 | Marketing | Seguros | 10000000.00 | importe_excesivo |
| 2025-09-01 | nan | Seguros | 1516.94 | area_no_valida |
| 2025-02-18 | Contabilidad | Alquileres | -500.00 | importe_invalido |
|  | IT | Personal | 3918.58 | fecha_invalida |
| 2025-08-29 | XXX-AREA MALA | Formacion | 4950.06 | area_no_valida |
| 2025-04-15 | nan | Hardware | 1134.09 | area_no_valida |
| 2025-05-17 | XXX-AREA MALA | Publicidad | 2641.44 | area_no_valida |
| 2025-01-06 | XXX-AREA MALA | Suministros | 5115.32 | area_no_valida |
| 2025-10-31 | Calidad | nan | 8887.56 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-20 | Contabilidad | nan | 13804.32 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-23 | Contabilidad | Software | -500.00 | importe_invalido |
| 2025-01-02 | nan | Hardware | 13294.86 | area_no_valida |
| 2025-10-23 | nan | Publicidad | 1885.27 | area_no_valida |
| 2025-09-09 | Contabilidad | nan | 2262.81 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-23 | Calidad | Hardware | 10000000.00 | importe_excesivo |
| 2025-08-23 | nan | Personal | 1900.85 | area_no_valida |
| 2025-09-24 | Direccion | nan | 11622.35 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-01 | IT | nan | 3071.94 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-09 | Ventas | XXX-PARTIDA MALA | 504.84 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-04 | Administracion | Software | -500.00 | importe_invalido |
|  | Marketing | Hardware | 8665.86 | fecha_invalida |
|  | Direccion | Alquileres | 1769.69 | fecha_invalida |
| 2025-04-29 | RRHH | nan | 122.78 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-02 | RRHH | XXX-PARTIDA MALA | 19539.66 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-14 | Administracion | Viajes | 10000000.00 | importe_excesivo |
| 2025-01-21 | nan | Seguros | 711.10 | area_no_valida |
| 2025-06-19 | Ventas | Seguros | 10000000.00 | importe_excesivo |
| 2025-02-28 | Marketing | Personal | -500.00 | importe_invalido |
| 2025-01-06 | Ventas | Formacion | 10000000.00 | importe_excesivo |
| 2025-09-11 | Administracion | XXX-PARTIDA MALA | 3416.06 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-13 | Direccion | nan | 4694.71 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-09 | IT | Hardware | 10000000.00 | importe_excesivo |
| 2025-04-30 | I+D | XXX-PARTIDA MALA | 2060.71 | partida_no_valida; partida_no_en_presupuesto |
|  | I+D | Publicidad | 1815.01 | fecha_invalida |
| 2025-06-10 | Contabilidad | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-02-09 | XXX-AREA MALA | Seguros | 1248.87 | area_no_valida |
|  | Operaciones | Alquileres | 4895.87 | fecha_invalida |
| 2025-09-03 | nan | Publicidad | 10040.55 | area_no_valida |
| 2025-11-08 | nan | Alquileres | 4678.01 | area_no_valida |
| 2025-06-04 | Marketing | nan | 7726.81 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-19 | IT | nan | 6079.14 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-08 | Administracion | XXX-PARTIDA MALA | 1407.12 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-16 | nan | Seguros | 481.91 | area_no_valida |
| 2025-07-30 | Contabilidad | Publicidad | -500.00 | importe_invalido |
| 2025-05-05 | nan | Seguros | 1693.61 | area_no_valida |
| 2025-09-12 | Administracion | Publicidad | -500.00 | importe_invalido |
| 2025-09-01 | Operaciones | Publicidad | 10000000.00 | importe_excesivo |
| 2025-11-03 | nan | Seguros | 475.26 | area_no_valida |
| 2025-04-10 | nan | Software | 5127.62 | area_no_valida |
| 2025-08-17 | nan | Suministros | 5473.62 | area_no_valida |
| 2025-01-14 | nan | Alquileres | 9266.05 | area_no_valida |
|  | IT | Alquileres | 6621.19 | fecha_invalida |
| 2025-07-07 | Marketing | Suministros | -500.00 | importe_invalido |
| 2025-04-24 | Calidad | Alquileres | -500.00 | importe_invalido |
| 2025-11-01 | XXX-AREA MALA | Formacion | 6358.15 | area_no_valida |
| 2025-01-13 | Contabilidad | Alquileres | -500.00 | importe_invalido |
| 2025-08-17 | Direccion | XXX-PARTIDA MALA | 547.88 | partida_no_valida; partida_no_en_presupuesto |
|  | RRHH | Suministros | 6214.64 | fecha_invalida |
| 2025-11-05 | I+D | nan | 5225.06 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-09 | XXX-AREA MALA | Formacion | 5248.44 | area_no_valida |
| 2025-03-02 | Calidad | Viajes | -500.00 | importe_invalido |
| 2025-01-06 | XXX-AREA MALA | Publicidad | 2278.37 | area_no_valida |
| 2025-08-09 | IT | nan | 5115.74 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-15 | Calidad | XXX-PARTIDA MALA | 1164.95 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-11 | Operaciones | Suministros | 10000000.00 | importe_excesivo |
| 2025-08-24 | Operaciones | Suministros | -500.00 | importe_invalido |
| 2025-05-13 | nan | Seguros | 6861.70 | area_no_valida |
| 2025-10-06 | Ventas | Publicidad | 10000000.00 | importe_excesivo |
| 2025-08-20 | IT | XXX-PARTIDA MALA | 2501.82 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-12 | Direccion | Formacion | -500.00 | importe_invalido |
| 2025-06-04 | I+D | Hardware | 10000000.00 | importe_excesivo |
|  | IT | Viajes | 5541.94 | fecha_invalida |
| 2025-06-23 | Administracion | Publicidad | 10000000.00 | importe_excesivo |
| 2025-06-04 | Administracion | Suministros | 10000000.00 | importe_excesivo |
| 2025-02-14 | Calidad | nan | 1907.09 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-10 | XXX-AREA MALA | Mantenimiento | 2848.64 | area_no_valida |
| 2025-02-03 | XXX-AREA MALA | Formacion | 7695.38 | area_no_valida |
| 2025-09-02 | Operaciones | XXX-PARTIDA MALA | 4611.07 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-28 | nan | Viajes | 865.38 | area_no_valida |
| 2025-08-29 | Marketing | Viajes | -500.00 | importe_invalido |
| 2025-08-09 | nan | Formacion | 1901.04 | area_no_valida |
| 2025-07-12 | Contabilidad | XXX-PARTIDA MALA | 15582.99 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-12 | IT | Alquileres | 10000000.00 | importe_excesivo |
| 2025-04-10 | Contabilidad | nan | 261.63 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-19 | Ventas | Publicidad | 10000000.00 | importe_excesivo |
| 2025-05-30 | nan | Publicidad | 1204.88 | area_no_valida |
| 2025-08-01 | Ventas | Alquileres | -500.00 | importe_invalido |
| 2025-09-05 | RRHH | Alquileres | 10000000.00 | importe_excesivo |
| 2025-09-28 | XXX-AREA MALA | Seguros | 2868.32 | area_no_valida |
| 2025-02-08 | Contabilidad | nan | 6442.07 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-28 | Operaciones | nan | 1398.34 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-15 | Operaciones | XXX-PARTIDA MALA | 2230.94 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-31 | Operaciones | nan | 521.76 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-01 | Ventas | Alquileres | 10000000.00 | importe_excesivo |
| 2025-09-30 | RRHH | nan | 8225.27 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-20 | XXX-AREA MALA | Seguros | 597.06 | area_no_valida |
| 2025-08-24 | Administracion | Publicidad | 10000000.00 | importe_excesivo |
| 2025-05-23 | nan | Software | 1007.76 | area_no_valida |
| 2025-03-10 | Direccion | nan | 165.76 | partida_no_valida; partida_no_en_presupuesto |
|  | IT | Mantenimiento | 3935.95 | fecha_invalida |
| 2025-04-17 | XXX-AREA MALA | Publicidad | 1164.56 | area_no_valida |
|  | Marketing | Suministros | 4437.06 | fecha_invalida |
| 2025-07-23 | RRHH | XXX-PARTIDA MALA | 18558.58 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-06 | I+D | nan | 1819.94 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-20 | Ventas | XXX-PARTIDA MALA | 4144.23 | partida_no_valida; partida_no_en_presupuesto |
|  | Ventas | Alquileres | 4508.90 | fecha_invalida |
| 2025-02-15 | nan | Publicidad | 5214.83 | area_no_valida |
| 2025-05-07 | XXX-AREA MALA | Suministros | 803.40 | area_no_valida |
| 2025-06-17 | nan | Suministros | 6158.12 | area_no_valida |
| 2025-02-02 | Ventas | Suministros | -500.00 | importe_invalido |
| 2025-04-04 | Operaciones | nan | 3193.36 | partida_no_valida; partida_no_en_presupuesto |
|  | Marketing | Seguros | 7669.72 | fecha_invalida |
| 2025-09-11 | nan | Personal | 4381.97 | area_no_valida |
| 2025-09-04 | XXX-AREA MALA | Personal | 2373.38 | area_no_valida |
| 2025-09-23 | XXX-AREA MALA | Formacion | 10195.74 | area_no_valida |
| 2025-01-20 | Contabilidad | Suministros | 10000000.00 | importe_excesivo |
| 2025-08-13 | I+D | XXX-PARTIDA MALA | 10572.50 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-18 | Contabilidad | nan | 2964.00 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-10 | IT | Formacion | -500.00 | importe_invalido |
|  | I+D | Publicidad | 2253.51 | fecha_invalida |
| 2025-07-04 | XXX-AREA MALA | Software | 13385.65 | area_no_valida |
|  | Contabilidad | Seguros | 2188.30 | fecha_invalida |
| 2025-05-08 | Operaciones | Viajes | -500.00 | importe_invalido |
| 2025-01-26 | IT | Personal | 10000000.00 | importe_excesivo |
| 2025-09-06 | Ventas | Viajes | 10000000.00 | importe_excesivo |
| 2025-04-18 | nan | Alquileres | 2140.79 | area_no_valida |
| 2025-02-17 | nan | Personal | 2230.98 | area_no_valida |
|  | Direccion | Alquileres | 2014.88 | fecha_invalida |
| 2025-02-23 | nan | Software | 8655.52 | area_no_valida |
| 2025-09-05 | XXX-AREA MALA | Personal | 4336.34 | area_no_valida |
| 2025-02-25 | XXX-AREA MALA | Hardware | 9396.97 | area_no_valida |
| 2025-05-25 | IT | Mantenimiento | -500.00 | importe_invalido |
| 2025-03-17 | Calidad | Viajes | -500.00 | importe_invalido |
| 2025-11-03 | XXX-AREA MALA | Formacion | 508.56 | area_no_valida |
|  | I+D | Personal | 12745.53 | fecha_invalida |
| 2025-10-07 | Direccion | Seguros | -500.00 | importe_invalido |
| 2025-09-10 | Direccion | XXX-PARTIDA MALA | 1563.29 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-11 | Direccion | Viajes | 10000000.00 | importe_excesivo |
| 2025-06-30 | Contabilidad | XXX-PARTIDA MALA | 315.22 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-12 | Calidad | XXX-PARTIDA MALA | 12083.76 | partida_no_valida; partida_no_en_presupuesto |
|  | Ventas | Alquileres | 4010.39 | fecha_invalida |
| 2025-07-18 | XXX-AREA MALA | Hardware | 483.71 | area_no_valida |
| 2025-02-28 | XXX-AREA MALA | Mantenimiento | 2352.74 | area_no_valida |
| 2025-05-16 | Contabilidad | nan | 355.75 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-29 | Operaciones | XXX-PARTIDA MALA | 1122.46 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-27 | Administracion | Mantenimiento | 10000000.00 | importe_excesivo |
|  | Direccion | Hardware | 3527.66 | fecha_invalida |
| 2025-06-08 | Direccion | Publicidad | -500.00 | importe_invalido |
| 2025-06-04 | nan | Seguros | 290.88 | area_no_valida |
|  | IT | Hardware | 9254.59 | fecha_invalida |
| 2025-09-21 | IT | nan | 8523.80 | partida_no_valida; partida_no_en_presupuesto |
|  | Calidad | Personal | 13201.32 | fecha_invalida |
| 2025-10-16 | nan | Mantenimiento | 9201.84 | area_no_valida |
| 2025-02-25 | nan | Publicidad | 12264.31 | area_no_valida |
| 2025-06-24 | IT | nan | 613.92 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-17 | Contabilidad | Suministros | 10000000.00 | importe_excesivo |
| 2025-09-12 | I+D | Suministros | 10000000.00 | importe_excesivo |
| 2025-05-17 | nan | Formacion | 13649.16 | area_no_valida |
| 2025-09-05 | nan | Publicidad | 1319.67 | area_no_valida |
|  | Ventas | Software | 954.97 | fecha_invalida |
|  | Calidad | Hardware | 11584.81 | fecha_invalida |
| 2025-06-07 | Calidad | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-03-20 | Calidad | XXX-PARTIDA MALA | 8600.18 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-18 | Marketing | nan | 7288.48 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-24 | nan | Seguros | 4250.22 | area_no_valida |
|  | Contabilidad | Mantenimiento | 2459.72 | fecha_invalida |
| 2025-03-15 | Contabilidad | XXX-PARTIDA MALA | 7825.19 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-30 | Marketing | XXX-PARTIDA MALA | 8385.94 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-14 | Marketing | XXX-PARTIDA MALA | 3290.48 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-06 | Operaciones | Seguros | -500.00 | importe_invalido |
| 2025-07-05 | XXX-AREA MALA | Software | 1927.49 | area_no_valida |
| 2025-02-06 | IT | Seguros | -500.00 | importe_invalido |
| 2025-03-22 | Administracion | XXX-PARTIDA MALA | 1926.45 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-29 | Administracion | XXX-PARTIDA MALA | 5768.76 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-17 | Ventas | XXX-PARTIDA MALA | 6008.27 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-29 | RRHH | XXX-PARTIDA MALA | 16830.31 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-14 | Calidad | XXX-PARTIDA MALA | 997.88 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-04 | XXX-AREA MALA | Viajes | 3578.62 | area_no_valida |
| 2025-04-22 | nan | Alquileres | 1601.56 | area_no_valida |
| 2025-09-29 | I+D | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-07-12 | Contabilidad | nan | 13234.72 | partida_no_valida; partida_no_en_presupuesto |
|  | Contabilidad | Formacion | 2900.69 | fecha_invalida |
| 2025-04-28 | RRHH | Publicidad | -500.00 | importe_invalido |
| 2025-09-29 | Contabilidad | XXX-PARTIDA MALA | 1068.03 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-06 | nan | Personal | 14509.83 | area_no_valida |
|  | I+D | Suministros | 1169.29 | fecha_invalida |
| 2025-09-11 | Direccion | XXX-PARTIDA MALA | 10593.27 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-17 | Operaciones | Seguros | -500.00 | importe_invalido |
| 2025-09-11 | Operaciones | nan | 4314.77 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-11 | Ventas | Hardware | 10000000.00 | importe_excesivo |
| 2025-05-21 | XXX-AREA MALA | Publicidad | 8665.67 | area_no_valida |
| 2025-01-14 | XXX-AREA MALA | Personal | 2348.19 | area_no_valida |
| 2025-04-23 | Operaciones | Personal | -500.00 | importe_invalido |
| 2025-05-21 | RRHH | Suministros | -500.00 | importe_invalido |
| 2025-07-30 | I+D | XXX-PARTIDA MALA | 11502.50 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-28 | nan | Publicidad | 9893.78 | area_no_valida |
|  | I+D | Hardware | 767.13 | fecha_invalida |
| 2025-03-20 | Operaciones | Seguros | 10000000.00 | importe_excesivo |
| 2025-08-30 | Operaciones | XXX-PARTIDA MALA | 6886.17 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-24 | I+D | nan | 1502.63 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-07 | RRHH | XXX-PARTIDA MALA | 3513.44 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-23 | Calidad | Personal | 10000000.00 | importe_excesivo |
| 2025-10-07 | I+D | XXX-PARTIDA MALA | 523.12 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-24 | Direccion | Hardware | -500.00 | importe_invalido |
| 2025-05-05 | I+D | nan | 4487.31 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-11 | Marketing | Hardware | 10000000.00 | importe_excesivo |
|  | RRHH | Software | 18097.87 | fecha_invalida |
| 2025-01-07 | Ventas | nan | 11378.57 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-26 | nan | Mantenimiento | 3059.36 | area_no_valida |
| 2025-03-10 | XXX-AREA MALA | Publicidad | 8701.69 | area_no_valida |
| 2025-05-27 | I+D | nan | 4874.37 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-31 | Direccion | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-07-15 | Contabilidad | XXX-PARTIDA MALA | 674.29 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-11 | Calidad | XXX-PARTIDA MALA | 5969.06 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-09 | XXX-AREA MALA | Software | 11862.27 | area_no_valida |
| 2025-08-18 | XXX-AREA MALA | Seguros | 5889.56 | area_no_valida |
| 2025-03-16 | Contabilidad | Mantenimiento | -500.00 | importe_invalido |
| 2025-01-03 | Direccion | Software | -500.00 | importe_invalido |
| 2025-01-31 | XXX-AREA MALA | Formacion | 8625.35 | area_no_valida |
| 2025-05-26 | Administracion | nan | 4996.61 | partida_no_valida; partida_no_en_presupuesto |
|  | I+D | Suministros | 464.21 | fecha_invalida |
| 2025-07-09 | Contabilidad | nan | 8289.22 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-28 | nan | Formacion | 3503.36 | area_no_valida |
|  | IT | Suministros | 7549.47 | fecha_invalida |
| 2025-02-01 | nan | Hardware | 8873.91 | area_no_valida |
| 2025-02-02 | Contabilidad | Formacion | 10000000.00 | importe_excesivo |
| 2025-07-14 | nan | Hardware | 2333.45 | area_no_valida |
|  | Direccion | Mantenimiento | 13207.56 | fecha_invalida |
| 2025-01-08 | nan | Viajes | 1841.74 | area_no_valida |
| 2025-06-01 | nan | Suministros | 2174.87 | area_no_valida |
| 2025-10-29 | nan | Alquileres | 6812.77 | area_no_valida |
| 2025-05-30 | RRHH | Formacion | 10000000.00 | importe_excesivo |
| 2025-01-14 | Operaciones | Software | 10000000.00 | importe_excesivo |
| 2025-01-11 | Ventas | Personal | -500.00 | importe_invalido |
|  | I+D | Publicidad | 1403.90 | fecha_invalida |
| 2025-03-29 | Contabilidad | Seguros | 10000000.00 | importe_excesivo |
| 2025-08-16 | XXX-AREA MALA | Mantenimiento | 10947.95 | area_no_valida |
| 2025-09-02 | Direccion | Publicidad | 10000000.00 | importe_excesivo |
|  | Calidad | Mantenimiento | 637.74 | fecha_invalida |
| 2025-10-14 | XXX-AREA MALA | Hardware | 5446.98 | area_no_valida |
| 2025-06-30 | nan | Formacion | 6879.52 | area_no_valida |
| 2025-03-18 | XXX-AREA MALA | Formacion | 660.08 | area_no_valida |
| 2025-01-05 | Ventas | Software | 10000000.00 | importe_excesivo |
| 2025-07-31 | IT | Formacion | -500.00 | importe_invalido |
| 2025-10-21 | I+D | nan | 1358.44 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-05 | Administracion | nan | 8764.59 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-10 | I+D | Personal | 10000000.00 | importe_excesivo |
| 2025-03-09 | I+D | Publicidad | -500.00 | importe_invalido |
| 2025-06-06 | Operaciones | Publicidad | 10000000.00 | importe_excesivo |
|  | RRHH | Mantenimiento | 2313.20 | fecha_invalida |
| 2025-03-05 | Operaciones | Software | -500.00 | importe_invalido |
| 2025-06-13 | Direccion | Mantenimiento | -500.00 | importe_invalido |
| 2025-06-05 | IT | Alquileres | -500.00 | importe_invalido |
|  | Marketing | Personal | 2729.97 | fecha_invalida |
| 2025-07-03 | IT | nan | 882.73 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-27 | nan | Suministros | 5177.48 | area_no_valida |
|  | Calidad | Personal | 15759.13 | fecha_invalida |
| 2025-10-26 | Operaciones | Personal | 10000000.00 | importe_excesivo |
| 2025-08-16 | Contabilidad | XXX-PARTIDA MALA | 10506.63 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-01 | Contabilidad | nan | 6712.53 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-03 | XXX-AREA MALA | Personal | 776.36 | area_no_valida |
| 2025-10-22 | XXX-AREA MALA | Publicidad | 12816.57 | area_no_valida |
|  | Calidad | Hardware | 10472.75 | fecha_invalida |
| 2025-06-29 | RRHH | nan | 14849.20 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-02 | Operaciones | XXX-PARTIDA MALA | 4215.17 | partida_no_valida; partida_no_en_presupuesto |
|  | Contabilidad | Software | 12850.68 | fecha_invalida |
| 2025-08-20 | Ventas | XXX-PARTIDA MALA | 283.62 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-23 | Operaciones | Alquileres | 10000000.00 | importe_excesivo |
| 2025-11-08 | XXX-AREA MALA | Hardware | 3849.66 | area_no_valida |
| 2025-01-31 | XXX-AREA MALA | Alquileres | 2447.66 | area_no_valida |
| 2025-07-29 | IT | XXX-PARTIDA MALA | 7691.01 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-16 | Ventas | nan | 8739.07 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-12 | Ventas | Alquileres | -500.00 | importe_invalido |
| 2025-07-26 | XXX-AREA MALA | Suministros | 11137.34 | area_no_valida |
| 2025-05-10 | Contabilidad | XXX-PARTIDA MALA | 2435.40 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-22 | Ventas | nan | 4663.25 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-07 | Administracion | nan | 1094.88 | partida_no_valida; partida_no_en_presupuesto |
|  | Ventas | Personal | 14750.46 | fecha_invalida |
| 2025-07-18 | nan | Mantenimiento | 12794.68 | area_no_valida |
| 2025-03-24 | Calidad | XXX-PARTIDA MALA | 7894.83 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-15 | RRHH | Personal | -500.00 | importe_invalido |
|  | I+D | Seguros | 246.03 | fecha_invalida |
| 2025-10-04 | Operaciones | nan | 3615.08 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-04 | XXX-AREA MALA | Alquileres | 3525.32 | area_no_valida |
| 2025-05-21 | nan | Hardware | 943.23 | area_no_valida |
|  | IT | Publicidad | 3117.46 | fecha_invalida |
| 2025-04-27 | Direccion | XXX-PARTIDA MALA | 351.06 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-25 | RRHH | Alquileres | -500.00 | importe_invalido |
| 2025-02-25 | Contabilidad | XXX-PARTIDA MALA | 4423.86 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-18 | XXX-AREA MALA | Suministros | 1674.71 | area_no_valida |
| 2025-09-15 | nan | Suministros | 5914.33 | area_no_valida |
| 2025-08-18 | Administracion | Publicidad | -500.00 | importe_invalido |
| 2025-04-22 | Administracion | nan | 7732.47 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-08 | Direccion | XXX-PARTIDA MALA | 932.41 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-15 | nan | Hardware | 561.84 | area_no_valida |
| 2025-09-07 | Direccion | nan | 11032.43 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-14 | I+D | XXX-PARTIDA MALA | 1642.57 | partida_no_valida; partida_no_en_presupuesto |
|  | Operaciones | Suministros | 918.04 | fecha_invalida |
|  | I+D | Hardware | 1206.57 | fecha_invalida |
| 2025-10-11 | Contabilidad | XXX-PARTIDA MALA | 1106.30 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-08 | RRHH | Hardware | -500.00 | importe_invalido |
| 2025-01-14 | Calidad | nan | 4798.84 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-02 | Administracion | XXX-PARTIDA MALA | 8264.95 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-26 | RRHH | Viajes | 10000000.00 | importe_excesivo |
| 2025-06-17 | XXX-AREA MALA | Mantenimiento | 4482.23 | area_no_valida |
| 2025-02-25 | nan | Hardware | 10139.93 | area_no_valida |
| 2025-07-11 | Administracion | nan | 5951.26 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-07 | Administracion | XXX-PARTIDA MALA | 14948.16 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-30 | XXX-AREA MALA | Publicidad | 4145.88 | area_no_valida |
|  | I+D | Publicidad | 785.67 | fecha_invalida |
| 2025-11-10 | nan | Alquileres | 2166.97 | area_no_valida |
| 2025-07-16 | Calidad | Publicidad | 10000000.00 | importe_excesivo |
|  | Calidad | Viajes | 9707.38 | fecha_invalida |
| 2025-08-21 | XXX-AREA MALA | Suministros | 120.30 | area_no_valida |
| 2025-08-29 | RRHH | Alquileres | 10000000.00 | importe_excesivo |
| 2025-08-07 | nan | Hardware | 1144.44 | area_no_valida |
| 2025-01-30 | Direccion | nan | 15621.58 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-25 | Operaciones | Alquileres | -500.00 | importe_invalido |
|  | Marketing | Viajes | 1921.62 | fecha_invalida |
| 2025-01-25 | Direccion | XXX-PARTIDA MALA | 9330.35 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-22 | Administracion | XXX-PARTIDA MALA | 1166.14 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-23 | nan | Viajes | 7547.35 | area_no_valida |
| 2025-06-08 | IT | XXX-PARTIDA MALA | 3340.75 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-26 | Ventas | Viajes | -500.00 | importe_invalido |
| 2025-09-08 | I+D | XXX-PARTIDA MALA | 4300.84 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-01 | IT | Viajes | 10000000.00 | importe_excesivo |
|  | RRHH | Suministros | 3065.93 | fecha_invalida |
| 2025-03-20 | RRHH | Publicidad | -500.00 | importe_invalido |
| 2025-07-26 | nan | Suministros | 4120.46 | area_no_valida |
| 2025-03-04 | XXX-AREA MALA | Seguros | 10116.80 | area_no_valida |
| 2025-01-12 | RRHH | nan | 6708.93 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-13 | RRHH | Alquileres | 10000000.00 | importe_excesivo |
| 2025-08-04 | XXX-AREA MALA | Formacion | 520.76 | area_no_valida |
| 2025-07-29 | I+D | Software | 10000000.00 | importe_excesivo |
| 2025-01-22 | Contabilidad | Suministros | -500.00 | importe_invalido |
| 2025-07-12 | RRHH | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-09-04 | Administracion | XXX-PARTIDA MALA | 3841.38 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-19 | RRHH | Formacion | 10000000.00 | importe_excesivo |
| 2025-02-14 | XXX-AREA MALA | Hardware | 10503.43 | area_no_valida |
| 2025-10-05 | Ventas | Personal | -500.00 | importe_invalido |
| 2025-01-06 | nan | Software | 7798.46 | area_no_valida |
| 2025-07-17 | nan | Formacion | 2696.96 | area_no_valida |
|  | I+D | Suministros | 472.00 | fecha_invalida |
| 2025-10-04 | Marketing | XXX-PARTIDA MALA | 11208.37 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-19 | nan | Hardware | 16039.15 | area_no_valida |
| 2025-01-28 | Contabilidad | Publicidad | -500.00 | importe_invalido |
| 2025-02-25 | Administracion | nan | 619.01 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-23 | Direccion | Software | 10000000.00 | importe_excesivo |
| 2025-02-24 | IT | Alquileres | -500.00 | importe_invalido |
| 2025-08-25 | nan | Suministros | 1254.71 | area_no_valida |
| 2025-09-07 | Operaciones | Viajes | -500.00 | importe_invalido |
| 2025-07-14 | Direccion | nan | 334.81 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-04 | XXX-AREA MALA | Suministros | 6990.76 | area_no_valida |
| 2025-01-03 | Calidad | Suministros | -500.00 | importe_invalido |
| 2025-02-11 | IT | nan | 4517.16 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-26 | nan | Software | 16546.83 | area_no_valida |
| 2025-09-27 | nan | Personal | 16532.77 | area_no_valida |
| 2025-04-20 | Direccion | Hardware | -500.00 | importe_invalido |
| 2025-03-02 | Direccion | Seguros | 10000000.00 | importe_excesivo |
| 2025-09-02 | Calidad | nan | 4147.73 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-13 | Operaciones | nan | 1775.61 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-15 | Ventas | nan | 10086.04 | partida_no_valida; partida_no_en_presupuesto |
|  | RRHH | Personal | 7402.95 | fecha_invalida |
|  | Contabilidad | Suministros | 644.85 | fecha_invalida |
| 2025-06-15 | Operaciones | Suministros | -500.00 | importe_invalido |
| 2025-02-11 | XXX-AREA MALA | Viajes | 2882.19 | area_no_valida |
| 2025-03-02 | XXX-AREA MALA | Viajes | 11492.68 | area_no_valida |
| 2025-02-19 | Marketing | Personal | -500.00 | importe_invalido |
| 2025-05-21 | Marketing | XXX-PARTIDA MALA | 492.47 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-11 | RRHH | Formacion | -500.00 | importe_invalido |
| 2025-10-27 | IT | Software | 10000000.00 | importe_excesivo |
| 2025-02-25 | nan | Hardware | 8516.05 | area_no_valida |
| 2025-05-10 | I+D | Personal | -500.00 | importe_invalido |
| 2025-05-08 | RRHH | nan | 15469.07 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-10 | Calidad | XXX-PARTIDA MALA | 3640.49 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-09 | XXX-AREA MALA | Formacion | 3503.84 | area_no_valida |
| 2025-06-12 | XXX-AREA MALA | Viajes | 2223.21 | area_no_valida |
| 2025-02-22 | RRHH | nan | 199.43 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-10 | Marketing | Personal | -500.00 | importe_invalido |
| 2025-06-30 | nan | Software | 308.30 | area_no_valida |
|  | RRHH | Seguros | 682.43 | fecha_invalida |
| 2025-09-11 | IT | XXX-PARTIDA MALA | 6832.71 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-20 | nan | Personal | 10025.58 | area_no_valida |
|  | Ventas | Seguros | 5371.50 | fecha_invalida |
|  | I+D | Formacion | 1896.81 | fecha_invalida |
| 2025-03-30 | IT | nan | 4073.40 | partida_no_valida; partida_no_en_presupuesto |
|  | RRHH | Personal | 8183.74 | fecha_invalida |
| 2025-11-06 | IT | XXX-PARTIDA MALA | 262.57 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-05 | Administracion | Alquileres | -500.00 | importe_invalido |
| 2025-09-30 | I+D | Alquileres | -500.00 | importe_invalido |
| 2025-07-25 | XXX-AREA MALA | Viajes | 6705.55 | area_no_valida |
| 2025-09-05 | Marketing | Personal | -500.00 | importe_invalido |
|  | Contabilidad | Formacion | 1026.22 | fecha_invalida |
|  | Marketing | Viajes | 2762.63 | fecha_invalida |
| 2025-10-26 | XXX-AREA MALA | Alquileres | 8237.57 | area_no_valida |
| 2025-07-29 | RRHH | Software | -500.00 | importe_invalido |
|  | I+D | Mantenimiento | 6413.44 | fecha_invalida |
| 2025-08-05 | Contabilidad | Alquileres | -500.00 | importe_invalido |
| 2025-08-27 | Direccion | XXX-PARTIDA MALA | 11720.49 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-16 | I+D | XXX-PARTIDA MALA | 3119.26 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-23 | XXX-AREA MALA | Personal | 3514.32 | area_no_valida |
| 2025-03-20 | nan | Mantenimiento | 7318.49 | area_no_valida |
| 2025-04-26 | nan | Software | 9954.59 | area_no_valida |
| 2025-01-15 | Contabilidad | nan | 2505.73 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-12 | RRHH | Hardware | -500.00 | importe_invalido |
| 2025-07-24 | Administracion | XXX-PARTIDA MALA | 4688.15 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-25 | nan | Publicidad | 544.85 | area_no_valida |
| 2025-04-23 | XXX-AREA MALA | Formacion | 2258.76 | area_no_valida |
| 2025-10-09 | nan | Personal | 3245.86 | area_no_valida |
| 2025-09-06 | Calidad | Seguros | 10000000.00 | importe_excesivo |
| 2025-02-10 | XXX-AREA MALA | Alquileres | 1894.01 | area_no_valida |
| 2025-07-10 | Ventas | nan | 1319.02 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-01 | Contabilidad | Seguros | 10000000.00 | importe_excesivo |
| 2025-03-27 | XXX-AREA MALA | Viajes | 6773.84 | area_no_valida |
| 2025-01-26 | Calidad | XXX-PARTIDA MALA | 8656.42 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-10 | Administracion | XXX-PARTIDA MALA | 9055.88 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-06 | RRHH | XXX-PARTIDA MALA | 6516.89 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-16 | Calidad | nan | 3832.17 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-15 | Administracion | nan | 7966.99 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-16 | Administracion | Formacion | -500.00 | importe_invalido |
| 2025-03-06 | Administracion | Viajes | -500.00 | importe_invalido |
| 2025-08-22 | Calidad | Suministros | 10000000.00 | importe_excesivo |
| 2025-04-22 | XXX-AREA MALA | Seguros | 736.46 | area_no_valida |
| 2025-10-27 | Operaciones | Viajes | -500.00 | importe_invalido |
|  | I+D | Suministros | 1336.69 | fecha_invalida |
| 2025-05-18 | I+D | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-04-05 | XXX-AREA MALA | Software | 1537.19 | area_no_valida |
| 2025-07-17 | Direccion | Software | -500.00 | importe_invalido |
| 2025-08-03 | XXX-AREA MALA | Alquileres | 192.40 | area_no_valida |
| 2025-04-21 | RRHH | Viajes | 10000000.00 | importe_excesivo |
| 2025-07-19 | nan | Suministros | 11579.65 | area_no_valida |
| 2025-08-31 | I+D | nan | 1002.26 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-06 | IT | XXX-PARTIDA MALA | 2179.04 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-13 | Marketing | nan | 4434.55 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-31 | nan | Mantenimiento | 6635.18 | area_no_valida |
| 2025-07-25 | Marketing | Personal | 10000000.00 | importe_excesivo |
| 2025-10-04 | Ventas | nan | 965.06 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-23 | Direccion | nan | 2394.69 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-15 | nan | Publicidad | 1040.85 | area_no_valida |
| 2025-07-26 | I+D | XXX-PARTIDA MALA | 4228.50 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-06 | XXX-AREA MALA | Mantenimiento | 7266.63 | area_no_valida |
|  | Operaciones | Alquileres | 11361.11 | fecha_invalida |
|  | Calidad | Hardware | 7280.04 | fecha_invalida |
| 2025-06-06 | nan | Seguros | 6202.51 | area_no_valida |
| 2025-09-04 | Operaciones | XXX-PARTIDA MALA | 151.49 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-23 | Ventas | XXX-PARTIDA MALA | 688.25 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-04 | Contabilidad | Software | 10000000.00 | importe_excesivo |
| 2025-05-09 | Contabilidad | Seguros | 10000000.00 | importe_excesivo |
| 2025-01-10 | Marketing | XXX-PARTIDA MALA | 9811.83 | partida_no_valida; partida_no_en_presupuesto |
|  | IT | Seguros | 10583.99 | fecha_invalida |
| 2025-07-17 | RRHH | Seguros | 10000000.00 | importe_excesivo |
| 2025-06-24 | Ventas | nan | 5276.12 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-10 | Administracion | XXX-PARTIDA MALA | 1813.64 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-28 | nan | Publicidad | 1188.75 | area_no_valida |
| 2025-01-05 | RRHH | Viajes | 10000000.00 | importe_excesivo |
| 2025-10-01 | I+D | XXX-PARTIDA MALA | 1678.19 | partida_no_valida; partida_no_en_presupuesto |
|  | Calidad | Software | 4470.25 | fecha_invalida |
| 2025-08-27 | Direccion | Hardware | -500.00 | importe_invalido |
| 2025-06-11 | nan | Personal | 639.97 | area_no_valida |
| 2025-05-05 | IT | Software | -500.00 | importe_invalido |
| 2025-07-19 | XXX-AREA MALA | Mantenimiento | 15544.83 | area_no_valida |
| 2025-10-02 | Administracion | Hardware | 10000000.00 | importe_excesivo |
| 2025-02-15 | XXX-AREA MALA | Viajes | 6341.88 | area_no_valida |
| 2025-02-27 | RRHH | Software | -500.00 | importe_invalido |
| 2025-07-25 | nan | Personal | 14602.65 | area_no_valida |
| 2025-01-28 | I+D | Hardware | 10000000.00 | importe_excesivo |
| 2025-04-16 | Administracion | Publicidad | 10000000.00 | importe_excesivo |
| 2025-10-26 | Marketing | nan | 684.54 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-08 | IT | Hardware | -500.00 | importe_invalido |
| 2025-10-15 | Administracion | XXX-PARTIDA MALA | 10631.37 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-16 | XXX-AREA MALA | Publicidad | 5223.71 | area_no_valida |
| 2025-10-31 | RRHH | XXX-PARTIDA MALA | 11048.65 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-05 | Marketing | Viajes | -500.00 | importe_invalido |
| 2025-01-30 | Ventas | Personal | -500.00 | importe_invalido |
| 2025-03-21 | Calidad | Seguros | 10000000.00 | importe_excesivo |
| 2025-04-17 | Administracion | XXX-PARTIDA MALA | 595.74 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-13 | Administracion | Viajes | -500.00 | importe_invalido |
| 2025-02-13 | nan | Formacion | 11611.05 | area_no_valida |
| 2025-01-03 | Ventas | Software | 10000000.00 | importe_excesivo |
|  | I+D | Hardware | 882.10 | fecha_invalida |
| 2025-07-25 | RRHH | Publicidad | -500.00 | importe_invalido |
|  | Marketing | Software | 3578.29 | fecha_invalida |
| 2025-03-18 | XXX-AREA MALA | Publicidad | 3493.49 | area_no_valida |
| 2025-10-30 | Calidad | Software | 10000000.00 | importe_excesivo |
| 2025-02-23 | I+D | Software | -500.00 | importe_invalido |
|  | Direccion | Mantenimiento | 11404.30 | fecha_invalida |
|  | Ventas | Software | 929.17 | fecha_invalida |
| 2025-08-20 | nan | Hardware | 18317.07 | area_no_valida |
| 2025-09-24 | Direccion | Viajes | 10000000.00 | importe_excesivo |
| 2025-08-09 | Contabilidad | nan | 2118.70 | partida_no_valida; partida_no_en_presupuesto |
|  | Calidad | Software | 1165.96 | fecha_invalida |
| 2025-02-25 | IT | Suministros | 10000000.00 | importe_excesivo |
| 2025-05-08 | Marketing | XXX-PARTIDA MALA | 11660.70 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-21 | Marketing | nan | 450.55 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-04 | Operaciones | XXX-PARTIDA MALA | 951.86 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-25 | RRHH | XXX-PARTIDA MALA | 9391.08 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-23 | Contabilidad | nan | 1266.93 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-25 | nan | Suministros | 3887.28 | area_no_valida |
| 2025-10-06 | RRHH | nan | 447.56 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-15 | nan | Alquileres | 954.90 | area_no_valida |
| 2025-09-19 | nan | Software | 10943.22 | area_no_valida |
| 2025-07-24 | nan | Formacion | 2338.04 | area_no_valida |
| 2025-06-12 | RRHH | Mantenimiento | 10000000.00 | importe_excesivo |
|  | Operaciones | Alquileres | 6668.03 | fecha_invalida |
| 2025-07-02 | IT | Hardware | -500.00 | importe_invalido |
| 2025-07-26 | Contabilidad | Seguros | 10000000.00 | importe_excesivo |
| 2025-02-02 | Contabilidad | nan | 6257.02 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-13 | Administracion | XXX-PARTIDA MALA | 13121.56 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-30 | XXX-AREA MALA | Formacion | 2688.76 | area_no_valida |
| 2025-04-10 | I+D | XXX-PARTIDA MALA | 7014.24 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-17 | XXX-AREA MALA | Suministros | 12070.99 | area_no_valida |
| 2025-07-05 | nan | Personal | 13842.28 | area_no_valida |
| 2025-05-06 | RRHH | XXX-PARTIDA MALA | 2265.38 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-19 | Contabilidad | Formacion | -500.00 | importe_invalido |
| 2025-06-05 | IT | Hardware | 10000000.00 | importe_excesivo |
| 2025-07-10 | XXX-AREA MALA | Personal | 7318.01 | area_no_valida |
| 2025-09-18 | nan | Seguros | 628.43 | area_no_valida |
| 2025-02-02 | RRHH | nan | 6836.37 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-16 | I+D | Alquileres | -500.00 | importe_invalido |
| 2025-07-06 | Marketing | Viajes | 10000000.00 | importe_excesivo |
| 2025-04-21 | Operaciones | nan | 2533.92 | partida_no_valida; partida_no_en_presupuesto |
|  | Direccion | Personal | 1073.31 | fecha_invalida |
| 2025-04-05 | Contabilidad | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-05-08 | Operaciones | Suministros | 10000000.00 | importe_excesivo |
| 2025-08-16 | Ventas | XXX-PARTIDA MALA | 7674.59 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-01 | Contabilidad | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-03-27 | Administracion | Seguros | -500.00 | importe_invalido |
| 2025-04-16 | nan | Publicidad | 2416.18 | area_no_valida |
| 2025-08-22 | nan | Suministros | 3071.68 | area_no_valida |
|  | I+D | Formacion | 1868.20 | fecha_invalida |
| 2025-10-30 | RRHH | nan | 9705.76 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-04 | Administracion | Hardware | 10000000.00 | importe_excesivo |
|  | Operaciones | Mantenimiento | 13604.36 | fecha_invalida |
| 2025-09-10 | nan | Viajes | 5026.89 | area_no_valida |
| 2025-07-29 | Calidad | nan | 3969.06 | partida_no_valida; partida_no_en_presupuesto |
|  | Administracion | Alquileres | 5454.10 | fecha_invalida |
| 2025-05-14 | I+D | Personal | -500.00 | importe_invalido |
| 2025-10-16 | nan | Formacion | 1172.57 | area_no_valida |
| 2025-02-06 | XXX-AREA MALA | Software | 9808.98 | area_no_valida |
| 2025-05-13 | I+D | Hardware | 10000000.00 | importe_excesivo |
|  | Direccion | Suministros | 9046.89 | fecha_invalida |
| 2025-02-10 | Ventas | Mantenimiento | -500.00 | importe_invalido |
| 2025-09-19 | Administracion | XXX-PARTIDA MALA | 5646.81 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-02 | IT | Publicidad | -500.00 | importe_invalido |
| 2025-09-23 | XXX-AREA MALA | Mantenimiento | 3124.66 | area_no_valida |
| 2025-06-10 | Marketing | Hardware | 10000000.00 | importe_excesivo |
| 2025-03-15 | Ventas | Seguros | 10000000.00 | importe_excesivo |
|  | Administracion | Seguros | 8769.60 | fecha_invalida |
| 2025-08-28 | nan | Mantenimiento | 11168.27 | area_no_valida |
| 2025-09-01 | XXX-AREA MALA | Suministros | 1133.13 | area_no_valida |
|  | IT | Personal | 6620.44 | fecha_invalida |
| 2025-05-10 | nan | Publicidad | 16795.41 | area_no_valida |
| 2025-06-14 | nan | Seguros | 395.92 | area_no_valida |
|  | Direccion | Alquileres | 1041.17 | fecha_invalida |
|  | Ventas | Software | 1568.55 | fecha_invalida |
| 2025-02-19 | RRHH | nan | 2814.12 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-29 | Administracion | Viajes | 10000000.00 | importe_excesivo |
| 2025-03-13 | Direccion | Viajes | 10000000.00 | importe_excesivo |
| 2025-05-28 | nan | Seguros | 9241.00 | area_no_valida |
| 2025-10-01 | I+D | nan | 1653.04 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-10 | Contabilidad | Suministros | 10000000.00 | importe_excesivo |
| 2025-03-26 | XXX-AREA MALA | Software | 2484.65 | area_no_valida |
| 2025-04-29 | Marketing | XXX-PARTIDA MALA | 2738.36 | partida_no_valida; partida_no_en_presupuesto |
|  | Administracion | Viajes | 10286.69 | fecha_invalida |
|  | IT | Hardware | 495.22 | fecha_invalida |
| 2025-01-31 | Marketing | XXX-PARTIDA MALA | 9084.38 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-30 | XXX-AREA MALA | Suministros | 2657.18 | area_no_valida |
| 2025-01-26 | nan | Software | 720.71 | area_no_valida |
| 2025-05-19 | Administracion | nan | 2291.25 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-06 | Contabilidad | Publicidad | 10000000.00 | importe_excesivo |
| 2025-09-09 | Direccion | Alquileres | -500.00 | importe_invalido |
| 2025-01-22 | XXX-AREA MALA | Publicidad | 7570.04 | area_no_valida |
| 2025-01-27 | nan | Publicidad | 8764.71 | area_no_valida |
| 2025-05-04 | IT | XXX-PARTIDA MALA | 5980.65 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-30 | Marketing | Personal | 10000000.00 | importe_excesivo |
| 2025-07-04 | XXX-AREA MALA | Mantenimiento | 4623.39 | area_no_valida |
| 2025-03-04 | Ventas | Viajes | 10000000.00 | importe_excesivo |
| 2025-08-17 | nan | Formacion | 2670.77 | area_no_valida |
| 2025-03-08 | XXX-AREA MALA | Hardware | 11322.34 | area_no_valida |
|  | I+D | Formacion | 2831.24 | fecha_invalida |
| 2025-04-18 | IT | Personal | -500.00 | importe_invalido |
| 2025-06-20 | nan | Mantenimiento | 461.65 | area_no_valida |
|  | RRHH | Seguros | 1033.25 | fecha_invalida |
| 2025-01-06 | Administracion | XXX-PARTIDA MALA | 11533.34 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-06 | Direccion | Formacion | 10000000.00 | importe_excesivo |
| 2025-02-03 | XXX-AREA MALA | Publicidad | 683.60 | area_no_valida |
| 2025-01-03 | Ventas | nan | 9682.47 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-22 | nan | Viajes | 4777.01 | area_no_valida |
|  | RRHH | Software | 17799.34 | fecha_invalida |
| 2025-03-29 | Contabilidad | XXX-PARTIDA MALA | 5989.22 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-10 | XXX-AREA MALA | Seguros | 296.71 | area_no_valida |
| 2025-02-12 | Direccion | nan | 9504.14 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-22 | Operaciones | Personal | 10000000.00 | importe_excesivo |
| 2025-09-13 | nan | Publicidad | 4929.68 | area_no_valida |
| 2025-06-01 | Administracion | nan | 18472.25 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-07 | XXX-AREA MALA | Publicidad | 8977.82 | area_no_valida |
| 2025-08-07 | RRHH | Suministros | -500.00 | importe_invalido |
| 2025-09-25 | Administracion | XXX-PARTIDA MALA | 5742.25 | partida_no_valida; partida_no_en_presupuesto |
|  | Contabilidad | Suministros | 837.57 | fecha_invalida |
| 2025-11-03 | XXX-AREA MALA | Mantenimiento | 10954.43 | area_no_valida |
| 2025-01-14 | Administracion | XXX-PARTIDA MALA | 7739.30 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-21 | Ventas | nan | 1658.55 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-21 | Administracion | Hardware | 10000000.00 | importe_excesivo |
| 2025-01-24 | Ventas | XXX-PARTIDA MALA | 9472.13 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-21 | nan | Viajes | 7385.25 | area_no_valida |
| 2025-03-12 | Calidad | Software | 10000000.00 | importe_excesivo |
| 2025-02-27 | nan | Suministros | 4640.03 | area_no_valida |
|  | Ventas | Formacion | 6731.62 | fecha_invalida |
| 2025-07-27 | RRHH | nan | 17345.81 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-11 | I+D | nan | 7834.06 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-21 | nan | Software | 6983.58 | area_no_valida |
| 2025-01-30 | XXX-AREA MALA | Seguros | 3960.15 | area_no_valida |
| 2025-10-04 | Direccion | Mantenimiento | 10000000.00 | importe_excesivo |
|  | I+D | Formacion | 6337.47 | fecha_invalida |
| 2025-07-04 | XXX-AREA MALA | Alquileres | 2708.43 | area_no_valida |
| 2025-05-21 | XXX-AREA MALA | Alquileres | 3409.31 | area_no_valida |
| 2025-01-03 | Contabilidad | nan | 303.83 | partida_no_valida; partida_no_en_presupuesto |
|  | I+D | Suministros | 1393.75 | fecha_invalida |
| 2025-10-16 | I+D | nan | 1026.25 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-14 | nan | Software | 111.07 | area_no_valida |
| 2025-01-25 | nan | Publicidad | 693.85 | area_no_valida |
| 2025-08-16 | Direccion | Publicidad | -500.00 | importe_invalido |
|  | Marketing | Suministros | 7090.61 | fecha_invalida |
| 2025-10-28 | XXX-AREA MALA | Hardware | 1024.95 | area_no_valida |
| 2025-10-04 | I+D | Software | -500.00 | importe_invalido |
| 2025-02-14 | Direccion | nan | 12379.94 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-08 | nan | Mantenimiento | 9903.67 | area_no_valida |
|  | Direccion | Alquileres | 1347.36 | fecha_invalida |
| 2025-11-10 | Calidad | XXX-PARTIDA MALA | 2271.68 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-21 | Ventas | Alquileres | 10000000.00 | importe_excesivo |
| 2025-04-05 | XXX-AREA MALA | Publicidad | 191.53 | area_no_valida |
| 2025-04-26 | nan | Hardware | 17623.32 | area_no_valida |
| 2025-09-01 | Contabilidad | Viajes | -500.00 | importe_invalido |
| 2025-11-02 | Operaciones | Seguros | 10000000.00 | importe_excesivo |
| 2025-03-25 | nan | Viajes | 762.49 | area_no_valida |
| 2025-06-23 | Administracion | nan | 5526.54 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-24 | XXX-AREA MALA | Alquileres | 7365.92 | area_no_valida |
| 2025-04-30 | nan | Suministros | 361.98 | area_no_valida |
| 2025-09-04 | XXX-AREA MALA | Suministros | 2130.70 | area_no_valida |
| 2025-10-08 | Contabilidad | XXX-PARTIDA MALA | 1030.92 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-29 | Marketing | nan | 11246.67 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-13 | XXX-AREA MALA | Publicidad | 1777.43 | area_no_valida |
| 2025-08-16 | Operaciones | Publicidad | -500.00 | importe_invalido |
| 2025-06-30 | XXX-AREA MALA | Seguros | 4074.81 | area_no_valida |
| 2025-01-31 | nan | Suministros | 8735.58 | area_no_valida |
| 2025-04-06 | Operaciones | Software | 10000000.00 | importe_excesivo |
| 2025-04-21 | nan | Software | 668.31 | area_no_valida |
| 2025-03-12 | nan | Seguros | 2957.81 | area_no_valida |
| 2025-05-08 | Marketing | Hardware | -500.00 | importe_invalido |
| 2025-09-04 | Ventas | Suministros | 10000000.00 | importe_excesivo |
| 2025-03-14 | Direccion | Publicidad | 10000000.00 | importe_excesivo |
| 2025-09-11 | RRHH | XXX-PARTIDA MALA | 4831.72 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-09 | RRHH | Suministros | -500.00 | importe_invalido |
| 2025-10-14 | IT | XXX-PARTIDA MALA | 5917.66 | partida_no_valida; partida_no_en_presupuesto |
|  | IT | Seguros | 8076.57 | fecha_invalida |
| 2025-08-25 | Contabilidad | Alquileres | 10000000.00 | importe_excesivo |
|  | I+D | Formacion | 11682.36 | fecha_invalida |
| 2025-01-04 | I+D | Software | -500.00 | importe_invalido |
| 2025-10-22 | I+D | XXX-PARTIDA MALA | 3471.91 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-19 | IT | XXX-PARTIDA MALA | 1981.32 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-12 | Ventas | nan | 3175.26 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-29 | Contabilidad | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-08-02 | XXX-AREA MALA | Software | 1067.47 | area_no_valida |
| 2025-09-09 | Administracion | Personal | 10000000.00 | importe_excesivo |
| 2025-04-20 | XXX-AREA MALA | Publicidad | 13069.09 | area_no_valida |
|  | Calidad | Personal | 7193.38 | fecha_invalida |
| 2025-03-26 | I+D | nan | 171.37 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-15 | Calidad | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-08-23 | Marketing | XXX-PARTIDA MALA | 4914.18 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-25 | Operaciones | XXX-PARTIDA MALA | 1928.11 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-04 | XXX-AREA MALA | Software | 12864.96 | area_no_valida |
| 2025-08-27 | Contabilidad | nan | 16571.27 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-01 | Ventas | nan | 10466.07 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-18 | IT | Publicidad | 10000000.00 | importe_excesivo |
| 2025-09-17 | XXX-AREA MALA | Alquileres | 2866.59 | area_no_valida |
| 2025-04-26 | XXX-AREA MALA | Alquileres | 3733.89 | area_no_valida |
| 2025-01-09 | nan | Alquileres | 7853.65 | area_no_valida |
| 2025-09-19 | Ventas | Software | -500.00 | importe_invalido |
| 2025-06-07 | Direccion | Viajes | -500.00 | importe_invalido |
| 2025-05-27 | Calidad | XXX-PARTIDA MALA | 4454.83 | partida_no_valida; partida_no_en_presupuesto |
|  | Operaciones | Personal | 856.29 | fecha_invalida |
| 2025-07-03 | Administracion | nan | 1245.27 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-04 | Calidad | XXX-PARTIDA MALA | 1025.57 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-23 | nan | Publicidad | 2265.35 | area_no_valida |
| 2025-03-21 | nan | Formacion | 13994.42 | area_no_valida |
| 2025-03-24 | Operaciones | Hardware | 10000000.00 | importe_excesivo |
| 2025-10-02 | Calidad | Alquileres | -500.00 | importe_invalido |
| 2025-07-28 | RRHH | nan | 19464.33 | partida_no_valida; partida_no_en_presupuesto |
|  | Direccion | Alquileres | 2269.58 | fecha_invalida |
| 2025-01-07 | Marketing | Software | 10000000.00 | importe_excesivo |
| 2025-05-07 | Administracion | Publicidad | -500.00 | importe_invalido |
|  | Marketing | Publicidad | 5023.85 | fecha_invalida |
| 2025-10-26 | I+D | Suministros | -500.00 | importe_invalido |
| 2025-08-31 | Administracion | XXX-PARTIDA MALA | 2757.06 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-14 | Marketing | XXX-PARTIDA MALA | 3334.22 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-11 | Contabilidad | Personal | -500.00 | importe_invalido |
| 2025-03-14 | Direccion | nan | 190.83 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-04 | Calidad | Software | 10000000.00 | importe_excesivo |
| 2025-08-12 | XXX-AREA MALA | Publicidad | 10194.06 | area_no_valida |
| 2025-07-07 | Direccion | XXX-PARTIDA MALA | 6134.92 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-02 | Marketing | Hardware | -500.00 | importe_invalido |
| 2025-01-31 | nan | Viajes | 5539.25 | area_no_valida |
| 2025-08-31 | nan | Suministros | 1599.89 | area_no_valida |
| 2025-02-05 | nan | Hardware | 13424.34 | area_no_valida |
| 2025-08-14 | nan | Viajes | 1544.44 | area_no_valida |
| 2025-06-12 | nan | Formacion | 3081.31 | area_no_valida |
|  | Administracion | Formacion | 4631.36 | fecha_invalida |
| 2025-08-25 | nan | Alquileres | 7135.33 | area_no_valida |
| 2025-02-20 | Ventas | Hardware | -500.00 | importe_invalido |
| 2025-04-22 | Contabilidad | Software | -500.00 | importe_invalido |
| 2025-10-05 | I+D | Formacion | 10000000.00 | importe_excesivo |
| 2025-09-09 | I+D | Personal | 10000000.00 | importe_excesivo |
| 2025-01-30 | XXX-AREA MALA | Publicidad | 9591.31 | area_no_valida |
| 2025-07-23 | Calidad | nan | 970.35 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-25 | Marketing | XXX-PARTIDA MALA | 780.92 | partida_no_valida; partida_no_en_presupuesto |
|  | Marketing | Mantenimiento | 4675.97 | fecha_invalida |
| 2025-01-19 | Operaciones | Formacion | 10000000.00 | importe_excesivo |
| 2025-04-01 | I+D | Alquileres | -500.00 | importe_invalido |
| 2025-06-25 | Administracion | Personal | 10000000.00 | importe_excesivo |
|  | Operaciones | Formacion | 4382.34 | fecha_invalida |
| 2025-09-25 | I+D | Seguros | -500.00 | importe_invalido |
| 2025-09-22 | IT | nan | 1340.32 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-11 | Operaciones | Formacion | 10000000.00 | importe_excesivo |
| 2025-01-04 | I+D | nan | 694.97 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-23 | Calidad | nan | 4916.39 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-31 | Calidad | Personal | -500.00 | importe_invalido |
| 2025-04-15 | nan | Seguros | 6548.61 | area_no_valida |
| 2025-08-01 | Direccion | Publicidad | 10000000.00 | importe_excesivo |
| 2025-04-06 | XXX-AREA MALA | Software | 358.23 | area_no_valida |
| 2025-10-18 | Administracion | Alquileres | 10000000.00 | importe_excesivo |
| 2025-06-25 | I+D | Personal | -500.00 | importe_invalido |
| 2025-05-09 | Administracion | Seguros | -500.00 | importe_invalido |
| 2025-06-25 | XXX-AREA MALA | Seguros | 831.63 | area_no_valida |
| 2025-07-14 | XXX-AREA MALA | Seguros | 3136.57 | area_no_valida |
| 2025-05-15 | XXX-AREA MALA | Software | 11205.70 | area_no_valida |
| 2025-08-21 | IT | Software | -500.00 | importe_invalido |
| 2025-05-26 | nan | Personal | 2403.91 | area_no_valida |
| 2025-09-16 | Operaciones | XXX-PARTIDA MALA | 1073.74 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-03 | Direccion | XXX-PARTIDA MALA | 1610.67 | partida_no_valida; partida_no_en_presupuesto |
|  | IT | Hardware | 7851.08 | fecha_invalida |
| 2025-05-16 | XXX-AREA MALA | Software | 2532.41 | area_no_valida |
| 2025-08-24 | Contabilidad | XXX-PARTIDA MALA | 16329.07 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-15 | nan | Seguros | 6390.21 | area_no_valida |
|  | Contabilidad | Viajes | 1287.26 | fecha_invalida |
| 2025-04-04 | nan | Suministros | 2639.72 | area_no_valida |
| 2025-05-19 | XXX-AREA MALA | Formacion | 9228.86 | area_no_valida |
| 2025-08-05 | Marketing | Publicidad | 10000000.00 | importe_excesivo |
| 2025-03-16 | Ventas | XXX-PARTIDA MALA | 4400.74 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-15 | Marketing | nan | 9186.09 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-10 | nan | Mantenimiento | 9322.97 | area_no_valida |
| 2025-08-02 | RRHH | Software | -500.00 | importe_invalido |
|  | RRHH | Personal | 451.46 | fecha_invalida |
| 2025-04-12 | Ventas | nan | 10870.40 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-11 | I+D | Suministros | -500.00 | importe_invalido |
| 2025-10-18 | Direccion | Seguros | 10000000.00 | importe_excesivo |
| 2025-06-11 | nan | Hardware | 1860.99 | area_no_valida |
| 2025-05-14 | IT | XXX-PARTIDA MALA | 617.56 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-26 | IT | Formacion | 10000000.00 | importe_excesivo |
| 2025-07-22 | Marketing | Publicidad | 10000000.00 | importe_excesivo |
| 2025-03-22 | nan | Viajes | 2514.85 | area_no_valida |
|  | RRHH | Mantenimiento | 12381.78 | fecha_invalida |
| 2025-01-03 | XXX-AREA MALA | Hardware | 3373.08 | area_no_valida |
| 2025-11-01 | Ventas | Personal | 10000000.00 | importe_excesivo |
| 2025-09-08 | Direccion | nan | 579.55 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-10 | Direccion | Formacion | 10000000.00 | importe_excesivo |
| 2025-04-24 | nan | Suministros | 1356.92 | area_no_valida |
| 2025-11-07 | nan | Suministros | 952.88 | area_no_valida |
| 2025-04-19 | Direccion | XXX-PARTIDA MALA | 7518.62 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-28 | nan | Formacion | 5533.64 | area_no_valida |
| 2025-09-17 | IT | nan | 1993.05 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-04 | XXX-AREA MALA | Personal | 7588.67 | area_no_valida |
| 2025-08-19 | RRHH | Alquileres | 10000000.00 | importe_excesivo |
| 2025-01-20 | XXX-AREA MALA | Software | 2560.91 | area_no_valida |
| 2025-09-30 | Direccion | Software | 10000000.00 | importe_excesivo |
| 2025-09-16 | RRHH | Publicidad | 10000000.00 | importe_excesivo |
|  | Marketing | Publicidad | 475.06 | fecha_invalida |
| 2025-03-19 | XXX-AREA MALA | Hardware | 8755.81 | area_no_valida |
| 2025-03-01 | RRHH | XXX-PARTIDA MALA | 4458.65 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-26 | IT | nan | 2116.22 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-27 | I+D | Seguros | -500.00 | importe_invalido |
| 2025-04-16 | Contabilidad | Seguros | 10000000.00 | importe_excesivo |
| 2025-02-17 | nan | Hardware | 598.45 | area_no_valida |
| 2025-04-19 | XXX-AREA MALA | Seguros | 739.67 | area_no_valida |
| 2025-04-06 | Administracion | Hardware | -500.00 | importe_invalido |
| 2025-10-02 | Operaciones | XXX-PARTIDA MALA | 6422.20 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-26 | nan | Suministros | 2737.39 | area_no_valida |
| 2025-02-22 | Administracion | nan | 3339.20 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-08 | Calidad | XXX-PARTIDA MALA | 14084.05 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-03 | Calidad | Software | -500.00 | importe_invalido |
| 2025-02-05 | Direccion | Alquileres | 10000000.00 | importe_excesivo |
| 2025-01-05 | XXX-AREA MALA | Software | 13424.66 | area_no_valida |
| 2025-02-26 | nan | Mantenimiento | 138.67 | area_no_valida |
| 2025-07-19 | RRHH | XXX-PARTIDA MALA | 15933.30 | partida_no_valida; partida_no_en_presupuesto |
|  | IT | Publicidad | 1059.14 | fecha_invalida |
| 2025-04-23 | Administracion | Viajes | -500.00 | importe_invalido |
| 2025-01-28 | RRHH | Personal | -500.00 | importe_invalido |
| 2025-04-04 | Calidad | Mantenimiento | -500.00 | importe_invalido |
| 2025-03-26 | Ventas | Suministros | 10000000.00 | importe_excesivo |
| 2025-06-22 | I+D | XXX-PARTIDA MALA | 1555.93 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-12 | I+D | XXX-PARTIDA MALA | 6130.00 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-12 | Operaciones | Seguros | -500.00 | importe_invalido |
|  | Ventas | Software | 1063.41 | fecha_invalida |
| 2025-01-11 | Administracion | nan | 1611.89 | partida_no_valida; partida_no_en_presupuesto |
|  | Operaciones | Publicidad | 9133.84 | fecha_invalida |
| 2025-03-31 | Ventas | XXX-PARTIDA MALA | 8083.18 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-18 | Operaciones | Publicidad | -500.00 | importe_invalido |
| 2025-05-24 | Contabilidad | Seguros | -500.00 | importe_invalido |
| 2025-05-01 | I+D | Software | 10000000.00 | importe_excesivo |
| 2025-06-14 | Direccion | nan | 14409.51 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-10 | RRHH | XXX-PARTIDA MALA | 1406.26 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-14 | Ventas | Formacion | -500.00 | importe_invalido |
| 2025-08-06 | RRHH | nan | 5790.98 | partida_no_valida; partida_no_en_presupuesto |
|  | RRHH | Publicidad | 6267.76 | fecha_invalida |
| 2025-11-04 | Marketing | Personal | 10000000.00 | importe_excesivo |
| 2025-10-16 | RRHH | nan | 1247.46 | partida_no_valida; partida_no_en_presupuesto |
|  | Administracion | Publicidad | 8569.52 | fecha_invalida |
| 2025-09-29 | nan | Alquileres | 6827.57 | area_no_valida |
| 2025-05-13 | Calidad | Suministros | 10000000.00 | importe_excesivo |
| 2025-06-23 | Calidad | nan | 13417.20 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-03 | Direccion | Software | -500.00 | importe_invalido |
|  | Contabilidad | Personal | 4339.29 | fecha_invalida |
|  | I+D | Viajes | 3421.85 | fecha_invalida |
| 2025-01-24 | Ventas | nan | 1270.08 | partida_no_valida; partida_no_en_presupuesto |
|  | Operaciones | Software | 5350.76 | fecha_invalida |
| 2025-05-07 | IT | Suministros | -500.00 | importe_invalido |
|  | RRHH | Mantenimiento | 8266.51 | fecha_invalida |
| 2025-03-04 | nan | Seguros | 8305.00 | area_no_valida |
| 2025-05-08 | nan | Personal | 5798.44 | area_no_valida |
| 2025-05-19 | nan | Software | 2848.95 | area_no_valida |
| 2025-02-21 | nan | Publicidad | 3444.40 | area_no_valida |
| 2025-06-06 | Contabilidad | nan | 6569.92 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-21 | RRHH | XXX-PARTIDA MALA | 723.71 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-28 | IT | Seguros | -500.00 | importe_invalido |
| 2025-06-08 | RRHH | XXX-PARTIDA MALA | 7906.63 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-22 | RRHH | Alquileres | 10000000.00 | importe_excesivo |
| 2025-06-15 | nan | Alquileres | 1277.81 | area_no_valida |
| 2025-07-27 | I+D | XXX-PARTIDA MALA | 4951.33 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-06 | XXX-AREA MALA | Seguros | 960.53 | area_no_valida |
| 2025-11-03 | nan | Software | 16111.58 | area_no_valida |
| 2025-09-06 | Calidad | XXX-PARTIDA MALA | 1101.84 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-06 | Calidad | Formacion | -500.00 | importe_invalido |
| 2025-07-14 | Contabilidad | nan | 475.42 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-26 | XXX-AREA MALA | Mantenimiento | 319.39 | area_no_valida |
| 2025-11-01 | IT | XXX-PARTIDA MALA | 7122.20 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-03 | Direccion | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-01-25 | nan | Hardware | 6516.44 | area_no_valida |
|  | Direccion | Personal | 261.83 | fecha_invalida |
| 2025-01-15 | Operaciones | nan | 3237.04 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-05 | IT | Alquileres | -500.00 | importe_invalido |
| 2025-10-11 | Ventas | Hardware | 10000000.00 | importe_excesivo |
| 2025-03-03 | nan | Suministros | 9456.59 | area_no_valida |
| 2025-09-17 | Contabilidad | XXX-PARTIDA MALA | 1613.07 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-10 | Ventas | Suministros | 10000000.00 | importe_excesivo |
| 2025-04-27 | Marketing | Suministros | 10000000.00 | importe_excesivo |
|  | RRHH | Viajes | 6390.54 | fecha_invalida |
| 2025-07-10 | I+D | XXX-PARTIDA MALA | 303.45 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-29 | nan | Viajes | 6593.11 | area_no_valida |
| 2025-11-01 | Calidad | Suministros | 10000000.00 | importe_excesivo |
| 2025-03-13 | I+D | XXX-PARTIDA MALA | 6742.05 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-24 | Direccion | XXX-PARTIDA MALA | 12832.71 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-10 | XXX-AREA MALA | Alquileres | 211.75 | area_no_valida |
| 2025-04-17 | XXX-AREA MALA | Viajes | 3068.82 | area_no_valida |
| 2025-07-30 | Operaciones | XXX-PARTIDA MALA | 497.72 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-29 | XXX-AREA MALA | Hardware | 6238.13 | area_no_valida |
| 2025-05-27 | Contabilidad | XXX-PARTIDA MALA | 5164.18 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-04 | RRHH | Mantenimiento | -500.00 | importe_invalido |
| 2025-08-04 | nan | Viajes | 16815.47 | area_no_valida |
| 2025-11-06 | I+D | nan | 6828.06 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-09 | Ventas | nan | 5412.58 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-20 | Contabilidad | Alquileres | -500.00 | importe_invalido |
| 2025-08-24 | XXX-AREA MALA | Hardware | 3777.07 | area_no_valida |
| 2025-03-03 | nan | Suministros | 5083.86 | area_no_valida |
| 2025-01-16 | nan | Mantenimiento | 2580.77 | area_no_valida |
| 2025-10-03 | Administracion | Seguros | 10000000.00 | importe_excesivo |
| 2025-08-01 | Marketing | Publicidad | 10000000.00 | importe_excesivo |
| 2025-06-17 | Administracion | Mantenimiento | -500.00 | importe_invalido |
| 2025-04-08 | I+D | Mantenimiento | -500.00 | importe_invalido |
| 2025-07-31 | RRHH | XXX-PARTIDA MALA | 13694.07 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-01 | Operaciones | nan | 1419.02 | partida_no_valida; partida_no_en_presupuesto |
|  | RRHH | Formacion | 2301.89 | fecha_invalida |
| 2025-03-04 | I+D | Suministros | -500.00 | importe_invalido |
| 2025-05-07 | Direccion | Viajes | 10000000.00 | importe_excesivo |
| 2025-04-05 | Direccion | Formacion | -500.00 | importe_invalido |
| 2025-07-01 | Operaciones | Personal | 10000000.00 | importe_excesivo |
| 2025-03-31 | nan | Alquileres | 2064.96 | area_no_valida |
|  | I+D | Software | 6593.61 | fecha_invalida |
| 2025-02-28 | nan | Formacion | 2642.82 | area_no_valida |
| 2025-02-14 | Direccion | XXX-PARTIDA MALA | 876.00 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-31 | XXX-AREA MALA | Publicidad | 749.65 | area_no_valida |
| 2025-08-22 | nan | Alquileres | 3476.83 | area_no_valida |
| 2025-02-11 | XXX-AREA MALA | Formacion | 10509.28 | area_no_valida |
| 2025-09-05 | nan | Alquileres | 8101.01 | area_no_valida |
| 2025-03-23 | Contabilidad | XXX-PARTIDA MALA | 4647.30 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-17 | Contabilidad | XXX-PARTIDA MALA | 2579.34 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-29 | I+D | Suministros | -500.00 | importe_invalido |
| 2025-05-15 | Contabilidad | nan | 2398.41 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-20 | RRHH | XXX-PARTIDA MALA | 776.61 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-26 | Operaciones | Formacion | -500.00 | importe_invalido |
| 2025-09-01 | Ventas | Suministros | -500.00 | importe_invalido |
| 2025-02-06 | Ventas | nan | 5682.74 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-05 | nan | Alquileres | 10483.37 | area_no_valida |
| 2025-05-30 | nan | Formacion | 3458.01 | area_no_valida |
| 2025-09-05 | XXX-AREA MALA | Personal | 1101.32 | area_no_valida |
| 2025-02-23 | Ventas | Seguros | -500.00 | importe_invalido |
| 2025-03-25 | Ventas | Mantenimiento | 10000000.00 | importe_excesivo |
|  | Direccion | Mantenimiento | 15821.25 | fecha_invalida |
| 2025-06-28 | nan | Seguros | 684.20 | area_no_valida |
| 2025-05-29 | Ventas | Publicidad | 10000000.00 | importe_excesivo |
| 2025-03-23 | XXX-AREA MALA | Publicidad | 1132.43 | area_no_valida |
| 2025-01-02 | Direccion | XXX-PARTIDA MALA | 701.06 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-11 | XXX-AREA MALA | Personal | 970.82 | area_no_valida |
| 2025-08-10 | IT | Publicidad | 10000000.00 | importe_excesivo |
| 2025-10-11 | XXX-AREA MALA | Viajes | 4637.01 | area_no_valida |
| 2025-05-22 | nan | Alquileres | 1602.97 | area_no_valida |
|  | I+D | Seguros | 4685.08 | fecha_invalida |
| 2025-09-20 | Ventas | Alquileres | -500.00 | importe_invalido |
