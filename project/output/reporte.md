# Informe de Ejecución Presupuestaria
_Generado: 2025-11-12 02:06_
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
| Administracion | 781602.00 | 3033503.69 | 388.0% |
| Calidad | 1460173.00 | 5726235.32 | 392.0% |
| Contabilidad | 1284139.00 | 5186073.45 | 404.0% |
| Direccion | 1293832.00 | 5132057.15 | 397.0% |
| I+D | 960874.00 | 3852292.14 | 401.0% |
| IT | 1217621.00 | 4841711.50 | 398.0% |
| Marketing | 1166976.00 | 4380899.15 | 375.0% |
| Operaciones | 716943.00 | 2958665.12 | 413.0% |
| RRHH | 1016457.00 | 4318076.34 | 425.0% |
| Ventas | 1172169.00 | 4507264.76 | 385.0% |

## 4. Ejecución por área y partida
| Área | Partida | Presupuesto | Gasto acumulado | KPI |
|------|---------|-------------|-----------------|-----|
| Administracion | Alquileres | 57247.00 | 286607.66 | 501.0% |
| Administracion | Formacion | 149888.00 | 575901.89 | 384.0% |
| Administracion | Hardware | 50737.00 | 190367.92 | 375.0% |
| Administracion | Mantenimiento | 46566.00 | 212844.41 | 457.0% |
| Administracion | Personal | 45973.00 | 164255.03 | 357.0% |
| Administracion | Publicidad | 146194.00 | 494978.97 | 339.0% |
| Administracion | Seguros | 33366.00 | 178921.41 | 536.0% |
| Administracion | Software | 56283.00 | 214795.35 | 382.0% |
| Administracion | Suministros | 90208.00 | 302058.95 | 335.0% |
| Administracion | Viajes | 105140.00 | 412772.10 | 393.0% |
| Calidad | Alquileres | 83919.00 | 329874.70 | 393.0% |
| Calidad | Formacion | 167848.00 | 722370.51 | 430.0% |
| Calidad | Hardware | 116536.00 | 459807.42 | 395.0% |
| Calidad | Mantenimiento | 180837.00 | 699249.64 | 387.0% |
| Calidad | Personal | 159893.00 | 542391.12 | 339.0% |
| Calidad | Publicidad | 167892.00 | 568948.00 | 339.0% |
| Calidad | Seguros | 195834.00 | 838862.32 | 428.0% |
| Calidad | Software | 173857.00 | 750597.91 | 432.0% |
| Calidad | Suministros | 86844.00 | 344025.79 | 396.0% |
| Calidad | Viajes | 126713.00 | 470107.91 | 371.0% |
| Contabilidad | Alquileres | 143516.00 | 608596.91 | 424.0% |
| Contabilidad | Formacion | 17978.00 | 76551.95 | 426.0% |
| Contabilidad | Hardware | 154547.00 | 639705.72 | 414.0% |
| Contabilidad | Mantenimiento | 89781.00 | 332609.99 | 370.0% |
| Contabilidad | Personal | 191999.00 | 826871.44 | 431.0% |
| Contabilidad | Publicidad | 110289.00 | 440299.22 | 399.0% |
| Contabilidad | Seguros | 146187.00 | 645184.80 | 441.0% |
| Contabilidad | Software | 175931.00 | 752039.73 | 427.0% |
| Contabilidad | Suministros | 135139.00 | 467709.87 | 346.0% |
| Contabilidad | Viajes | 118772.00 | 396503.82 | 334.0% |
| Direccion | Alquileres | 107922.00 | 419277.82 | 389.0% |
| Direccion | Formacion | 55362.00 | 225203.38 | 407.0% |
| Direccion | Hardware | 166426.00 | 687285.88 | 413.0% |
| Direccion | Mantenimiento | 74553.00 | 283602.32 | 380.0% |
| Direccion | Personal | 131228.00 | 379716.58 | 289.0% |
| Direccion | Publicidad | 138796.00 | 569805.04 | 411.0% |
| Direccion | Seguros | 64544.00 | 270059.46 | 418.0% |
| Direccion | Software | 167545.00 | 750993.58 | 448.0% |
| Direccion | Suministros | 189752.00 | 731135.52 | 385.0% |
| Direccion | Viajes | 197704.00 | 814977.57 | 412.0% |
| I+D | Alquileres | 167998.00 | 763124.14 | 454.0% |
| I+D | Formacion | 145342.00 | 594106.25 | 409.0% |
| I+D | Hardware | 90495.00 | 403514.10 | 446.0% |
| I+D | Mantenimiento | 16065.00 | 76311.11 | 475.0% |
| I+D | Personal | 129840.00 | 399423.23 | 308.0% |
| I+D | Publicidad | 82842.00 | 383080.70 | 462.0% |
| I+D | Seguros | 38692.00 | 144735.49 | 374.0% |
| I+D | Software | 40557.00 | 121714.96 | 300.0% |
| I+D | Suministros | 105422.00 | 423940.48 | 402.0% |
| I+D | Viajes | 143621.00 | 542341.68 | 378.0% |
| IT | Alquileres | 103554.00 | 381663.57 | 369.0% |
| IT | Formacion | 133393.00 | 512301.31 | 384.0% |
| IT | Hardware | 57317.00 | 226291.00 | 395.0% |
| IT | Mantenimiento | 113179.00 | 396515.00 | 350.0% |
| IT | Personal | 178918.00 | 746782.50 | 417.0% |
| IT | Publicidad | 85565.00 | 389435.03 | 455.0% |
| IT | Seguros | 143234.00 | 630448.06 | 440.0% |
| IT | Software | 192146.00 | 684586.16 | 356.0% |
| IT | Suministros | 72253.00 | 331360.65 | 459.0% |
| IT | Viajes | 138062.00 | 542328.22 | 393.0% |
| Marketing | Alquileres | 183127.00 | 751768.09 | 411.0% |
| Marketing | Formacion | 99078.00 | 375550.99 | 379.0% |
| Marketing | Hardware | 10493.00 | 35053.58 | 334.0% |
| Marketing | Mantenimiento | 169984.00 | 598361.42 | 352.0% |
| Marketing | Personal | 187480.00 | 584569.70 | 312.0% |
| Marketing | Publicidad | 45057.00 | 197420.71 | 438.0% |
| Marketing | Seguros | 95576.00 | 308778.47 | 323.0% |
| Marketing | Software | 184292.00 | 733973.45 | 398.0% |
| Marketing | Suministros | 91677.00 | 362203.28 | 395.0% |
| Marketing | Viajes | 100212.00 | 433219.46 | 432.0% |
| Operaciones | Alquileres | 12789.00 | 56451.65 | 441.0% |
| Operaciones | Formacion | 24333.00 | 92230.38 | 379.0% |
| Operaciones | Hardware | 37811.00 | 158882.70 | 420.0% |
| Operaciones | Mantenimiento | 90155.00 | 338235.20 | 375.0% |
| Operaciones | Personal | 66653.00 | 309840.83 | 465.0% |
| Operaciones | Publicidad | 80684.00 | 371944.60 | 461.0% |
| Operaciones | Seguros | 90538.00 | 298606.21 | 330.0% |
| Operaciones | Software | 81913.00 | 302182.26 | 369.0% |
| Operaciones | Suministros | 86797.00 | 450823.01 | 519.0% |
| Operaciones | Viajes | 145270.00 | 579468.28 | 399.0% |
| RRHH | Alquileres | 84328.00 | 371301.21 | 440.0% |
| RRHH | Formacion | 23300.00 | 79096.11 | 339.0% |
| RRHH | Hardware | 157838.00 | 688669.55 | 436.0% |
| RRHH | Mantenimiento | 153001.00 | 468989.83 | 307.0% |
| RRHH | Personal | 12089.00 | 52769.12 | 437.0% |
| RRHH | Publicidad | 14169.00 | 58922.60 | 416.0% |
| RRHH | Seguros | 146950.00 | 673936.45 | 459.0% |
| RRHH | Software | 38102.00 | 173084.73 | 454.0% |
| RRHH | Suministros | 188371.00 | 824594.53 | 438.0% |
| RRHH | Viajes | 198309.00 | 926712.21 | 467.0% |
| Ventas | Alquileres | 22894.00 | 81170.39 | 355.0% |
| Ventas | Formacion | 169718.00 | 538639.52 | 317.0% |
| Ventas | Hardware | 113008.00 | 381800.90 | 338.0% |
| Ventas | Mantenimiento | 160039.00 | 664178.87 | 415.0% |
| Ventas | Personal | 75779.00 | 277783.44 | 367.0% |
| Ventas | Publicidad | 138380.00 | 587738.95 | 425.0% |
| Ventas | Seguros | 199533.00 | 743164.89 | 372.0% |
| Ventas | Software | 91987.00 | 330906.46 | 360.0% |
| Ventas | Suministros | 54698.00 | 196512.42 | 359.0% |
| Ventas | Viajes | 146133.00 | 705368.92 | 483.0% |

## 5. Tendencia mensual de gasto (por área)
| Mes | Área | Gasto mensual |
|-----|------|----------------|
| 2025-01 | Administracion | 287101.52 |
| 2025-01 | Calidad | 584902.78 |
| 2025-01 | Contabilidad | 568395.74 |
| 2025-01 | Direccion | 502000.33 |
| 2025-01 | I+D | 324464.22 |
| 2025-01 | IT | 528687.66 |
| 2025-01 | Marketing | 392053.87 |
| 2025-01 | Operaciones | 263111.59 |
| 2025-01 | RRHH | 401990.47 |
| 2025-01 | Ventas | 542372.01 |
| 2025-02 | Administracion | 290186.59 |
| 2025-02 | Calidad | 389247.24 |
| 2025-02 | Contabilidad | 390382.96 |
| 2025-02 | Direccion | 395755.06 |
| 2025-02 | I+D | 284925.09 |
| 2025-02 | IT | 316702.57 |
| 2025-02 | Marketing | 317080.52 |
| 2025-02 | Operaciones | 305531.47 |
| 2025-02 | RRHH | 455773.16 |
| 2025-02 | Ventas | 327900.13 |
| 2025-03 | Administracion | 289704.57 |
| 2025-03 | Calidad | 557977.22 |
| 2025-03 | Contabilidad | 429134.26 |
| 2025-03 | Direccion | 551142.82 |
| 2025-03 | I+D | 399504.51 |
| 2025-03 | IT | 472161.10 |
| 2025-03 | Marketing | 423049.86 |
| 2025-03 | Operaciones | 235883.08 |
| 2025-03 | RRHH | 427345.90 |
| 2025-03 | Ventas | 500672.97 |
| 2025-04 | Administracion | 301354.40 |
| 2025-04 | Calidad | 518854.90 |
| 2025-04 | Contabilidad | 431171.92 |
| 2025-04 | Direccion | 585096.73 |
| 2025-04 | I+D | 388470.81 |
| 2025-04 | IT | 450897.52 |
| 2025-04 | Marketing | 398159.81 |
| 2025-04 | Operaciones | 305281.59 |
| 2025-04 | RRHH | 349425.50 |
| 2025-04 | Ventas | 451098.73 |
| 2025-05 | Administracion | 292909.92 |
| 2025-05 | Calidad | 539058.93 |
| 2025-05 | Contabilidad | 468880.25 |
| 2025-05 | Direccion | 484609.20 |
| 2025-05 | I+D | 361705.64 |
| 2025-05 | IT | 522984.94 |
| 2025-05 | Marketing | 399768.96 |
| 2025-05 | Operaciones | 290490.78 |
| 2025-05 | RRHH | 385256.40 |
| 2025-05 | Ventas | 479255.07 |
| 2025-06 | Administracion | 291147.86 |
| 2025-06 | Calidad | 531700.82 |
| 2025-06 | Contabilidad | 526481.92 |
| 2025-06 | Direccion | 569912.18 |
| 2025-06 | I+D | 387885.29 |
| 2025-06 | IT | 515350.57 |
| 2025-06 | Marketing | 478642.30 |
| 2025-06 | Operaciones | 251383.42 |
| 2025-06 | RRHH | 346024.08 |
| 2025-06 | Ventas | 411979.20 |
| 2025-07 | Administracion | 291894.86 |
| 2025-07 | Calidad | 619817.17 |
| 2025-07 | Contabilidad | 522645.36 |
| 2025-07 | Direccion | 401551.80 |
| 2025-07 | I+D | 399156.27 |
| 2025-07 | IT | 443615.45 |
| 2025-07 | Marketing | 438821.89 |
| 2025-07 | Operaciones | 328967.62 |
| 2025-07 | RRHH | 532520.64 |
| 2025-07 | Ventas | 452760.04 |
| 2025-08 | Administracion | 293043.97 |
| 2025-08 | Calidad | 577833.96 |
| 2025-08 | Contabilidad | 551887.35 |
| 2025-08 | Direccion | 504524.41 |
| 2025-08 | I+D | 406182.10 |
| 2025-08 | IT | 479211.34 |
| 2025-08 | Marketing | 445692.53 |
| 2025-08 | Operaciones | 336078.54 |
| 2025-08 | RRHH | 423947.73 |
| 2025-08 | Ventas | 481354.08 |
| 2025-09 | Administracion | 293940.13 |
| 2025-09 | Calidad | 588624.49 |
| 2025-09 | Contabilidad | 478027.57 |
| 2025-09 | Direccion | 496485.54 |
| 2025-09 | I+D | 383315.29 |
| 2025-09 | IT | 425196.60 |
| 2025-09 | Marketing | 430909.95 |
| 2025-09 | Operaciones | 262425.83 |
| 2025-09 | RRHH | 441697.14 |
| 2025-09 | Ventas | 369721.60 |
| 2025-10 | Administracion | 287721.89 |
| 2025-10 | Calidad | 544836.94 |
| 2025-10 | Contabilidad | 592326.73 |
| 2025-10 | Direccion | 506487.50 |
| 2025-10 | I+D | 391593.55 |
| 2025-10 | IT | 475259.83 |
| 2025-10 | Marketing | 381081.31 |
| 2025-10 | Operaciones | 294622.64 |
| 2025-10 | RRHH | 446925.83 |
| 2025-10 | Ventas | 366655.46 |
| 2025-11 | Administracion | 114497.98 |
| 2025-11 | Calidad | 273380.87 |
| 2025-11 | Contabilidad | 226739.39 |
| 2025-11 | Direccion | 134491.58 |
| 2025-11 | I+D | 125089.37 |
| 2025-11 | IT | 211643.92 |
| 2025-11 | Marketing | 275638.15 |
| 2025-11 | Operaciones | 84888.56 |
| 2025-11 | RRHH | 107169.49 |
| 2025-11 | Ventas | 123495.47 |

## 6. Filas en cuarentena (gastos descartados)
| fecha | area | partida | importe | causa |
|-------|------|---------|---------|--------|
|  | Marketing | Software | 14697.46 | fecha_invalida |
| 2025-02-02 | Direccion | nan | 6068.82 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-17 | IT | nan | 6116.36 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-15 | Calidad | Viajes | 10000000.00 | importe_excesivo |
| 2025-03-04 | Administracion | Alquileres | 10000000.00 | importe_excesivo |
| 2025-08-29 | Calidad | nan | 4125.11 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-22 | XXX-AREA MALA | Publicidad | 4067.95 | area_no_valida |
| 2025-08-30 | Administracion | nan | 1595.38 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-23 | RRHH | nan | 2476.91 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-08 | IT | nan | 8584.28 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-19 | Calidad | Software | 10000000.00 | importe_excesivo |
| 2025-09-14 | Marketing | Suministros | 10000000.00 | importe_excesivo |
| 2025-05-06 | Calidad | Software | -500.00 | importe_invalido |
| 2025-09-26 | nan | Seguros | 4236.62 | area_no_valida |
|  | Marketing | Mantenimiento | 11186.57 | fecha_invalida |
| 2025-06-06 | Operaciones | nan | 5759.42 | partida_no_valida; partida_no_en_presupuesto |
|  | I+D | Mantenimiento | 1234.37 | fecha_invalida |
| 2025-03-25 | nan | Suministros | 3292.31 | area_no_valida |
|  | Direccion | Hardware | 6286.18 | fecha_invalida |
| 2025-06-28 | IT | Software | 10000000.00 | importe_excesivo |
| 2025-04-06 | Direccion | Viajes | 10000000.00 | importe_excesivo |
| 2025-11-03 | XXX-AREA MALA | Suministros | 3204.15 | area_no_valida |
| 2025-09-24 | Direccion | XXX-PARTIDA MALA | 2483.21 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-18 | I+D | nan | 1020.89 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-03 | nan | Publicidad | 2698.45 | area_no_valida |
|  | IT | Alquileres | 7930.77 | fecha_invalida |
|  | Contabilidad | Personal | 9102.98 | fecha_invalida |
|  | IT | Hardware | 633.23 | fecha_invalida |
| 2025-05-25 | IT | nan | 8393.11 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-24 | nan | Alquileres | 2807.63 | area_no_valida |
| 2025-10-06 | XXX-AREA MALA | Publicidad | 6430.43 | area_no_valida |
| 2025-04-10 | Calidad | nan | 16214.96 | partida_no_valida; partida_no_en_presupuesto |
|  | RRHH | Hardware | 2644.57 | fecha_invalida |
| 2025-10-21 | Ventas | XXX-PARTIDA MALA | 8615.66 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-13 | nan | Seguros | 10946.94 | area_no_valida |
| 2025-07-13 | nan | Seguros | 8676.44 | area_no_valida |
| 2025-03-27 | Contabilidad | XXX-PARTIDA MALA | 11842.20 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-04 | Contabilidad | Viajes | 10000000.00 | importe_excesivo |
| 2025-06-21 | Operaciones | nan | 1439.35 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-12 | Marketing | XXX-PARTIDA MALA | 1971.25 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-22 | XXX-AREA MALA | Hardware | 454.04 | area_no_valida |
|  | IT | Suministros | 418.31 | fecha_invalida |
| 2025-09-23 | nan | Viajes | 10236.69 | area_no_valida |
| 2025-06-20 | Contabilidad | Hardware | 10000000.00 | importe_excesivo |
| 2025-06-25 | Marketing | Personal | -500.00 | importe_invalido |
| 2025-10-04 | Contabilidad | nan | 10852.70 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-09 | Ventas | XXX-PARTIDA MALA | 1823.31 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-25 | IT | XXX-PARTIDA MALA | 375.76 | partida_no_valida; partida_no_en_presupuesto |
|  | Operaciones | Mantenimiento | 7225.55 | fecha_invalida |
| 2025-09-21 | Ventas | nan | 10330.75 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-12 | nan | Seguros | 7539.94 | area_no_valida |
| 2025-10-16 | Calidad | nan | 15913.92 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-11 | I+D | XXX-PARTIDA MALA | 2295.02 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-30 | Operaciones | Hardware | -500.00 | importe_invalido |
| 2025-09-21 | Operaciones | Seguros | 10000000.00 | importe_excesivo |
| 2025-07-23 | XXX-AREA MALA | Formacion | 3362.53 | area_no_valida |
| 2025-10-16 | RRHH | nan | 216.12 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-26 | nan | Alquileres | 4277.33 | area_no_valida |
| 2025-03-25 | Direccion | XXX-PARTIDA MALA | 17105.05 | partida_no_valida; partida_no_en_presupuesto |
|  | Ventas | Alquileres | 330.64 | fecha_invalida |
| 2025-03-30 | IT | Alquileres | -500.00 | importe_invalido |
| 2025-10-26 | Direccion | XXX-PARTIDA MALA | 176.24 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-10 | XXX-AREA MALA | Personal | 855.82 | area_no_valida |
| 2025-01-15 | I+D | nan | 6392.14 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-14 | Administracion | nan | 3033.62 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-27 | IT | Seguros | 10000000.00 | importe_excesivo |
| 2025-04-15 | XXX-AREA MALA | Mantenimiento | 1255.28 | area_no_valida |
| 2025-08-05 | Direccion | Suministros | 10000000.00 | importe_excesivo |
| 2025-06-29 | Ventas | Formacion | 10000000.00 | importe_excesivo |
| 2025-06-20 | I+D | Suministros | -500.00 | importe_invalido |
| 2025-07-10 | Operaciones | XXX-PARTIDA MALA | 5508.52 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-16 | XXX-AREA MALA | Formacion | 2051.18 | area_no_valida |
| 2025-05-22 | RRHH | nan | 13931.97 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-13 | Ventas | XXX-PARTIDA MALA | 1026.17 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-31 | Ventas | Viajes | 10000000.00 | importe_excesivo |
| 2025-06-13 | Direccion | Seguros | 10000000.00 | importe_excesivo |
| 2025-10-12 | Marketing | Publicidad | -500.00 | importe_invalido |
| 2025-05-09 | XXX-AREA MALA | Seguros | 9279.05 | area_no_valida |
| 2025-08-07 | XXX-AREA MALA | Hardware | 5047.88 | area_no_valida |
|  | Contabilidad | Hardware | 4785.27 | fecha_invalida |
| 2025-08-09 | XXX-AREA MALA | Hardware | 4636.89 | area_no_valida |
|  | I+D | Software | 2726.07 | fecha_invalida |
| 2025-05-04 | Ventas | Seguros | 10000000.00 | importe_excesivo |
| 2025-09-19 | Operaciones | nan | 562.89 | partida_no_valida; partida_no_en_presupuesto |
|  | Ventas | Publicidad | 13426.28 | fecha_invalida |
| 2025-05-10 | Ventas | XXX-PARTIDA MALA | 9841.76 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-17 | I+D | Alquileres | 10000000.00 | importe_excesivo |
| 2025-10-07 | nan | Mantenimiento | 13703.99 | area_no_valida |
| 2025-02-23 | Marketing | Seguros | -500.00 | importe_invalido |
| 2025-02-27 | Marketing | nan | 3632.84 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-06 | I+D | Hardware | 10000000.00 | importe_excesivo |
| 2025-04-10 | Operaciones | nan | 7710.70 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-22 | Contabilidad | Alquileres | -500.00 | importe_invalido |
| 2025-09-08 | Operaciones | XXX-PARTIDA MALA | 1044.59 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-03 | Marketing | XXX-PARTIDA MALA | 541.31 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-30 | Operaciones | Hardware | -500.00 | importe_invalido |
| 2025-04-17 | RRHH | XXX-PARTIDA MALA | 1357.38 | partida_no_valida; partida_no_en_presupuesto |
|  | Contabilidad | Mantenimiento | 7707.93 | fecha_invalida |
| 2025-08-05 | Operaciones | nan | 5520.61 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-23 | XXX-AREA MALA | Publicidad | 1227.35 | area_no_valida |
| 2025-08-25 | XXX-AREA MALA | Alquileres | 1719.88 | area_no_valida |
| 2025-10-28 | Administracion | XXX-PARTIDA MALA | 2613.20 | partida_no_valida; partida_no_en_presupuesto |
|  | RRHH | Publicidad | 1132.42 | fecha_invalida |
| 2025-03-24 | nan | Formacion | 5227.72 | area_no_valida |
| 2025-08-21 | Marketing | Hardware | 10000000.00 | importe_excesivo |
| 2025-10-24 | IT | nan | 7853.31 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-06 | nan | Seguros | 18497.79 | area_no_valida |
| 2025-01-17 | nan | Suministros | 734.51 | area_no_valida |
| 2025-08-26 | Operaciones | Publicidad | 10000000.00 | importe_excesivo |
| 2025-05-30 | Contabilidad | XXX-PARTIDA MALA | 7138.23 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-20 | Calidad | XXX-PARTIDA MALA | 2356.91 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-15 | Ventas | XXX-PARTIDA MALA | 3202.43 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-19 | Direccion | Viajes | -500.00 | importe_invalido |
| 2025-05-17 | Operaciones | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-03-20 | nan | Personal | 11609.50 | area_no_valida |
| 2025-05-21 | Operaciones | nan | 6306.22 | partida_no_valida; partida_no_en_presupuesto |
|  | Administracion | Seguros | 3148.21 | fecha_invalida |
| 2025-07-18 | XXX-AREA MALA | Publicidad | 7039.55 | area_no_valida |
| 2025-07-18 | Contabilidad | Seguros | -500.00 | importe_invalido |
| 2025-04-02 | Calidad | Alquileres | 10000000.00 | importe_excesivo |
| 2025-04-13 | XXX-AREA MALA | Viajes | 12627.45 | area_no_valida |
| 2025-02-23 | Contabilidad | Mantenimiento | -500.00 | importe_invalido |
| 2025-06-25 | IT | XXX-PARTIDA MALA | 4305.76 | partida_no_valida; partida_no_en_presupuesto |
|  | IT | Seguros | 10922.55 | fecha_invalida |
| 2025-02-07 | XXX-AREA MALA | Publicidad | 4986.21 | area_no_valida |
|  | Calidad | Personal | 14063.79 | fecha_invalida |
|  | Ventas | Alquileres | 1699.06 | fecha_invalida |
| 2025-02-02 | IT | nan | 3237.39 | partida_no_valida; partida_no_en_presupuesto |
|  | Ventas | Suministros | 3969.66 | fecha_invalida |
| 2025-01-23 | Calidad | Mantenimiento | -500.00 | importe_invalido |
|  | Contabilidad | Software | 1527.77 | fecha_invalida |
|  | Ventas | Hardware | 1828.95 | fecha_invalida |
| 2025-03-13 | XXX-AREA MALA | Formacion | 3884.71 | area_no_valida |
| 2025-07-31 | IT | Formacion | 10000000.00 | importe_excesivo |
| 2025-03-04 | nan | Publicidad | 6072.70 | area_no_valida |
| 2025-03-10 | IT | XXX-PARTIDA MALA | 7765.02 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-15 | nan | Alquileres | 6116.43 | area_no_valida |
| 2025-07-18 | Ventas | Personal | 10000000.00 | importe_excesivo |
| 2025-01-14 | Ventas | Hardware | 10000000.00 | importe_excesivo |
| 2025-01-26 | Marketing | nan | 5349.34 | partida_no_valida; partida_no_en_presupuesto |
|  | Calidad | Seguros | 5343.49 | fecha_invalida |
|  | Ventas | Viajes | 14316.99 | fecha_invalida |
|  | RRHH | Seguros | 3840.10 | fecha_invalida |
| 2025-06-12 | RRHH | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-03-01 | Ventas | nan | 6984.67 | partida_no_valida; partida_no_en_presupuesto |
|  | Calidad | Software | 15024.96 | fecha_invalida |
| 2025-08-12 | nan | Software | 2245.79 | area_no_valida |
| 2025-01-10 | I+D | Alquileres | 10000000.00 | importe_excesivo |
| 2025-06-08 | Marketing | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-08-03 | nan | Publicidad | 3568.44 | area_no_valida |
| 2025-01-28 | Marketing | Software | 10000000.00 | importe_excesivo |
| 2025-10-24 | nan | Suministros | 5399.78 | area_no_valida |
| 2025-08-07 | Direccion | XXX-PARTIDA MALA | 354.49 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-02 | nan | Publicidad | 1294.83 | area_no_valida |
| 2025-01-15 | RRHH | nan | 6317.76 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-24 | Contabilidad | Seguros | -500.00 | importe_invalido |
| 2025-11-09 | Calidad | nan | 12819.45 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-07 | Operaciones | nan | 1913.11 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-21 | Marketing | Seguros | 10000000.00 | importe_excesivo |
| 2025-09-13 | IT | Mantenimiento | -500.00 | importe_invalido |
| 2025-07-21 | IT | Publicidad | -500.00 | importe_invalido |
| 2025-08-18 | XXX-AREA MALA | Viajes | 5963.75 | area_no_valida |
| 2025-08-29 | Direccion | nan | 13856.09 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-26 | Marketing | XXX-PARTIDA MALA | 4198.22 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-11 | Contabilidad | nan | 9464.55 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-18 | RRHH | Personal | -500.00 | importe_invalido |
| 2025-04-09 | XXX-AREA MALA | Personal | 7951.56 | area_no_valida |
| 2025-06-09 | IT | XXX-PARTIDA MALA | 10675.30 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-15 | Operaciones | Alquileres | 10000000.00 | importe_excesivo |
| 2025-05-23 | Contabilidad | nan | 853.33 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-27 | XXX-AREA MALA | Seguros | 2932.49 | area_no_valida |
|  | Calidad | Suministros | 8134.63 | fecha_invalida |
| 2025-04-03 | RRHH | Viajes | 10000000.00 | importe_excesivo |
|  | Marketing | Alquileres | 15826.50 | fecha_invalida |
| 2025-08-30 | IT | Formacion | -500.00 | importe_invalido |
| 2025-09-17 | XXX-AREA MALA | Mantenimiento | 7757.14 | area_no_valida |
| 2025-07-30 | XXX-AREA MALA | Suministros | 1663.25 | area_no_valida |
|  | Administracion | Formacion | 4346.84 | fecha_invalida |
| 2025-07-23 | nan | Hardware | 3647.12 | area_no_valida |
| 2025-07-18 | RRHH | XXX-PARTIDA MALA | 2646.53 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-17 | I+D | XXX-PARTIDA MALA | 16142.60 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-04 | nan | Alquileres | 3578.07 | area_no_valida |
| 2025-06-19 | Administracion | Personal | 10000000.00 | importe_excesivo |
| 2025-09-09 | IT | Suministros | -500.00 | importe_invalido |
| 2025-01-02 | XXX-AREA MALA | Publicidad | 9100.54 | area_no_valida |
| 2025-03-23 | nan | Suministros | 15931.64 | area_no_valida |
|  | Contabilidad | Seguros | 7925.58 | fecha_invalida |
| 2025-01-09 | Operaciones | XXX-PARTIDA MALA | 7625.06 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-22 | RRHH | XXX-PARTIDA MALA | 898.73 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-27 | Administracion | nan | 2058.23 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-02 | Calidad | XXX-PARTIDA MALA | 1647.78 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-12 | XXX-AREA MALA | Personal | 3964.39 | area_no_valida |
| 2025-04-24 | Ventas | Viajes | 10000000.00 | importe_excesivo |
| 2025-02-14 | Marketing | Personal | -500.00 | importe_invalido |
| 2025-05-01 | XXX-AREA MALA | Mantenimiento | 1229.64 | area_no_valida |
| 2025-06-19 | XXX-AREA MALA | Suministros | 131.53 | area_no_valida |
| 2025-05-21 | RRHH | Software | 10000000.00 | importe_excesivo |
| 2025-08-15 | Administracion | XXX-PARTIDA MALA | 2624.14 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-06 | Ventas | Mantenimiento | -500.00 | importe_invalido |
| 2025-06-12 | RRHH | nan | 9936.21 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-14 | XXX-AREA MALA | Alquileres | 953.51 | area_no_valida |
| 2025-07-12 | IT | Hardware | 10000000.00 | importe_excesivo |
| 2025-08-31 | nan | Publicidad | 14359.40 | area_no_valida |
| 2025-06-14 | nan | Publicidad | 183.47 | area_no_valida |
|  | Operaciones | Suministros | 405.48 | fecha_invalida |
| 2025-10-21 | Ventas | Publicidad | 10000000.00 | importe_excesivo |
| 2025-08-25 | XXX-AREA MALA | Hardware | 12935.96 | area_no_valida |
| 2025-01-17 | IT | Mantenimiento | -500.00 | importe_invalido |
|  | Direccion | Formacion | 987.43 | fecha_invalida |
| 2025-05-09 | XXX-AREA MALA | Personal | 2243.38 | area_no_valida |
| 2025-04-20 | XXX-AREA MALA | Publicidad | 2926.25 | area_no_valida |
| 2025-04-28 | nan | Formacion | 11226.16 | area_no_valida |
| 2025-06-17 | Administracion | XXX-PARTIDA MALA | 5897.36 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-20 | XXX-AREA MALA | Publicidad | 12469.48 | area_no_valida |
| 2025-10-13 | IT | Suministros | -500.00 | importe_invalido |
|  | Direccion | Hardware | 3027.02 | fecha_invalida |
| 2025-07-22 | nan | Alquileres | 8654.25 | area_no_valida |
| 2025-02-25 | XXX-AREA MALA | Hardware | 1859.61 | area_no_valida |
|  | Contabilidad | Suministros | 8885.70 | fecha_invalida |
| 2025-08-04 | XXX-AREA MALA | Software | 1101.31 | area_no_valida |
| 2025-04-02 | Ventas | Viajes | -500.00 | importe_invalido |
| 2025-01-07 | XXX-AREA MALA | Suministros | 6274.88 | area_no_valida |
| 2025-07-31 | RRHH | XXX-PARTIDA MALA | 8075.67 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-11 | Ventas | nan | 3875.13 | partida_no_valida; partida_no_en_presupuesto |
|  | Operaciones | Publicidad | 2429.12 | fecha_invalida |
| 2025-04-13 | nan | Mantenimiento | 1412.69 | area_no_valida |
| 2025-02-20 | Direccion | nan | 18355.64 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-28 | XXX-AREA MALA | Mantenimiento | 14694.27 | area_no_valida |
| 2025-09-20 | I+D | XXX-PARTIDA MALA | 368.86 | partida_no_valida; partida_no_en_presupuesto |
|  | Administracion | Hardware | 3915.18 | fecha_invalida |
| 2025-05-30 | XXX-AREA MALA | Viajes | 15712.11 | area_no_valida |
| 2025-09-02 | RRHH | Viajes | 10000000.00 | importe_excesivo |
| 2025-10-01 | Direccion | Seguros | -500.00 | importe_invalido |
| 2025-04-12 | Contabilidad | nan | 209.53 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-31 | RRHH | XXX-PARTIDA MALA | 4957.86 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-24 | nan | Formacion | 428.86 | area_no_valida |
|  | I+D | Hardware | 3000.45 | fecha_invalida |
| 2025-08-05 | Administracion | Hardware | -500.00 | importe_invalido |
|  | IT | Suministros | 5100.09 | fecha_invalida |
| 2025-11-05 | Ventas | nan | 2161.17 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-06 | nan | Alquileres | 1810.67 | area_no_valida |
| 2025-02-23 | I+D | XXX-PARTIDA MALA | 2377.41 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-02 | I+D | Alquileres | 10000000.00 | importe_excesivo |
| 2025-05-30 | XXX-AREA MALA | Hardware | 664.03 | area_no_valida |
| 2025-08-12 | Calidad | nan | 3063.32 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-14 | XXX-AREA MALA | Seguros | 3808.30 | area_no_valida |
|  | Direccion | Hardware | 5037.15 | fecha_invalida |
| 2025-01-31 | XXX-AREA MALA | Viajes | 9472.11 | area_no_valida |
| 2025-01-08 | Contabilidad | Formacion | -500.00 | importe_invalido |
| 2025-08-08 | Direccion | XXX-PARTIDA MALA | 8947.35 | partida_no_valida; partida_no_en_presupuesto |
|  | I+D | Formacion | 616.24 | fecha_invalida |
| 2025-09-27 | Calidad | nan | 6658.11 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-25 | XXX-AREA MALA | Formacion | 8822.05 | area_no_valida |
| 2025-05-09 | nan | Mantenimiento | 13832.77 | area_no_valida |
| 2025-08-05 | Calidad | Personal | 10000000.00 | importe_excesivo |
| 2025-04-29 | Contabilidad | Suministros | 10000000.00 | importe_excesivo |
| 2025-10-25 | nan | Suministros | 7001.94 | area_no_valida |
| 2025-03-28 | I+D | XXX-PARTIDA MALA | 3178.70 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-10 | nan | Formacion | 6075.21 | area_no_valida |
| 2025-10-18 | XXX-AREA MALA | Publicidad | 8266.56 | area_no_valida |
| 2025-04-07 | Operaciones | Hardware | 10000000.00 | importe_excesivo |
| 2025-01-02 | Direccion | Viajes | -500.00 | importe_invalido |
| 2025-10-29 | I+D | Hardware | -500.00 | importe_invalido |
| 2025-03-05 | XXX-AREA MALA | Formacion | 3203.11 | area_no_valida |
| 2025-02-13 | Ventas | Mantenimiento | -500.00 | importe_invalido |
| 2025-04-28 | Marketing | Software | -500.00 | importe_invalido |
|  | I+D | Viajes | 4255.78 | fecha_invalida |
|  | Contabilidad | Mantenimiento | 5932.04 | fecha_invalida |
| 2025-07-22 | XXX-AREA MALA | Alquileres | 7989.48 | area_no_valida |
| 2025-09-18 | Ventas | Publicidad | 10000000.00 | importe_excesivo |
| 2025-03-30 | Administracion | Hardware | -500.00 | importe_invalido |
| 2025-08-15 | IT | Suministros | -500.00 | importe_invalido |
| 2025-10-04 | XXX-AREA MALA | Publicidad | 1546.25 | area_no_valida |
| 2025-06-07 | Marketing | Seguros | 10000000.00 | importe_excesivo |
| 2025-08-16 | XXX-AREA MALA | Personal | 3069.38 | area_no_valida |
| 2025-09-07 | Ventas | Personal | 10000000.00 | importe_excesivo |
| 2025-10-12 | Ventas | nan | 778.81 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-27 | Direccion | nan | 2163.01 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-05 | Ventas | Formacion | 10000000.00 | importe_excesivo |
| 2025-01-23 | nan | Software | 7656.36 | area_no_valida |
| 2025-05-24 | I+D | XXX-PARTIDA MALA | 6874.35 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-16 | Calidad | nan | 7669.48 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-01 | IT | nan | 1566.33 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-15 | Ventas | Hardware | -500.00 | importe_invalido |
| 2025-10-22 | XXX-AREA MALA | Alquileres | 2055.42 | area_no_valida |
| 2025-05-15 | Direccion | Mantenimiento | -500.00 | importe_invalido |
| 2025-06-10 | RRHH | nan | 473.12 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-13 | XXX-AREA MALA | Formacion | 1251.20 | area_no_valida |
|  | Direccion | Personal | 4769.51 | fecha_invalida |
| 2025-09-22 | nan | Software | 8201.52 | area_no_valida |
| 2025-05-30 | Contabilidad | nan | 2809.45 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-30 | RRHH | XXX-PARTIDA MALA | 15308.13 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-24 | Marketing | nan | 13614.59 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-21 | nan | Seguros | 10531.95 | area_no_valida |
| 2025-02-01 | Calidad | Software | -500.00 | importe_invalido |
|  | Calidad | Viajes | 6956.93 | fecha_invalida |
| 2025-09-21 | XXX-AREA MALA | Personal | 1178.72 | area_no_valida |
| 2025-05-23 | XXX-AREA MALA | Hardware | 4929.51 | area_no_valida |
|  | Direccion | Mantenimiento | 2950.70 | fecha_invalida |
|  | RRHH | Mantenimiento | 2419.93 | fecha_invalida |
| 2025-06-10 | nan | Hardware | 12275.53 | area_no_valida |
| 2025-03-12 | RRHH | Publicidad | -500.00 | importe_invalido |
| 2025-01-20 | IT | Suministros | -500.00 | importe_invalido |
| 2025-09-28 | Marketing | XXX-PARTIDA MALA | 9614.26 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-28 | XXX-AREA MALA | Alquileres | 16165.45 | area_no_valida |
| 2025-02-07 | nan | Viajes | 8868.84 | area_no_valida |
|  | Operaciones | Publicidad | 7448.23 | fecha_invalida |
| 2025-08-20 | Direccion | Formacion | -500.00 | importe_invalido |
| 2025-06-20 | RRHH | nan | 1384.36 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-21 | XXX-AREA MALA | Software | 567.71 | area_no_valida |
| 2025-11-02 | Operaciones | Formacion | 10000000.00 | importe_excesivo |
| 2025-05-21 | Direccion | Hardware | 10000000.00 | importe_excesivo |
| 2025-01-27 | Marketing | XXX-PARTIDA MALA | 16992.30 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-31 | XXX-AREA MALA | Viajes | 2026.73 | area_no_valida |
| 2025-07-03 | Ventas | nan | 7351.79 | partida_no_valida; partida_no_en_presupuesto |
|  | Ventas | Formacion | 4659.78 | fecha_invalida |
| 2025-07-27 | Administracion | nan | 1677.11 | partida_no_valida; partida_no_en_presupuesto |
|  | Ventas | Suministros | 3366.22 | fecha_invalida |
|  | Administracion | Publicidad | 4802.72 | fecha_invalida |
| 2025-10-17 | IT | Alquileres | 10000000.00 | importe_excesivo |
| 2025-07-15 | nan | Personal | 4661.34 | area_no_valida |
| 2025-02-08 | IT | Hardware | 10000000.00 | importe_excesivo |
|  | Marketing | Suministros | 2035.70 | fecha_invalida |
| 2025-04-26 | XXX-AREA MALA | Personal | 11627.31 | area_no_valida |
| 2025-06-16 | XXX-AREA MALA | Software | 9014.13 | area_no_valida |
| 2025-02-11 | Contabilidad | Hardware | 10000000.00 | importe_excesivo |
| 2025-08-06 | Calidad | nan | 5225.17 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-18 | nan | Viajes | 12076.78 | area_no_valida |
| 2025-10-25 | Calidad | Viajes | 10000000.00 | importe_excesivo |
| 2025-04-07 | XXX-AREA MALA | Suministros | 1812.16 | area_no_valida |
| 2025-07-18 | nan | Viajes | 12026.62 | area_no_valida |
| 2025-01-10 | Contabilidad | Suministros | 10000000.00 | importe_excesivo |
| 2025-08-20 | XXX-AREA MALA | Viajes | 4539.45 | area_no_valida |
| 2025-08-18 | RRHH | Seguros | -500.00 | importe_invalido |
|  | Contabilidad | Personal | 1635.64 | fecha_invalida |
| 2025-08-18 | Contabilidad | nan | 7556.88 | partida_no_valida; partida_no_en_presupuesto |
|  | Administracion | Software | 2704.46 | fecha_invalida |
| 2025-06-09 | Contabilidad | Suministros | 10000000.00 | importe_excesivo |
| 2025-02-14 | IT | nan | 703.87 | partida_no_valida; partida_no_en_presupuesto |
|  | Contabilidad | Mantenimiento | 2934.06 | fecha_invalida |
| 2025-11-06 | Ventas | Personal | -500.00 | importe_invalido |
| 2025-07-05 | IT | Viajes | -500.00 | importe_invalido |
| 2025-05-10 | Administracion | XXX-PARTIDA MALA | 4126.14 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-11 | Contabilidad | XXX-PARTIDA MALA | 11573.89 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-23 | nan | Alquileres | 239.18 | area_no_valida |
| 2025-09-22 | XXX-AREA MALA | Personal | 11680.68 | area_no_valida |
| 2025-01-20 | IT | nan | 9320.91 | partida_no_valida; partida_no_en_presupuesto |
|  | Direccion | Software | 1943.38 | fecha_invalida |
| 2025-04-08 | I+D | XXX-PARTIDA MALA | 1865.72 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-15 | I+D | nan | 6070.34 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-05 | XXX-AREA MALA | Alquileres | 1036.02 | area_no_valida |
| 2025-07-10 | Contabilidad | Alquileres | -500.00 | importe_invalido |
|  | Ventas | Viajes | 13102.99 | fecha_invalida |
| 2025-10-23 | nan | Alquileres | 511.44 | area_no_valida |
| 2025-02-11 | Calidad | Alquileres | -500.00 | importe_invalido |
| 2025-11-07 | RRHH | XXX-PARTIDA MALA | 1183.65 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-15 | XXX-AREA MALA | Alquileres | 5454.45 | area_no_valida |
| 2025-08-21 | nan | Mantenimiento | 8491.84 | area_no_valida |
| 2025-03-17 | XXX-AREA MALA | Suministros | 169.75 | area_no_valida |
| 2025-07-11 | Administracion | Formacion | -500.00 | importe_invalido |
| 2025-11-06 | Calidad | nan | 8947.03 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-22 | XXX-AREA MALA | Software | 648.73 | area_no_valida |
| 2025-02-17 | Ventas | XXX-PARTIDA MALA | 1226.81 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-04 | nan | Mantenimiento | 2099.75 | area_no_valida |
| 2025-08-06 | nan | Mantenimiento | 5030.79 | area_no_valida |
|  | IT | Personal | 15130.32 | fecha_invalida |
| 2025-01-21 | IT | nan | 4717.62 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-18 | Administracion | Hardware | -500.00 | importe_invalido |
| 2025-06-28 | Ventas | Mantenimiento | -500.00 | importe_invalido |
| 2025-07-07 | Administracion | XXX-PARTIDA MALA | 5288.85 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-26 | Contabilidad | Software | -500.00 | importe_invalido |
|  | I+D | Mantenimiento | 192.01 | fecha_invalida |
| 2025-05-28 | Calidad | Viajes | 10000000.00 | importe_excesivo |
| 2025-02-05 | RRHH | Hardware | -500.00 | importe_invalido |
| 2025-08-26 | nan | Publicidad | 1025.06 | area_no_valida |
|  | Contabilidad | Hardware | 1874.36 | fecha_invalida |
| 2025-01-19 | nan | Publicidad | 8499.50 | area_no_valida |
| 2025-06-08 | IT | Viajes | -500.00 | importe_invalido |
| 2025-04-22 | nan | Personal | 1022.90 | area_no_valida |
|  | Direccion | Alquileres | 6598.43 | fecha_invalida |
| 2025-04-15 | Operaciones | Alquileres | -500.00 | importe_invalido |
| 2025-04-24 | RRHH | XXX-PARTIDA MALA | 1181.08 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-20 | nan | Viajes | 7895.63 | area_no_valida |
| 2025-10-14 | I+D | XXX-PARTIDA MALA | 2740.55 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-29 | Ventas | Formacion | -500.00 | importe_invalido |
| 2025-02-21 | Ventas | XXX-PARTIDA MALA | 1153.26 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-24 | nan | Personal | 3781.55 | area_no_valida |
| 2025-06-01 | I+D | nan | 560.59 | partida_no_valida; partida_no_en_presupuesto |
|  | Ventas | Mantenimiento | 15972.23 | fecha_invalida |
| 2025-10-06 | RRHH | Seguros | -500.00 | importe_invalido |
| 2025-02-23 | RRHH | Formacion | -500.00 | importe_invalido |
| 2025-10-06 | Calidad | nan | 767.64 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-22 | nan | Mantenimiento | 5809.02 | area_no_valida |
| 2025-10-11 | Operaciones | XXX-PARTIDA MALA | 4971.76 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-26 | XXX-AREA MALA | Software | 3427.28 | area_no_valida |
| 2025-10-01 | Direccion | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-03-28 | XXX-AREA MALA | Seguros | 2371.34 | area_no_valida |
| 2025-09-09 | Direccion | Seguros | -500.00 | importe_invalido |
| 2025-09-16 | XXX-AREA MALA | Viajes | 7565.40 | area_no_valida |
| 2025-06-05 | Calidad | Personal | -500.00 | importe_invalido |
| 2025-07-25 | RRHH | Software | -500.00 | importe_invalido |
| 2025-06-24 | nan | Publicidad | 298.92 | area_no_valida |
| 2025-08-12 | IT | Suministros | 10000000.00 | importe_excesivo |
| 2025-05-06 | I+D | XXX-PARTIDA MALA | 3953.12 | partida_no_valida; partida_no_en_presupuesto |
|  | Contabilidad | Personal | 15964.77 | fecha_invalida |
| 2025-10-04 | XXX-AREA MALA | Mantenimiento | 17473.81 | area_no_valida |
| 2025-07-11 | XXX-AREA MALA | Seguros | 1266.38 | area_no_valida |
| 2025-08-06 | IT | Formacion | 10000000.00 | importe_excesivo |
| 2025-03-04 | Ventas | XXX-PARTIDA MALA | 7339.07 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-23 | XXX-AREA MALA | Hardware | 14388.84 | area_no_valida |
| 2025-10-11 | XXX-AREA MALA | Software | 1455.13 | area_no_valida |
| 2025-08-02 | Administracion | Suministros | -500.00 | importe_invalido |
|  | Administracion | Suministros | 7345.67 | fecha_invalida |
| 2025-05-04 | XXX-AREA MALA | Mantenimiento | 2197.50 | area_no_valida |
| 2025-09-10 | Ventas | nan | 6320.89 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-18 | nan | Alquileres | 1040.60 | area_no_valida |
| 2025-02-21 | Marketing | XXX-PARTIDA MALA | 1211.95 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-24 | XXX-AREA MALA | Mantenimiento | 4859.88 | area_no_valida |
| 2025-07-12 | XXX-AREA MALA | Publicidad | 4931.89 | area_no_valida |
| 2025-07-06 | Ventas | Mantenimiento | -500.00 | importe_invalido |
|  | Calidad | Personal | 9394.44 | fecha_invalida |
| 2025-10-24 | I+D | Software | 10000000.00 | importe_excesivo |
| 2025-06-12 | I+D | XXX-PARTIDA MALA | 595.92 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-25 | XXX-AREA MALA | Formacion | 6482.82 | area_no_valida |
| 2025-10-07 | Direccion | XXX-PARTIDA MALA | 18119.26 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-20 | Ventas | XXX-PARTIDA MALA | 1379.01 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-26 | Marketing | nan | 548.56 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-13 | I+D | XXX-PARTIDA MALA | 2281.65 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-27 | Contabilidad | Personal | -500.00 | importe_invalido |
| 2025-07-06 | Calidad | Personal | -500.00 | importe_invalido |
| 2025-06-01 | nan | Alquileres | 6746.49 | area_no_valida |
| 2025-01-11 | XXX-AREA MALA | Alquileres | 251.00 | area_no_valida |
|  | Operaciones | Mantenimiento | 3328.78 | fecha_invalida |
|  | Operaciones | Personal | 5876.60 | fecha_invalida |
| 2025-02-06 | RRHH | Viajes | -500.00 | importe_invalido |
| 2025-01-22 | Contabilidad | nan | 18714.62 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-08 | I+D | XXX-PARTIDA MALA | 3169.46 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-08 | IT | nan | 7844.61 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-19 | RRHH | Seguros | -500.00 | importe_invalido |
| 2025-06-05 | Direccion | Seguros | 10000000.00 | importe_excesivo |
| 2025-08-23 | XXX-AREA MALA | Publicidad | 516.34 | area_no_valida |
| 2025-06-08 | Operaciones | Publicidad | 10000000.00 | importe_excesivo |
| 2025-10-02 | Calidad | nan | 12747.37 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-02 | RRHH | nan | 1256.20 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-11 | Operaciones | XXX-PARTIDA MALA | 5958.48 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-20 | nan | Seguros | 13434.75 | area_no_valida |
| 2025-10-20 | I+D | XXX-PARTIDA MALA | 10020.47 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-09 | nan | Alquileres | 7265.84 | area_no_valida |
| 2025-05-28 | Ventas | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-04-18 | IT | Personal | 10000000.00 | importe_excesivo |
| 2025-10-25 | Calidad | nan | 15884.92 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-09 | Ventas | XXX-PARTIDA MALA | 9248.22 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-04 | RRHH | XXX-PARTIDA MALA | 12180.85 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-20 | Administracion | XXX-PARTIDA MALA | 4651.22 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-02 | Calidad | Personal | -500.00 | importe_invalido |
| 2025-03-14 | XXX-AREA MALA | Hardware | 316.75 | area_no_valida |
| 2025-05-26 | I+D | Personal | -500.00 | importe_invalido |
| 2025-07-19 | Calidad | Hardware | 10000000.00 | importe_excesivo |
| 2025-06-17 | Calidad | Formacion | 10000000.00 | importe_excesivo |
| 2025-05-07 | RRHH | XXX-PARTIDA MALA | 187.90 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-29 | Contabilidad | Formacion | 10000000.00 | importe_excesivo |
| 2025-11-08 | XXX-AREA MALA | Seguros | 16592.43 | area_no_valida |
| 2025-03-05 | IT | Hardware | 10000000.00 | importe_excesivo |
| 2025-01-07 | Operaciones | Mantenimiento | 10000000.00 | importe_excesivo |
|  | Ventas | Formacion | 16808.73 | fecha_invalida |
| 2025-02-04 | RRHH | nan | 1239.23 | partida_no_valida; partida_no_en_presupuesto |
|  | Operaciones | Mantenimiento | 3699.23 | fecha_invalida |
| 2025-10-23 | Contabilidad | XXX-PARTIDA MALA | 6144.94 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-21 | Administracion | Formacion | -500.00 | importe_invalido |
| 2025-01-27 | Administracion | nan | 1782.32 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-09 | Calidad | Formacion | -500.00 | importe_invalido |
| 2025-03-16 | nan | Mantenimiento | 7107.97 | area_no_valida |
| 2025-04-10 | Marketing | Software | 10000000.00 | importe_excesivo |
| 2025-07-14 | Administracion | XXX-PARTIDA MALA | 2864.74 | partida_no_valida; partida_no_en_presupuesto |
|  | Marketing | Viajes | 4144.02 | fecha_invalida |
| 2025-02-07 | XXX-AREA MALA | Mantenimiento | 15914.18 | area_no_valida |
|  | I+D | Alquileres | 6184.38 | fecha_invalida |
| 2025-03-08 | Marketing | XXX-PARTIDA MALA | 2749.93 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-14 | Contabilidad | Personal | -500.00 | importe_invalido |
| 2025-08-17 | Contabilidad | Personal | -500.00 | importe_invalido |
| 2025-04-15 | nan | Mantenimiento | 5685.31 | area_no_valida |
| 2025-06-20 | RRHH | XXX-PARTIDA MALA | 1060.87 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-10 | IT | XXX-PARTIDA MALA | 6209.44 | partida_no_valida; partida_no_en_presupuesto |
|  | Direccion | Suministros | 16796.56 | fecha_invalida |
| 2025-06-06 | Calidad | Suministros | -500.00 | importe_invalido |
| 2025-07-24 | nan | Alquileres | 2063.37 | area_no_valida |
| 2025-05-25 | XXX-AREA MALA | Viajes | 13637.04 | area_no_valida |
| 2025-05-15 | RRHH | XXX-PARTIDA MALA | 7990.98 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-05 | IT | XXX-PARTIDA MALA | 8794.41 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-29 | nan | Software | 5354.97 | area_no_valida |
|  | Operaciones | Seguros | 7205.72 | fecha_invalida |
| 2025-09-21 | RRHH | nan | 5842.80 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-07 | Marketing | Personal | -500.00 | importe_invalido |
| 2025-06-05 | Operaciones | XXX-PARTIDA MALA | 1282.81 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-17 | Marketing | Seguros | -500.00 | importe_invalido |
| 2025-07-26 | Direccion | Personal | -500.00 | importe_invalido |
| 2025-06-28 | XXX-AREA MALA | Software | 3875.26 | area_no_valida |
| 2025-08-17 | Marketing | XXX-PARTIDA MALA | 1158.79 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-24 | RRHH | nan | 6144.74 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-04 | Operaciones | Mantenimiento | -500.00 | importe_invalido |
| 2025-10-05 | I+D | nan | 3181.55 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-09 | Administracion | nan | 5992.14 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-28 | Calidad | nan | 5653.57 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-16 | Contabilidad | Software | 10000000.00 | importe_excesivo |
| 2025-01-13 | Contabilidad | Seguros | -500.00 | importe_invalido |
| 2025-07-27 | IT | nan | 7174.88 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-05 | Contabilidad | XXX-PARTIDA MALA | 1933.75 | partida_no_valida; partida_no_en_presupuesto |
|  | Marketing | Mantenimiento | 12072.01 | fecha_invalida |
| 2025-08-11 | nan | Viajes | 10259.33 | area_no_valida |
|  | Contabilidad | Hardware | 388.00 | fecha_invalida |
| 2025-06-06 | RRHH | Alquileres | -500.00 | importe_invalido |
| 2025-06-23 | Contabilidad | Alquileres | 10000000.00 | importe_excesivo |
|  | Administracion | Seguros | 962.09 | fecha_invalida |
|  | Administracion | Mantenimiento | 1233.11 | fecha_invalida |
| 2025-06-03 | IT | Alquileres | -500.00 | importe_invalido |
|  | Marketing | Suministros | 1431.30 | fecha_invalida |
| 2025-09-17 | Administracion | Mantenimiento | -500.00 | importe_invalido |
| 2025-05-10 | nan | Alquileres | 8831.10 | area_no_valida |
| 2025-08-15 | Administracion | XXX-PARTIDA MALA | 3281.60 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-08 | Ventas | XXX-PARTIDA MALA | 10047.74 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-26 | I+D | nan | 2452.89 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-28 | nan | Mantenimiento | 1856.44 | area_no_valida |
| 2025-06-17 | RRHH | XXX-PARTIDA MALA | 6698.62 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-25 | nan | Mantenimiento | 2226.59 | area_no_valida |
| 2025-06-22 | nan | Software | 14396.24 | area_no_valida |
|  | Calidad | Hardware | 4389.14 | fecha_invalida |
| 2025-04-01 | XXX-AREA MALA | Personal | 3556.27 | area_no_valida |
| 2025-10-18 | Contabilidad | nan | 12695.97 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-10 | nan | Alquileres | 14910.25 | area_no_valida |
| 2025-10-08 | nan | Personal | 11270.09 | area_no_valida |
| 2025-10-13 | XXX-AREA MALA | Personal | 14000.77 | area_no_valida |
| 2025-02-28 | I+D | Software | -500.00 | importe_invalido |
| 2025-10-15 | nan | Publicidad | 645.99 | area_no_valida |
| 2025-08-02 | Calidad | XXX-PARTIDA MALA | 2852.86 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-28 | Direccion | XXX-PARTIDA MALA | 15616.04 | partida_no_valida; partida_no_en_presupuesto |
|  | Contabilidad | Seguros | 10382.95 | fecha_invalida |
|  | Operaciones | Seguros | 6944.79 | fecha_invalida |
|  | Marketing | Publicidad | 1750.82 | fecha_invalida |
|  | I+D | Viajes | 3804.38 | fecha_invalida |
| 2025-06-10 | I+D | XXX-PARTIDA MALA | 14088.14 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-04 | Direccion | Personal | -500.00 | importe_invalido |
| 2025-03-22 | nan | Personal | 1473.38 | area_no_valida |
| 2025-01-06 | Administracion | nan | 3765.65 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-13 | nan | Software | 5445.34 | area_no_valida |
| 2025-03-23 | XXX-AREA MALA | Viajes | 6124.26 | area_no_valida |
| 2025-07-23 | Operaciones | XXX-PARTIDA MALA | 271.56 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-13 | Marketing | XXX-PARTIDA MALA | 994.49 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-03 | Contabilidad | Publicidad | -500.00 | importe_invalido |
| 2025-09-11 | Administracion | nan | 3374.40 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-28 | XXX-AREA MALA | Publicidad | 1279.20 | area_no_valida |
|  | I+D | Viajes | 6152.63 | fecha_invalida |
| 2025-08-14 | XXX-AREA MALA | Formacion | 9124.75 | area_no_valida |
| 2025-02-15 | Operaciones | XXX-PARTIDA MALA | 3240.20 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-14 | Marketing | Mantenimiento | -500.00 | importe_invalido |
|  | Ventas | Mantenimiento | 13008.33 | fecha_invalida |
| 2025-01-23 | XXX-AREA MALA | Software | 5622.81 | area_no_valida |
| 2025-09-04 | Marketing | Seguros | 10000000.00 | importe_excesivo |
| 2025-07-04 | RRHH | XXX-PARTIDA MALA | 583.40 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-30 | Operaciones | XXX-PARTIDA MALA | 11953.50 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-20 | Administracion | Seguros | -500.00 | importe_invalido |
|  | Calidad | Publicidad | 927.09 | fecha_invalida |
| 2025-09-14 | IT | Publicidad | -500.00 | importe_invalido |
| 2025-04-14 | Operaciones | nan | 507.32 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-12 | Operaciones | XXX-PARTIDA MALA | 4011.01 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-24 | Ventas | nan | 1348.87 | partida_no_valida; partida_no_en_presupuesto |
|  | Operaciones | Seguros | 5768.15 | fecha_invalida |
| 2025-01-14 | XXX-AREA MALA | Mantenimiento | 802.74 | area_no_valida |
| 2025-10-29 | nan | Mantenimiento | 3760.91 | area_no_valida |
| 2025-01-14 | Calidad | nan | 3856.22 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-25 | IT | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-05-04 | I+D | Alquileres | -500.00 | importe_invalido |
| 2025-04-06 | I+D | Software | -500.00 | importe_invalido |
| 2025-10-28 | Administracion | XXX-PARTIDA MALA | 3340.41 | partida_no_valida; partida_no_en_presupuesto |
|  | Contabilidad | Hardware | 9073.77 | fecha_invalida |
| 2025-11-10 | XXX-AREA MALA | Personal | 10708.52 | area_no_valida |
| 2025-01-28 | XXX-AREA MALA | Seguros | 219.94 | area_no_valida |
| 2025-05-03 | Operaciones | Personal | 10000000.00 | importe_excesivo |
| 2025-08-31 | Marketing | nan | 473.14 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-08 | Direccion | XXX-PARTIDA MALA | 2854.57 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-04 | IT | Personal | 10000000.00 | importe_excesivo |
| 2025-09-18 | Administracion | XXX-PARTIDA MALA | 5328.94 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-31 | Ventas | nan | 3803.25 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-15 | I+D | nan | 6621.08 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-29 | XXX-AREA MALA | Seguros | 581.21 | area_no_valida |
| 2025-02-03 | Administracion | nan | 2650.49 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-08 | Calidad | Hardware | 10000000.00 | importe_excesivo |
| 2025-08-13 | Administracion | XXX-PARTIDA MALA | 2779.67 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-19 | Contabilidad | Personal | -500.00 | importe_invalido |
|  | Ventas | Personal | 7013.94 | fecha_invalida |
| 2025-05-27 | Operaciones | nan | 5818.15 | partida_no_valida; partida_no_en_presupuesto |
|  | I+D | Hardware | 8977.27 | fecha_invalida |
| 2025-05-09 | Calidad | nan | 1457.66 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-30 | Operaciones | Hardware | -500.00 | importe_invalido |
| 2025-03-04 | nan | Mantenimiento | 206.01 | area_no_valida |
| 2025-03-10 | Ventas | nan | 4838.98 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-06 | Administracion | XXX-PARTIDA MALA | 3467.24 | partida_no_valida; partida_no_en_presupuesto |
|  | Marketing | Alquileres | 1505.10 | fecha_invalida |
| 2025-02-12 | Operaciones | nan | 1487.29 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-19 | Contabilidad | Formacion | 10000000.00 | importe_excesivo |
| 2025-10-25 | Operaciones | Suministros | -500.00 | importe_invalido |
| 2025-04-06 | XXX-AREA MALA | Suministros | 2117.89 | area_no_valida |
| 2025-07-27 | XXX-AREA MALA | Hardware | 2843.21 | area_no_valida |
| 2025-05-29 | XXX-AREA MALA | Mantenimiento | 4200.99 | area_no_valida |
| 2025-05-17 | Administracion | Suministros | 10000000.00 | importe_excesivo |
| 2025-02-27 | XXX-AREA MALA | Hardware | 277.00 | area_no_valida |
| 2025-04-22 | nan | Formacion | 1562.98 | area_no_valida |
| 2025-07-10 | Marketing | nan | 3686.50 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-31 | Direccion | Mantenimiento | -500.00 | importe_invalido |
| 2025-08-30 | RRHH | Seguros | -500.00 | importe_invalido |
| 2025-01-17 | Operaciones | Hardware | 10000000.00 | importe_excesivo |
| 2025-07-09 | Ventas | nan | 2271.83 | partida_no_valida; partida_no_en_presupuesto |
|  | Direccion | Hardware | 10361.15 | fecha_invalida |
| 2025-06-14 | Calidad | XXX-PARTIDA MALA | 2072.40 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-20 | Operaciones | XXX-PARTIDA MALA | 2128.34 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-27 | Operaciones | Seguros | 10000000.00 | importe_excesivo |
| 2025-03-25 | Administracion | Suministros | -500.00 | importe_invalido |
| 2025-07-30 | Ventas | Formacion | -500.00 | importe_invalido |
| 2025-08-21 | Direccion | XXX-PARTIDA MALA | 9640.03 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-23 | nan | Seguros | 1326.42 | area_no_valida |
| 2025-07-29 | IT | nan | 2624.16 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-29 | I+D | XXX-PARTIDA MALA | 579.91 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-20 | Marketing | Publicidad | -500.00 | importe_invalido |
| 2025-08-27 | IT | XXX-PARTIDA MALA | 5564.85 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-28 | XXX-AREA MALA | Suministros | 353.10 | area_no_valida |
| 2025-07-29 | XXX-AREA MALA | Software | 2141.13 | area_no_valida |
| 2025-04-10 | XXX-AREA MALA | Hardware | 6884.85 | area_no_valida |
|  | I+D | Personal | 7141.48 | fecha_invalida |
| 2025-08-26 | I+D | Viajes | -500.00 | importe_invalido |
| 2025-03-27 | XXX-AREA MALA | Mantenimiento | 5467.52 | area_no_valida |
| 2025-02-01 | Direccion | nan | 10310.30 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-10 | Marketing | nan | 6738.38 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-27 | Calidad | XXX-PARTIDA MALA | 9311.29 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-15 | Calidad | Alquileres | 10000000.00 | importe_excesivo |
| 2025-03-03 | I+D | nan | 3895.77 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-27 | RRHH | Suministros | -500.00 | importe_invalido |
| 2025-10-21 | Contabilidad | XXX-PARTIDA MALA | 546.62 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-07 | Contabilidad | Seguros | -500.00 | importe_invalido |
| 2025-06-08 | Administracion | nan | 3308.38 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-19 | XXX-AREA MALA | Seguros | 329.37 | area_no_valida |
|  | Calidad | Alquileres | 7072.20 | fecha_invalida |
|  | Calidad | Suministros | 6979.05 | fecha_invalida |
| 2025-05-07 | IT | Formacion | 10000000.00 | importe_excesivo |
| 2025-03-14 | XXX-AREA MALA | Publicidad | 1431.14 | area_no_valida |
| 2025-01-30 | Operaciones | Seguros | -500.00 | importe_invalido |
| 2025-09-12 | Contabilidad | Suministros | -500.00 | importe_invalido |
| 2025-03-05 | nan | Suministros | 1022.64 | area_no_valida |
|  | Marketing | Personal | 14372.37 | fecha_invalida |
|  | Contabilidad | Software | 17502.64 | fecha_invalida |
| 2025-08-19 | Administracion | Hardware | -500.00 | importe_invalido |
|  | Contabilidad | Viajes | 2375.57 | fecha_invalida |
| 2025-02-07 | Operaciones | nan | 1376.96 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-01 | nan | Mantenimiento | 7580.95 | area_no_valida |
| 2025-08-19 | Operaciones | XXX-PARTIDA MALA | 7985.00 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-12 | Contabilidad | nan | 603.20 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-11 | XXX-AREA MALA | Publicidad | 3470.64 | area_no_valida |
| 2025-07-16 | nan | Viajes | 7301.44 | area_no_valida |
| 2025-09-11 | Administracion | nan | 5612.79 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-07 | Operaciones | XXX-PARTIDA MALA | 2551.12 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-23 | IT | nan | 3105.23 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-19 | Contabilidad | XXX-PARTIDA MALA | 5525.70 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-01 | Administracion | nan | 1613.22 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-13 | nan | Suministros | 2947.95 | area_no_valida |
| 2025-03-26 | RRHH | XXX-PARTIDA MALA | 268.64 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-19 | XXX-AREA MALA | Publicidad | 3820.78 | area_no_valida |
| 2025-04-06 | XXX-AREA MALA | Alquileres | 5795.88 | area_no_valida |
| 2025-07-15 | Operaciones | nan | 805.53 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-16 | Administracion | XXX-PARTIDA MALA | 2421.50 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-25 | nan | Seguros | 5423.89 | area_no_valida |
|  | Operaciones | Hardware | 374.78 | fecha_invalida |
| 2025-10-20 | IT | Personal | 10000000.00 | importe_excesivo |
| 2025-07-05 | Contabilidad | nan | 13781.24 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-02 | RRHH | Hardware | 10000000.00 | importe_excesivo |
| 2025-02-01 | XXX-AREA MALA | Formacion | 2044.84 | area_no_valida |
| 2025-08-13 | Ventas | nan | 1389.41 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-14 | Administracion | Software | 10000000.00 | importe_excesivo |
| 2025-09-06 | Operaciones | Suministros | 10000000.00 | importe_excesivo |
| 2025-07-08 | XXX-AREA MALA | Publicidad | 1085.87 | area_no_valida |
| 2025-10-31 | nan | Hardware | 14117.45 | area_no_valida |
| 2025-02-10 | Operaciones | Formacion | -500.00 | importe_invalido |
| 2025-06-16 | XXX-AREA MALA | Viajes | 1572.28 | area_no_valida |
|  | Calidad | Suministros | 625.13 | fecha_invalida |
| 2025-06-07 | Contabilidad | Alquileres | 10000000.00 | importe_excesivo |
| 2025-04-10 | nan | Mantenimiento | 14256.79 | area_no_valida |
| 2025-10-08 | IT | nan | 1654.51 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-07 | Calidad | XXX-PARTIDA MALA | 6190.99 | partida_no_valida; partida_no_en_presupuesto |
|  | Calidad | Hardware | 10769.85 | fecha_invalida |
|  | RRHH | Alquileres | 8334.96 | fecha_invalida |
| 2025-08-16 | IT | Seguros | -500.00 | importe_invalido |
| 2025-09-18 | XXX-AREA MALA | Alquileres | 1060.32 | area_no_valida |
| 2025-10-25 | Contabilidad | nan | 3560.94 | partida_no_valida; partida_no_en_presupuesto |
|  | Administracion | Viajes | 8300.15 | fecha_invalida |
| 2025-07-23 | nan | Software | 8893.71 | area_no_valida |
| 2025-09-20 | RRHH | Viajes | 10000000.00 | importe_excesivo |
| 2025-07-10 | Contabilidad | nan | 6158.98 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-16 | Direccion | Publicidad | -500.00 | importe_invalido |
| 2025-05-12 | Direccion | Personal | -500.00 | importe_invalido |
| 2025-04-27 | Contabilidad | nan | 9712.27 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-07 | Calidad | XXX-PARTIDA MALA | 17201.18 | partida_no_valida; partida_no_en_presupuesto |
|  | RRHH | Formacion | 2282.53 | fecha_invalida |
| 2025-03-15 | Direccion | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-07-10 | nan | Software | 7189.66 | area_no_valida |
| 2025-06-05 | Marketing | Mantenimiento | -500.00 | importe_invalido |
| 2025-10-06 | Administracion | XXX-PARTIDA MALA | 1034.47 | partida_no_valida; partida_no_en_presupuesto |
|  | Marketing | Hardware | 851.62 | fecha_invalida |
| 2025-01-26 | nan | Formacion | 913.11 | area_no_valida |
| 2025-07-27 | I+D | XXX-PARTIDA MALA | 215.53 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-06 | XXX-AREA MALA | Publicidad | 1255.76 | area_no_valida |
| 2025-10-11 | Marketing | nan | 12495.03 | partida_no_valida; partida_no_en_presupuesto |
|  | Contabilidad | Viajes | 5058.44 | fecha_invalida |
| 2025-05-30 | Direccion | nan | 5022.32 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-20 | IT | XXX-PARTIDA MALA | 563.30 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-17 | I+D | Software | -500.00 | importe_invalido |
| 2025-03-13 | IT | XXX-PARTIDA MALA | 2526.60 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-06 | nan | Mantenimiento | 3298.90 | area_no_valida |
| 2025-03-17 | Calidad | XXX-PARTIDA MALA | 12563.27 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-27 | RRHH | Formacion | 10000000.00 | importe_excesivo |
| 2025-11-12 | RRHH | Hardware | 10000000.00 | importe_excesivo |
| 2025-02-22 | XXX-AREA MALA | Suministros | 5882.20 | area_no_valida |
|  | Contabilidad | Hardware | 274.19 | fecha_invalida |
| 2025-08-03 | I+D | XXX-PARTIDA MALA | 4831.50 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-24 | Contabilidad | Alquileres | -500.00 | importe_invalido |
| 2025-05-10 | Direccion | nan | 2358.72 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-25 | I+D | XXX-PARTIDA MALA | 9735.52 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-05 | Ventas | Viajes | -500.00 | importe_invalido |
| 2025-06-24 | nan | Formacion | 1302.44 | area_no_valida |
| 2025-08-31 | XXX-AREA MALA | Software | 8531.97 | area_no_valida |
| 2025-02-09 | XXX-AREA MALA | Alquileres | 527.25 | area_no_valida |
| 2025-10-13 | Ventas | Viajes | -500.00 | importe_invalido |
|  | Administracion | Suministros | 1432.68 | fecha_invalida |
| 2025-10-26 | IT | Hardware | -500.00 | importe_invalido |
| 2025-04-09 | Marketing | Suministros | 10000000.00 | importe_excesivo |
| 2025-07-17 | XXX-AREA MALA | Suministros | 2624.06 | area_no_valida |
| 2025-05-16 | XXX-AREA MALA | Viajes | 7412.43 | area_no_valida |
| 2025-07-10 | XXX-AREA MALA | Formacion | 1429.09 | area_no_valida |
| 2025-08-10 | nan | Alquileres | 2006.06 | area_no_valida |
| 2025-01-17 | XXX-AREA MALA | Hardware | 11241.95 | area_no_valida |
| 2025-05-13 | Operaciones | XXX-PARTIDA MALA | 6309.95 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-29 | I+D | Publicidad | -500.00 | importe_invalido |
| 2025-07-02 | XXX-AREA MALA | Software | 16204.53 | area_no_valida |
| 2025-03-29 | Marketing | Formacion | -500.00 | importe_invalido |
| 2025-09-26 | nan | Formacion | 3805.43 | area_no_valida |
| 2025-06-13 | nan | Seguros | 3417.75 | area_no_valida |
| 2025-07-21 | Direccion | XXX-PARTIDA MALA | 6797.46 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-24 | nan | Hardware | 3932.89 | area_no_valida |
| 2025-06-08 | nan | Alquileres | 5753.10 | area_no_valida |
|  | RRHH | Suministros | 1633.84 | fecha_invalida |
| 2025-04-26 | nan | Suministros | 11632.43 | area_no_valida |
| 2025-08-21 | Direccion | Hardware | 10000000.00 | importe_excesivo |
| 2025-10-23 | Operaciones | nan | 7959.79 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-16 | Ventas | Personal | -500.00 | importe_invalido |
| 2025-02-06 | IT | Alquileres | 10000000.00 | importe_excesivo |
| 2025-02-08 | Calidad | Publicidad | -500.00 | importe_invalido |
| 2025-10-15 | Direccion | XXX-PARTIDA MALA | 5624.13 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-29 | nan | Viajes | 9554.32 | area_no_valida |
| 2025-05-17 | Contabilidad | Formacion | -500.00 | importe_invalido |
| 2025-09-18 | IT | Publicidad | 10000000.00 | importe_excesivo |
| 2025-06-24 | Ventas | XXX-PARTIDA MALA | 6191.28 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-07 | I+D | XXX-PARTIDA MALA | 5728.90 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-13 | Direccion | XXX-PARTIDA MALA | 8637.55 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-03 | RRHH | XXX-PARTIDA MALA | 14860.65 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-10 | Operaciones | Suministros | 10000000.00 | importe_excesivo |
|  | IT | Hardware | 995.06 | fecha_invalida |
| 2025-03-19 | RRHH | Suministros | 10000000.00 | importe_excesivo |
| 2025-01-04 | Contabilidad | Alquileres | 10000000.00 | importe_excesivo |
| 2025-04-08 | Ventas | XXX-PARTIDA MALA | 2643.36 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-01 | Operaciones | nan | 1795.95 | partida_no_valida; partida_no_en_presupuesto |
|  | Administracion | Software | 4473.12 | fecha_invalida |
| 2025-02-07 | Ventas | Suministros | -500.00 | importe_invalido |
| 2025-09-05 | nan | Software | 11093.77 | area_no_valida |
| 2025-09-07 | Operaciones | Formacion | -500.00 | importe_invalido |
| 2025-03-17 | Ventas | Formacion | -500.00 | importe_invalido |
| 2025-10-25 | Direccion | XXX-PARTIDA MALA | 835.12 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-28 | IT | nan | 8071.07 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-08 | XXX-AREA MALA | Suministros | 2918.82 | area_no_valida |
| 2025-03-28 | nan | Viajes | 5202.78 | area_no_valida |
| 2025-04-02 | Direccion | nan | 5788.30 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-09 | I+D | Alquileres | -500.00 | importe_invalido |
| 2025-02-19 | nan | Viajes | 15036.76 | area_no_valida |
| 2025-04-15 | Administracion | Personal | -500.00 | importe_invalido |
| 2025-09-25 | Administracion | XXX-PARTIDA MALA | 1437.60 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-24 | XXX-AREA MALA | Hardware | 4151.78 | area_no_valida |
| 2025-03-11 | Calidad | Personal | -500.00 | importe_invalido |
| 2025-11-09 | XXX-AREA MALA | Seguros | 12952.66 | area_no_valida |
|  | Calidad | Seguros | 1496.64 | fecha_invalida |
| 2025-07-11 | Marketing | Publicidad | -500.00 | importe_invalido |
| 2025-04-18 | XXX-AREA MALA | Software | 2266.99 | area_no_valida |
| 2025-05-15 | XXX-AREA MALA | Suministros | 1515.07 | area_no_valida |
| 2025-03-09 | nan | Seguros | 2080.07 | area_no_valida |
| 2025-08-22 | Direccion | Alquileres | 10000000.00 | importe_excesivo |
| 2025-08-30 | Operaciones | Personal | 10000000.00 | importe_excesivo |
| 2025-07-09 | I+D | Personal | -500.00 | importe_invalido |
| 2025-03-16 | nan | Alquileres | 1270.04 | area_no_valida |
| 2025-07-27 | RRHH | Software | -500.00 | importe_invalido |
| 2025-07-06 | Direccion | nan | 12605.43 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-09 | nan | Software | 6675.91 | area_no_valida |
| 2025-06-21 | Calidad | XXX-PARTIDA MALA | 13501.19 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-21 | Calidad | nan | 2268.02 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-17 | Calidad | Viajes | 10000000.00 | importe_excesivo |
| 2025-10-19 | Direccion | Hardware | 10000000.00 | importe_excesivo |
| 2025-07-14 | Direccion | XXX-PARTIDA MALA | 1927.24 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-20 | Contabilidad | Formacion | -500.00 | importe_invalido |
| 2025-10-01 | Operaciones | Personal | 10000000.00 | importe_excesivo |
| 2025-10-19 | nan | Publicidad | 888.67 | area_no_valida |
|  | Calidad | Seguros | 5552.28 | fecha_invalida |
| 2025-08-19 | Calidad | XXX-PARTIDA MALA | 6136.88 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-02 | Ventas | XXX-PARTIDA MALA | 15451.47 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-05 | nan | Suministros | 4644.48 | area_no_valida |
|  | Operaciones | Suministros | 1726.47 | fecha_invalida |
| 2025-05-10 | Administracion | Formacion | -500.00 | importe_invalido |
| 2025-03-28 | nan | Publicidad | 2481.75 | area_no_valida |
| 2025-01-06 | nan | Seguros | 7289.32 | area_no_valida |
| 2025-07-16 | IT | nan | 2847.48 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-16 | Ventas | nan | 1935.45 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-04 | nan | Personal | 6001.64 | area_no_valida |
| 2025-09-23 | XXX-AREA MALA | Hardware | 4468.16 | area_no_valida |
| 2025-08-04 | Ventas | nan | 12660.65 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-07 | Marketing | XXX-PARTIDA MALA | 10469.03 | partida_no_valida; partida_no_en_presupuesto |
|  | Calidad | Formacion | 1138.28 | fecha_invalida |
| 2025-11-04 | RRHH | XXX-PARTIDA MALA | 545.49 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-22 | RRHH | Publicidad | -500.00 | importe_invalido |
| 2025-02-21 | Operaciones | nan | 1739.91 | partida_no_valida; partida_no_en_presupuesto |
|  | Calidad | Hardware | 4204.35 | fecha_invalida |
| 2025-01-28 | Marketing | XXX-PARTIDA MALA | 305.38 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-10 | Direccion | XXX-PARTIDA MALA | 13114.49 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-25 | Contabilidad | Formacion | 10000000.00 | importe_excesivo |
|  | IT | Formacion | 2624.40 | fecha_invalida |
|  | IT | Software | 7062.03 | fecha_invalida |
| 2025-08-27 | I+D | Formacion | 10000000.00 | importe_excesivo |
| 2025-01-20 | Operaciones | XXX-PARTIDA MALA | 3590.50 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-26 | Ventas | nan | 5978.32 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-05 | Direccion | Software | 10000000.00 | importe_excesivo |
| 2025-04-19 | Administracion | Personal | 10000000.00 | importe_excesivo |
| 2025-08-21 | Operaciones | Hardware | 10000000.00 | importe_excesivo |
| 2025-01-02 | nan | Viajes | 11789.65 | area_no_valida |
| 2025-02-13 | XXX-AREA MALA | Personal | 5624.90 | area_no_valida |
|  | Calidad | Suministros | 3538.58 | fecha_invalida |
| 2025-01-02 | nan | Seguros | 10311.40 | area_no_valida |
| 2025-07-08 | Ventas | Seguros | 10000000.00 | importe_excesivo |
| 2025-10-06 | Contabilidad | XXX-PARTIDA MALA | 4380.01 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-14 | Ventas | Personal | -500.00 | importe_invalido |
|  | Operaciones | Suministros | 5769.77 | fecha_invalida |
| 2025-10-30 | XXX-AREA MALA | Alquileres | 4303.36 | area_no_valida |
| 2025-05-25 | Administracion | Suministros | -500.00 | importe_invalido |
| 2025-03-23 | Administracion | XXX-PARTIDA MALA | 1635.05 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-02 | nan | Suministros | 5934.11 | area_no_valida |
| 2025-10-22 | Operaciones | Suministros | 10000000.00 | importe_excesivo |
| 2025-05-29 | Direccion | nan | 1502.61 | partida_no_valida; partida_no_en_presupuesto |
| 2025-07-22 | IT | XXX-PARTIDA MALA | 9444.96 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-19 | XXX-AREA MALA | Mantenimiento | 5986.44 | area_no_valida |
| 2025-01-14 | nan | Personal | 425.45 | area_no_valida |
| 2025-06-02 | Operaciones | Publicidad | -500.00 | importe_invalido |
| 2025-03-31 | Contabilidad | XXX-PARTIDA MALA | 518.95 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-20 | nan | Suministros | 7832.18 | area_no_valida |
| 2025-09-09 | Marketing | Publicidad | 10000000.00 | importe_excesivo |
|  | Marketing | Formacion | 5987.39 | fecha_invalida |
| 2025-07-13 | nan | Suministros | 2731.38 | area_no_valida |
| 2025-09-24 | Calidad | XXX-PARTIDA MALA | 9131.34 | partida_no_valida; partida_no_en_presupuesto |
|  | Direccion | Suministros | 452.53 | fecha_invalida |
| 2025-09-07 | XXX-AREA MALA | Viajes | 3260.59 | area_no_valida |
|  | Administracion | Viajes | 6360.14 | fecha_invalida |
| 2025-08-31 | nan | Hardware | 2664.66 | area_no_valida |
| 2025-04-23 | nan | Personal | 11783.50 | area_no_valida |
| 2025-10-12 | Operaciones | Suministros | -500.00 | importe_invalido |
| 2025-10-18 | XXX-AREA MALA | Viajes | 608.86 | area_no_valida |
| 2025-07-09 | XXX-AREA MALA | Hardware | 15643.80 | area_no_valida |
| 2025-10-22 | Administracion | nan | 6579.89 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-11 | XXX-AREA MALA | Mantenimiento | 1277.30 | area_no_valida |
| 2025-09-27 | Marketing | Software | 10000000.00 | importe_excesivo |
| 2025-05-21 | XXX-AREA MALA | Mantenimiento | 13052.75 | area_no_valida |
| 2025-02-12 | Contabilidad | Suministros | -500.00 | importe_invalido |
| 2025-07-18 | XXX-AREA MALA | Publicidad | 872.68 | area_no_valida |
| 2025-08-09 | Calidad | nan | 15524.35 | partida_no_valida; partida_no_en_presupuesto |
|  | Operaciones | Software | 5568.74 | fecha_invalida |
| 2025-01-13 | nan | Seguros | 6101.14 | area_no_valida |
| 2025-02-28 | XXX-AREA MALA | Publicidad | 5736.55 | area_no_valida |
| 2025-03-20 | IT | XXX-PARTIDA MALA | 1043.68 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-15 | I+D | Suministros | 10000000.00 | importe_excesivo |
| 2025-04-09 | XXX-AREA MALA | Viajes | 2066.99 | area_no_valida |
| 2025-01-12 | XXX-AREA MALA | Mantenimiento | 1971.14 | area_no_valida |
| 2025-03-27 | Administracion | XXX-PARTIDA MALA | 4219.47 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-17 | XXX-AREA MALA | Alquileres | 1441.12 | area_no_valida |
| 2025-04-03 | Marketing | nan | 6231.00 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-15 | IT | Formacion | -500.00 | importe_invalido |
|  | Marketing | Mantenimiento | 3770.76 | fecha_invalida |
| 2025-03-26 | Operaciones | Mantenimiento | -500.00 | importe_invalido |
| 2025-05-06 | XXX-AREA MALA | Alquileres | 4907.41 | area_no_valida |
| 2025-06-25 | Direccion | nan | 5689.98 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-24 | Calidad | nan | 1369.25 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-21 | XXX-AREA MALA | Personal | 2264.50 | area_no_valida |
| 2025-09-24 | XXX-AREA MALA | Personal | 856.82 | area_no_valida |
| 2025-07-21 | IT | Alquileres | -500.00 | importe_invalido |
| 2025-06-02 | XXX-AREA MALA | Alquileres | 140.95 | area_no_valida |
| 2025-10-08 | IT | XXX-PARTIDA MALA | 1336.96 | partida_no_valida; partida_no_en_presupuesto |
| 2025-02-24 | nan | Publicidad | 6154.00 | area_no_valida |
| 2025-01-21 | nan | Mantenimiento | 2567.23 | area_no_valida |
| 2025-08-05 | IT | Personal | -500.00 | importe_invalido |
| 2025-04-07 | XXX-AREA MALA | Software | 579.06 | area_no_valida |
| 2025-02-10 | Administracion | XXX-PARTIDA MALA | 1123.51 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-12 | RRHH | Alquileres | 10000000.00 | importe_excesivo |
| 2025-01-01 | nan | Mantenimiento | 7712.83 | area_no_valida |
| 2025-09-15 | I+D | Suministros | 10000000.00 | importe_excesivo |
|  | I+D | Hardware | 4573.25 | fecha_invalida |
| 2025-10-01 | Direccion | Hardware | 10000000.00 | importe_excesivo |
| 2025-06-09 | nan | Seguros | 13386.57 | area_no_valida |
| 2025-02-27 | XXX-AREA MALA | Viajes | 8257.47 | area_no_valida |
| 2025-09-15 | I+D | XXX-PARTIDA MALA | 7052.11 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-26 | Calidad | nan | 5400.05 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-12 | Calidad | Publicidad | -500.00 | importe_invalido |
|  | Calidad | Seguros | 2844.23 | fecha_invalida |
| 2025-02-06 | Administracion | XXX-PARTIDA MALA | 1412.07 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-02 | XXX-AREA MALA | Alquileres | 8673.27 | area_no_valida |
| 2025-09-06 | Administracion | nan | 14717.04 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-10 | Direccion | XXX-PARTIDA MALA | 4833.69 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-11 | Administracion | Suministros | -500.00 | importe_invalido |
| 2025-10-06 | Direccion | Software | 10000000.00 | importe_excesivo |
| 2025-10-24 | Contabilidad | Software | -500.00 | importe_invalido |
| 2025-06-11 | nan | Alquileres | 2652.40 | area_no_valida |
| 2025-11-01 | nan | Alquileres | 222.31 | area_no_valida |
| 2025-06-10 | I+D | nan | 7987.20 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-26 | XXX-AREA MALA | Alquileres | 614.42 | area_no_valida |
| 2025-01-18 | I+D | Personal | -500.00 | importe_invalido |
|  | Direccion | Personal | 9307.76 | fecha_invalida |
| 2025-08-09 | Contabilidad | Mantenimiento | -500.00 | importe_invalido |
| 2025-09-22 | XXX-AREA MALA | Alquileres | 623.89 | area_no_valida |
|  | Direccion | Alquileres | 3187.05 | fecha_invalida |
| 2025-09-28 | I+D | nan | 316.09 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-22 | Administracion | Hardware | 10000000.00 | importe_excesivo |
| 2025-08-27 | Calidad | Alquileres | 10000000.00 | importe_excesivo |
| 2025-05-10 | RRHH | nan | 619.71 | partida_no_valida; partida_no_en_presupuesto |
| 2025-08-17 | I+D | Alquileres | -500.00 | importe_invalido |
| 2025-05-30 | nan | Mantenimiento | 2575.34 | area_no_valida |
| 2025-06-05 | Operaciones | Suministros | -500.00 | importe_invalido |
| 2025-05-09 | nan | Mantenimiento | 14442.61 | area_no_valida |
| 2025-07-02 | Administracion | Personal | 10000000.00 | importe_excesivo |
| 2025-09-10 | nan | Software | 2203.73 | area_no_valida |
| 2025-07-17 | XXX-AREA MALA | Software | 7991.93 | area_no_valida |
| 2025-02-12 | Contabilidad | Hardware | 10000000.00 | importe_excesivo |
| 2025-02-10 | Administracion | Alquileres | -500.00 | importe_invalido |
|  | I+D | Suministros | 7440.74 | fecha_invalida |
| 2025-01-27 | RRHH | Formacion | 10000000.00 | importe_excesivo |
| 2025-09-29 | nan | Publicidad | 144.80 | area_no_valida |
| 2025-05-11 | XXX-AREA MALA | Viajes | 10678.43 | area_no_valida |
| 2025-01-02 | Contabilidad | Alquileres | -500.00 | importe_invalido |
|  | Administracion | Suministros | 869.53 | fecha_invalida |
|  | Contabilidad | Seguros | 2048.51 | fecha_invalida |
|  | RRHH | Software | 1745.41 | fecha_invalida |
| 2025-07-19 | Administracion | nan | 4660.37 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-12 | Ventas | Formacion | -500.00 | importe_invalido |
| 2025-05-30 | Calidad | XXX-PARTIDA MALA | 2518.96 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-10 | nan | Personal | 6126.74 | area_no_valida |
| 2025-01-19 | XXX-AREA MALA | Hardware | 8874.40 | area_no_valida |
| 2025-04-10 | nan | Software | 3359.96 | area_no_valida |
| 2025-09-03 | Direccion | Mantenimiento | 10000000.00 | importe_excesivo |
| 2025-05-20 | nan | Alquileres | 7061.36 | area_no_valida |
|  | I+D | Viajes | 10349.35 | fecha_invalida |
| 2025-07-31 | Contabilidad | Seguros | -500.00 | importe_invalido |
| 2025-09-18 | RRHH | nan | 6222.70 | partida_no_valida; partida_no_en_presupuesto |
| 2025-11-05 | Calidad | XXX-PARTIDA MALA | 3363.34 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-07 | Contabilidad | XXX-PARTIDA MALA | 1665.46 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-06 | I+D | nan | 5910.46 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-04 | XXX-AREA MALA | Hardware | 3016.69 | area_no_valida |
|  | IT | Suministros | 2567.13 | fecha_invalida |
| 2025-08-12 | I+D | XXX-PARTIDA MALA | 8704.44 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-13 | IT | Suministros | -500.00 | importe_invalido |
| 2025-06-29 | Contabilidad | nan | 4723.15 | partida_no_valida; partida_no_en_presupuesto |
|  | Marketing | Viajes | 3154.57 | fecha_invalida |
| 2025-08-04 | Ventas | Publicidad | -500.00 | importe_invalido |
| 2025-03-21 | XXX-AREA MALA | Hardware | 5885.84 | area_no_valida |
|  | Operaciones | Publicidad | 3989.84 | fecha_invalida |
| 2025-02-14 | Marketing | Personal | 10000000.00 | importe_excesivo |
| 2025-08-10 | Administracion | Suministros | -500.00 | importe_invalido |
| 2025-09-27 | nan | Software | 13154.99 | area_no_valida |
|  | Ventas | Formacion | 4836.02 | fecha_invalida |
|  | Contabilidad | Suministros | 4088.94 | fecha_invalida |
| 2025-09-09 | I+D | nan | 8842.86 | partida_no_valida; partida_no_en_presupuesto |
| 2025-06-02 | IT | XXX-PARTIDA MALA | 2385.10 | partida_no_valida; partida_no_en_presupuesto |
| 2025-09-08 | Operaciones | XXX-PARTIDA MALA | 8400.47 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-21 | Contabilidad | Suministros | -500.00 | importe_invalido |
| 2025-02-08 | Calidad | XXX-PARTIDA MALA | 5105.75 | partida_no_valida; partida_no_en_presupuesto |
|  | Direccion | Hardware | 11226.30 | fecha_invalida |
| 2025-07-27 | Marketing | Viajes | 10000000.00 | importe_excesivo |
|  | I+D | Alquileres | 4551.59 | fecha_invalida |
| 2025-04-17 | Contabilidad | Software | -500.00 | importe_invalido |
| 2025-05-18 | I+D | nan | 1339.57 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-01 | Administracion | Hardware | 10000000.00 | importe_excesivo |
|  | Marketing | Software | 3744.95 | fecha_invalida |
| 2025-02-11 | XXX-AREA MALA | Suministros | 4764.18 | area_no_valida |
| 2025-07-02 | Direccion | XXX-PARTIDA MALA | 544.39 | partida_no_valida; partida_no_en_presupuesto |
| 2025-10-08 | XXX-AREA MALA | Viajes | 233.97 | area_no_valida |
| 2025-05-31 | nan | Formacion | 1211.40 | area_no_valida |
| 2025-03-28 | Operaciones | Mantenimiento | -500.00 | importe_invalido |
| 2025-01-28 | Marketing | Alquileres | 10000000.00 | importe_excesivo |
| 2025-08-13 | nan | Suministros | 3547.23 | area_no_valida |
|  | Operaciones | Viajes | 9039.19 | fecha_invalida |
| 2025-08-11 | nan | Software | 4499.26 | area_no_valida |
| 2025-05-01 | Ventas | Viajes | 10000000.00 | importe_excesivo |
| 2025-02-25 | nan | Software | 14918.33 | area_no_valida |
| 2025-08-07 | nan | Suministros | 2996.43 | area_no_valida |
| 2025-04-27 | Contabilidad | XXX-PARTIDA MALA | 16743.11 | partida_no_valida; partida_no_en_presupuesto |
| 2025-01-03 | XXX-AREA MALA | Publicidad | 3927.81 | area_no_valida |
| 2025-04-10 | Ventas | Seguros | 10000000.00 | importe_excesivo |
| 2025-02-27 | Calidad | XXX-PARTIDA MALA | 6452.96 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-13 | XXX-AREA MALA | Seguros | 10271.01 | area_no_valida |
| 2025-04-15 | XXX-AREA MALA | Personal | 5545.57 | area_no_valida |
| 2025-10-21 | I+D | nan | 3833.42 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-29 | XXX-AREA MALA | Hardware | 9276.83 | area_no_valida |
| 2025-08-24 | nan | Mantenimiento | 4048.49 | area_no_valida |
| 2025-02-24 | XXX-AREA MALA | Suministros | 4221.13 | area_no_valida |
| 2025-02-24 | nan | Software | 521.71 | area_no_valida |
| 2025-04-14 | nan | Personal | 3330.73 | area_no_valida |
| 2025-07-28 | nan | Hardware | 5469.38 | area_no_valida |
| 2025-06-14 | Ventas | nan | 18939.54 | partida_no_valida; partida_no_en_presupuesto |
| 2025-03-25 | XXX-AREA MALA | Software | 7026.03 | area_no_valida |
| 2025-04-14 | Administracion | Hardware | 10000000.00 | importe_excesivo |
| 2025-08-16 | Direccion | Alquileres | 10000000.00 | importe_excesivo |
| 2025-08-04 | XXX-AREA MALA | Publicidad | 11318.43 | area_no_valida |
| 2025-08-19 | nan | Publicidad | 12479.34 | area_no_valida |
| 2025-05-25 | Ventas | Publicidad | -500.00 | importe_invalido |
| 2025-04-29 | XXX-AREA MALA | Viajes | 9673.87 | area_no_valida |
| 2025-05-03 | RRHH | Formacion | 10000000.00 | importe_excesivo |
| 2025-10-02 | I+D | XXX-PARTIDA MALA | 3561.82 | partida_no_valida; partida_no_en_presupuesto |
| 2025-05-28 | Ventas | Hardware | 10000000.00 | importe_excesivo |
|  | Direccion | Hardware | 5970.91 | fecha_invalida |
| 2025-08-26 | XXX-AREA MALA | Viajes | 570.63 | area_no_valida |
| 2025-01-19 | Calidad | Suministros | -500.00 | importe_invalido |
| 2025-04-18 | nan | Seguros | 3224.44 | area_no_valida |
| 2025-08-24 | Ventas | XXX-PARTIDA MALA | 4833.86 | partida_no_valida; partida_no_en_presupuesto |
| 2025-04-09 | nan | Suministros | 7572.20 | area_no_valida |
