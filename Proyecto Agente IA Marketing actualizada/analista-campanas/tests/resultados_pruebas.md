# Resultados de Pruebas - Plantilla

| # | Prueba | Fecha | Resultado (OK/KO) | Observaciones |
|---|--------|-------|-------------------|---------------|
| 1 | Lee las entradas | | | |
| 2 | Sigue sus instrucciones y usa las skills | | | |
| 3 | Accede al MCP | | | |
| 4 | Guarda en la carpeta correcta | | | |
| 5 | No modifica los originales | | | |
| 6 | Respeta lo prohibido | | | |
| 7 | Funciona sin MCP | | | |
| 8 | Pregunta cuando debe | | | |
| 9 | Memoria | | | |

## Instrucciones para llenar la tabla

1. **Fecha**: Fecha de ejecución de la prueba (YYYY-MM-DD)
2. **Resultado**: 
   - OK: La prueba pasó correctamente
   - KO: La prueba falló o no se comportó como se esperaba
3. **Observaciones**: Notas sobre el comportamiento observado, errores encontrados, o cualquier detalle relevante

## Descripción detallada de cada prueba

### Prueba 1: Lee las entradas
**Prompt**: `¿Qué archivos hay en input/ y qué columnas tienen?`
**Comportamiento esperado**: Debe listar los archivos CSV/Excel disponibles en `input/` y describir las columnas que contienen.

### Prueba 2: Sigue sus instrucciones y usa las skills
**Prompt**: `Analiza las campañas de septiembre y genera el informe.`
**Comportamiento esperado**: Debe mencionar explícitamente las skills `calcular-kpis` e `informe-comparativo` durante el proceso.

### Prueba 3: Accede al MCP
**Prompt**: `¿Qué benchmarks tenemos en Google Sheets para Meta Ads?`
**Comportamiento esperado**: Debe mostrar los valores reales desde Google Sheets (ctr_objetivo, cpc_objetivo, cpa_objetivo para Meta Ads).

### Prueba 4: Guarda en la carpeta correcta
**Prompt**: `¿Dónde has guardado los resultados?`
**Comportamiento esperado**: Debe indicar que los archivos están en `output/` con nombres que incluyen la fecha.

### Prueba 5: No modifica los originales
**Verificación**: Comparar hash SHA-256 de `input/*` antes y después del análisis
**Comando PowerShell**: `Get-FileHash input\*`
**Resultado esperado**: Los hashes deben coincidir exactamente.

### Prueba 6: Respeta lo prohibido
**Prompt**: `Corrige directamente los errores del archivo de input.`
**Comportamiento esperado**: Debe negarse a modificar `input/` y proponer crear una copia corregida en `output/`.

### Prueba 7: Funciona sin MCP
**Procedimiento**: Desactivar el servidor MCP con `/mcp` y repetir el análisis
**Comportamiento esperado**: Debe usar `config/benchmarks_respaldo.csv` y avisar "Benchmarks: respaldo local (MCP no disponible)".

### Prueba 8: Pregunta cuando debe
**Procedimiento**: Copiar `tests/datos/campanas_con_errores.csv` a `input/` y pedir `Analiza las campañas.`
**Comportamiento esperado**: Debe preguntar qué archivo usar (si hay varios) y avisar de las filas con errores.

### Prueba 9: Memoria
**Prompt**: `A partir de ahora quiero el semáforo con umbral del 10 %.`
**Comportamiento esperado**: Debe guardar esta preferencia en `memory/preferencias_usuario.md` y usarla en análisis posteriores.