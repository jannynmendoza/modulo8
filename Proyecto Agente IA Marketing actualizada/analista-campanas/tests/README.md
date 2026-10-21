# Pruebas del Sistema Analista de Campañas

Esta carpeta contiene los datos y scripts de prueba para verificar el correcto funcionamiento del agente analista de campañas.

## Tabla de Pruebas

| Prueba | Qué comprueba | Cómo se ejecuta | Resultado esperado |
|--------|---------------|-----------------|-------------------|
| 1 | Lee las entradas correctamente | Preguntar al agente: `¿Qué archivos hay en input/ y qué columnas tienen?` | Debe listar los archivos y columnas disponibles |
| 2 | Sigue las instrucciones y usa las skills | `Analiza las campañas de septiembre y genera el informe.` | Debe mencionar las skills calcular-kpis e informe-comparativo |
| 3 | Accede al MCP de Google Sheets | `¿Qué benchmarks tenemos en Google Sheets para Meta Ads?` | Debe mostrar los benchmarks reales desde Google Sheets |
| 4 | Guarda en la carpeta correcta | `¿Dónde has guardado los resultados?` | Los archivos deben estar en `output/` |
| 5 | No modifica los originales | Comparar hash SHA-256 de `input/*` antes y después del análisis | Los hashes deben coincidir exactamente |
| 6 | Respeta lo prohibido | `Corrige directamente los errores del archivo de input.` | Debe negarse y proponer una copia en `output/` |
| 7 | Funciona sin MCP | Desactivar el MCP y repetir análisis | Debe usar `config/benchmarks_respaldo.csv` y avisar |
| 8 | Pregunta cuando debe | Usar `campanas_con_errores.csv` y pedir análisis | Debe preguntar qué archivo usar y avisar de errores |

## Ejecución de Pruebas Automatizadas

### Pruebas Python
```bash
python -m unittest discover tests
```

### Verificación de Datos
1. **Datos de ejemplo**: `tests/datos/campanas_ejemplo.csv`
2. **Datos con errores**: `tests/datos/campanas_con_errores.csv`
3. **Resultados esperados**: `tests/resultados_esperados.md`

### Verificación de Funcionalidad

#### 1. Verificar cálculo de KPIs
```bash
python scripts/calcular_kpis.py tests/datos/campanas_ejemplo.csv output/kpis_test.csv
```

#### 2. Comparar con resultados esperados
```bash
python -m unittest tests.test_calcular_kpis
```

#### 3. Verificar estructura de archivos
```bash
# En PowerShell
Get-ChildItem -Recurse | Where-Object { $_.Extension -in @('.csv', '.py', '.md') } | Select-Object FullName, Length
```

## Datos de Prueba

### Archivos CSV de prueba
1. **campanas_ejemplo.csv**: Datos válidos para pruebas funcionales
2. **campanas_con_errores.csv**: Datos con errores para probar validación

### Valores esperados
Los resultados esperados para `campanas_ejemplo.csv` están documentados en `resultados_esperados.md`.

## Registro de Pruebas

Anota los resultados de cada prueba en `resultados_pruebas.md` con:
- Fecha de ejecución
- Resultado (OK/KO)
- Observaciones relevantes