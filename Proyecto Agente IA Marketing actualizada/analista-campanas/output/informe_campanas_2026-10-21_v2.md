# Informe ejecutivo de campañas

**Fecha del informe:** 2026-10-21  
**Periodo analizado:** 1–30 de septiembre de 2026  
**Archivo de datos:** `input/campanas_2026_09.csv`  
**Fuente de benchmarks:** respaldo local `config/benchmarks_respaldo.csv` (no hay conexión de Google Sheets disponible en esta sesión)  
**Umbral del semáforo:** 20% (verde = cumple/supera el objetivo; amarillo = desviación desfavorable de hasta 40%; rojo = desviación desfavorable superior al 40%).

## Resumen ejecutivo

Se analizaron cinco campañas y todas las filas son válidas. Google Ads logra el CPA más bajo (12,50 €) y supera sus tres objetivos; Meta Ads presenta resultados mixtos, con una campaña por encima del objetivo de CPA. LinkedIn Ads tiene el CPA más alto (120,00 €), un 50% peor que su referencia. Video_Prueba en TikTok consigue clics económicos, pero no registra conversiones, por lo que su CPA no se puede calcular.

## KPIs por campaña

| Campaña | Canal | CTR | CPC | CPA | Conversiones | Comparación relevante con benchmark |
|---|---|---:|---:|---:|---:|---|
| Search_Reservas_Verano | Google Ads | 5,00% | 0,50 € | 12,50 € | 100 | CTR +66,7% favorable; CPC −50,0% favorable; CPA −50,0% favorable |
| Retargeting_Web | Meta Ads | 1,50% | 0,50 € | 20,00 € | 45 | CTR +50,0% favorable; CPC −37,5% favorable; CPA cumple |
| Stories_Escapadas | Meta Ads | 0,80% | 0,75 € | 40,00 € | 12 | CTR −20,0% en el límite; CPC −6,3% favorable; CPA +100,0% desfavorable |
| Eventos_Empresa | LinkedIn Ads | 0,50% | 4,00 € | 120,00 € | 5 | CTR −16,7% favorable por quedar dentro del umbral; CPC +14,3% desfavorable moderada; CPA +50,0% desfavorable significativa |
| Video_Prueba | TikTok Ads | 1,50% | 0,30 € | n/d | 0 | CTR +50,0% favorable; CPC −40,0% favorable; sin CPA por cero conversiones |

## Resultados agregados por canal

Los KPIs agregados se calculan a partir de los totales de cada canal (CTR = clics/impresiones, CPC = coste/clics, CPA = coste/conversiones).

| Canal | Campañas | CTR real / objetivo | CPC real / objetivo | CPA real / objetivo |
|---|---:|---|---|---|
| Google Ads | 1 | 5,00% / 3,00% — 🟢 +66,7% favorable | 0,50 € / 1,00 € — 🟢 −50,0% favorable | 12,50 € / 25,00 € — 🟢 −50,0% favorable |
| Meta Ads | 2 | 1,22% / 1,00% — 🟢 +22,0% favorable | 0,57 € / 0,80 € — 🟢 −28,8% favorable | 24,21 € / 20,00 € — 🟡 +21,1% desfavorable |
| LinkedIn Ads | 1 | 0,50% / 0,60% — 🟢 −16,7% desfavorable dentro del umbral | 4,00 € / 3,50 € — 🟢 +14,3% desfavorable dentro del umbral | 120,00 € / 80,00 € — 🔴 +50,0% desfavorable |
| TikTok Ads | 1 | 1,50% / 1,00% — 🟢 +50,0% favorable | 0,30 € / 0,50 € — 🟢 −40,0% favorable | n/d / 30,00 € — sin conversiones |

**Lectura del semáforo:** para CTR, un valor superior al objetivo es favorable; para CPC y CPA, un valor inferior es favorable. Verde indica que el objetivo se cumple o que la desviación desfavorable no supera el 20%; amarillo, una desviación desfavorable superior al 20% y hasta el 40%; rojo, más del 40%. Las desviaciones favorables se marcan en verde aunque superen el 20%.

## Ranking por CPA

1. **Search_Reservas_Verano (Google Ads):** 12,50 € — 100 conversiones.
2. **Retargeting_Web (Meta Ads):** 20,00 € — 45 conversiones.
3. **Stories_Escapadas (Meta Ads):** 40,00 € — 12 conversiones.
4. **Eventos_Empresa (LinkedIn Ads):** 120,00 € — 5 conversiones.
5. **Video_Prueba (TikTok Ads):** n/d — 0 conversiones; no comparable por CPA.

## Alertas de datos

- 5 de 5 campañas procesadas; no se observan filas inválidas en el CSV.
- Video_Prueba no registró conversiones. Su CPA es n/d, no cero.
- El análisis usa benchmarks de respaldo local; no se consultó Google Sheets en esta sesión.

## Recomendaciones

1. **Investigar Eventos_Empresa:** su CPA supera el objetivo en 50% y su CPC en 14,3%. Revisar la segmentación y las pujas; comprobar también la calidad de las cinco conversiones antes de cambiar inversión.
2. **Optimizar Stories_Escapadas:** el CTR queda 20% bajo el objetivo y el CPA es el doble del benchmark. Probar nuevas creatividades y audiencias, y revisar la experiencia de conversión.
3. **Diagnosticar Video_Prueba antes de escalar:** aunque el CTR y CPC son favorables, 900 clics sin conversiones pueden indicar desajuste entre anuncio y página, fricción del formulario/reserva o un problema de medición.
4. **Preservar lo que funciona en Search_Reservas_Verano y Retargeting_Web:** documentar sus audiencias y mensajes y probarlos de forma controlada en otras campañas.
5. **Tratar la reasignación de presupuesto como una prueba gradual:** comparar valor y calidad de las conversiones además del CPA antes de mover inversión entre canales.

## Archivos

- KPIs: `output/kpis_campanas_2026-10-21.csv`
- Informe: `output/informe_campanas_2026-10-21_v2.md`
