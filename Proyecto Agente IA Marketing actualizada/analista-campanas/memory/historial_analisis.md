# Historial de Análisis

| Fecha | Archivo | Nº campañas | Mejor campaña (CPA) | Peor campaña (CPA) | Fuente benchmarks |
|-------|---------|-------------|---------------------|--------------------|-------------------|
| 2026-10-21 | campanas_2026_09.csv | 5 | Search_Reservas_Verano (12,50 €) | Eventos_Empresa (120,00 €) | Google Sheets |
| 2026-10-21 | campanas_2026_09.csv | 5 | Search_Reservas_Verano (12,50 €) | Eventos_Empresa (120,00 €) | Respaldo local |
| | | | | | |

## Formato de la tabla

- **Fecha**: Fecha del análisis (2026-20-21)
- **Archivo**: Nombre del archivo analizado en `input/`
- **Nº campañas**: Cantidad de campañas válidas procesadas
- **Mejor campaña**: Nombre de la campaña con menor CPA (excluyendo "n/d")
- **Peor campaña**: Nombre de la campaña con mayor CPA válido
- **Fuente benchmarks**: "Google Sheets" o "Respaldo local"

## Ejemplo de entrada

| Fecha | Archivo | Nº campañas | Mejor campaña (CPA) | Peor campaña (CPA) | Fuente benchmarks |
|-------|---------|-------------|---------------------|--------------------|-------------------|
| 2026-09-15 | campanas_2026_09.csv | 5 | Search_Reservas_Verano (12,50 €) | Eventos_Empresa (120,00 €) | Respaldo local |

## Notas

- Solo se registran análisis completados exitosamente
- Las campañas con CPA "n/d" no se consideran para mejor/peor
- Si todas las campañas tienen CPA "n/d", se registra "Sin CPA válido"
