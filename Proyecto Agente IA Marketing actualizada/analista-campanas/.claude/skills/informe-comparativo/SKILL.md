---
name: informe-comparativo
description: Usa esta skill cuando tengas los KPIs calculados y necesites compararlos con benchmarks y generar un informe ejecutivo.
---

# Skill: Informe Comparativo

Compara los KPIs de campañas con objetivos de benchmarks y genera un informe ejecutivo con recomendaciones.

## Cuándo usar esta skill

- Ya has calculado los KPIs usando la skill `calcular-kpis`
- Tienes acceso a benchmarks (Google Sheets o respaldo local)
- Necesitas generar un informe ejecutivo para el usuario
- Debes proporcionar recomendaciones accionables basadas en los datos

## Pasos a seguir

### 1. Obtener benchmarks
- **Primero**: Intentar obtener benchmarks desde Google Sheets (MCP)
- **Si falla**: Usar `config/benchmarks_respaldo.csv`
- **Registrar**: Indicar en el informe la fuente usada

### 2. Comparar KPIs con objetivos
Para cada campaña y canal:
- **CTR**: Más alto es mejor
- **CPC**: Más bajo es mejor  
- **CPA**: Más bajo es mejor

Calcular desviación porcentual:
```
desviacion = ((valor_real - objetivo) / objetivo) × 100
```

### 3. Asignar semáforo
Basado en el umbral configurado en `memory/preferencias_usuario.md` (20% por defecto):

- 🟢 **Verde**: Cumple con el objetivo (|desviación| ≤ umbral)
- 🟡 **Amarillo**: Desviación moderada (umbral < |desviación| ≤ 2×umbral)
- 🔴 **Rojo**: Desviación significativa (|desviación| > 2×umbral)

### 4. Crear ranking de campañas
1. Ordenar por CPA (menor es mejor)
2. Las campañas sin conversiones (CPA = "n/d") van al final
3. Incluir posición, nombre de campaña, canal y KPIs clave

### 5. Redactar el informe
Seguir la plantilla en `output/informe_campanas_AAAA-MM-DD.md`:

#### A. Resumen ejecutivo (3-5 líneas)
- Período analizado
- Número total de campañas
- Mejor y peor desempeño
- Tendencias principales

#### B. Tabla de KPIs por campaña
- Todas las campañas válidas
- CTR, CPC, CPA calculados
- Comparación con objetivos (semáforo)

#### C. Tabla por canal
- KPIs agregados por canal
- Comparación con benchmarks del canal
- Desviaciones porcentuales

#### D. Ranking de campañas
- Top 5 campañas por CPA
- Campañas problemáticas al final

#### E. Alertas de datos
- Campañas excluidas (con motivos)
- Datos faltantes o inconsistentes
- Advertencias específicas

#### F. Recomendaciones (3-5)
Conectar causa con indicador:
- **CTR bajo** → Revisar creatividades y segmentación
- **CPC alto** → Revisar pujas y palabras clave  
- **CPA alto con buen CTR** → Revisar landing page o proceso
- **Canal con mal desempeño** → Reasignar presupuesto
- **Campaña sin conversiones** → Reevaluar objetivo o segmento

#### G. Metadatos
- Fecha del informe
- Fuente de benchmarks usada
- Archivo de datos analizado
- Umbral de semáforo aplicado

### 6. Guardar resultados
- **Informe**: `output/informe_campanas_AAAA-MM-DD.md`
- **KPIs calculados**: `output/kpis_campanas_AAAA-MM-DD.csv`
- **Si existe archivo con mismo nombre**: Añadir sufijo `_v2`, `_v3`, etc.

## Ejemplo de comparación

**Benchmark Meta Ads:**
- CTR objetivo: 1,00%
- CPC objetivo: 0,80 €
- CPA objetivo: 20,00 €

**Campaña Retargeting_Web:**
- CTR real: 1,50% → +50% → 🟢 (dentro de 20%)
- CPC real: 0,50 € → -37,5% → 🟢 (mejor que objetivo)
- CPA real: 20,00 € → 0% → 🟢 (cumple objetivo)

## Plantilla de recomendaciones

1. **Para CTR bajo (< objetivo):**
   > "El CTR de [Campaña] en [Canal] está [X]% por debajo del objetivo. Recomiendo revisar las creatividades del anuncio, ajustar la segmentación de audiencia o testear diferentes llamadas a la acción."

2. **Para CPC alto (> objetivo):**
   > "El CPC de [Campaña] en [Canal] supera el objetivo en [X]%. Sugiero revisar las pujas por palabra clave, eliminar términos poco relevantes o ajustar la estrategia de puja por conversión."

3. **Para CPA alto (> objetivo):**
   > "Aunque el CTR es bueno, el CPA de [Campaña] está [X]% por encima del objetivo. Esto puede indicar problemas en la landing page o en el proceso de conversión. Recomiendo optimizar el funnel."

4. **Para campaña sin conversiones:**
   > "[Campaña] no ha generado conversiones durante el período analizado. Sugiero reevaluar el objetivo de la campaña, ajustar la segmentación o considerar su suspensión temporal."

5. **Para canal con mal desempeño general:**
   > "El canal [Canal] muestra un desempeño consistentemente por debajo de los benchmarks. Recomiendo reasignar parte del presupuesto a canales mejor desempeñados como [Canal Mejor]."

## Validaciones

✅ **Validaciones antes de generar informe:**
- Todos los KPIs están calculados
- Benchmarks disponibles para todos los canales
- No hay ambigüedades en los datos
- El usuario ha confirmado el archivo a analizar (si hay varios)

✅ **Validaciones del informe:**
- Incluye todas las secciones requeridas
- Los cálculos son consistentes
- Las recomendaciones se basan en datos concretos
- Se indica claramente la fuente de benchmarks