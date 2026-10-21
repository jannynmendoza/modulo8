# Resultados Esperados - Archivo campanas_ejemplo.csv

## KPIs por Campaña

| Campaña | Canal | CTR | CPC | CPA |
|---------|-------|-----|-----|-----|
| Search_Reservas_Verano | Google Ads | 5,00 % | 0,50 € | 12,50 € |
| Retargeting_Web | Meta Ads | 1,50 % | 0,50 € | 20,00 € |
| Stories_Escapadas | Meta Ads | 0,80 % | 0,75 € | 40,00 € |
| Eventos_Empresa | LinkedIn Ads | 0,50 % | 4,00 € | 120,00 € |
| Video_Prueba | TikTok Ads | 1,50 % | 0,30 € | n/d (sin conversiones) |

## KPIs Agregados por Canal

| Canal | Impresiones | Clics | Coste | Conversiones | CTR | CPC | CPA |
|-------|-------------|-------|-------|--------------|-----|-----|-----|
| Google Ads | 50.000 | 2.500 | 1.250 € | 100 | 5,00 % | 0,50 € | 12,50 € |
| Meta Ads | 200.000 | 2.440 | 1.380 € | 57 | 1,22 % | 0,57 € | 24,21 € |
| LinkedIn Ads | 30.000 | 150 | 600 € | 5 | 0,50 % | 4,00 € | 120,00 € |
| TikTok Ads | 60.000 | 900 | 270 € | 0 | 1,50 % | 0,30 € | n/d |

## Cálculos Detallados

### Search_Reservas_Verano (Google Ads)
- CTR: (2.500 / 50.000) × 100 = 5,00 %
- CPC: 1.250 € / 2.500 = 0,50 €
- CPA: 1.250 € / 100 = 12,50 €

### Retargeting_Web (Meta Ads)
- CTR: (1.800 / 120.000) × 100 = 1,50 %
- CPC: 900 € / 1.800 = 0,50 €
- CPA: 900 € / 45 = 20,00 €

### Stories_Escapadas (Meta Ads)
- CTR: (640 / 80.000) × 100 = 0,80 %
- CPC: 480 € / 640 = 0,75 €
- CPA: 480 € / 12 = 40,00 €

### Eventos_Empresa (LinkedIn Ads)
- CTR: (150 / 30.000) × 100 = 0,50 %
- CPC: 600 € / 150 = 4,00 €
- CPA: 600 € / 5 = 120,00 €

### Video_Prueba (TikTok Ads)
- CTR: (900 / 60.000) × 100 = 1,50 %
- CPC: 270 € / 900 = 0,30 €
- CPA: 270 € / 0 = n/d (división por cero)

### Meta Ads Agregado
- Impresiones totales: 120.000 + 80.000 = 200.000
- Clics totales: 1.800 + 640 = 2.440
- Coste total: 900 € + 480 € = 1.380 €
- Conversiones totales: 45 + 12 = 57
- CTR agregado: (2.440 / 200.000) × 100 = 1,22 %
- CPC agregado: 1.380 € / 2.440 = 0,57 €
- CPA agregado: 1.380 € / 57 = 24,21 €

## Alertas Esperadas

1. **Video_Prueba**: Campaña sin conversiones (CPA = n/d)
2. **Meta Ads agregado**: CTR de 1,22 % vs objetivo de 1,00 % (desviación +22 %)
3. **LinkedIn Ads**: CPC de 4,00 € vs objetivo de 3,50 € (desviación +14,29 %)