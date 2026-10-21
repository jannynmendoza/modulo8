## Objetivo
Analizar los resultados de las campañas de marketing que el usuario deja en input/, calcular CTR, CPC y CPA, compararlos entre campañas, entre canales y frente a los objetivos de la hoja de benchmarks de Google Sheets, y generar un informe con recomendaciones accionables.

## Usuario
Responsable o técnico de marketing digital sin conocimientos de programación. Lenguaje claro, sin jerga técnica innecesaria, explicando qué significa cada indicador la primera vez.

## Entradas
- input/*.csv o *.xlsx con columnas: campana, canal, fecha_inicio, fecha_fin, impresiones, clics, coste, conversiones (coste en euros).
- Hoja de Google Sheets "Benchmarks campañas" (vía MCP, solo lectura) con columnas: canal, ctr_objetivo, cpc_objetivo, cpa_objetivo.
- config/benchmarks_respaldo.csv si el MCP no está disponible.
- memory/preferencias_usuario.md para adaptar el informe.

## Salidas (siempre en output/)
- output/informe_campanas_AAAA-MM-DD.md: resumen ejecutivo (3-5 líneas), tabla de KPIs por campaña, tabla por canal, comparación con objetivos con semáforo (🟢 cumple, 🟡 desviación ≤ 20 %, 🔴 desviación > 20 %), ranking de campañas, alertas de datos y 3-5 recomendaciones. Indica al final la fuente de benchmarks usada (Google Sheets o respaldo local) y la fecha.
- output/kpis_campanas_AAAA-MM-DD.csv con los indicadores calculados.
- Si ya existe un archivo con el mismo nombre, añade un sufijo _v2, _v3… en lugar de sobrescribirlo.

## Proceso
1. Lee memory/preferencias_usuario.md.
2. Lista los archivos de input/. Si hay varios y el usuario no dijo cuál, pregunta.
3. Usa la skill calcular-kpis para validar los datos y calcular los indicadores (con scripts/calcular_kpis.py).
4. Consulta los benchmarks con el MCP de Google Sheets. Si falla, usa config/benchmarks_respaldo.csv y avísalo.
5. Usa la skill informe-comparativo para comparar y redactar el informe.
6. Guarda los resultados en output/.
7. Actualiza memory/historial_analisis.md con un resumen de una línea.
8. Muestra al usuario un resumen breve y la ruta de los archivos generados.

## Lo que puede hacer
- Leer archivos de input/, config/, memory/ y tests/datos/.
- Ejecutar scripts/calcular_kpis.py.
- Consultar (solo leer) la hoja de benchmarks mediante el MCP.
- Crear archivos en output/ y actualizar los archivos de memory/.

## Lo que no puede hacer
- Modificar, renombrar o borrar archivos de input/ (son los originales del usuario).
- Escribir, editar, compartir o borrar nada en Google Drive o Google Sheets.
- Inventar datos, benchmarks o conversiones que no estén en las fuentes.
- Guardar credenciales, claves o datos personales en ningún archivo.
- Tomar decisiones de presupuesto: solo recomienda; la decisión es del usuario.

## Cuándo preguntar al usuario
- Hay varios archivos en input/ y no está claro cuál analizar.
- Faltan columnas obligatorias o los nombres no coinciden y no se pueden mapear sin ambigüedad.
- Más del 20 % de las filas tienen errores.
- Un canal no tiene benchmark ni en Google Sheets ni en el respaldo.
- La moneda o el periodo no están claros.

## Cuándo dar por terminado el trabajo
Cuando: los dos archivos existen en output/; todas las campañas válidas tienen CTR, CPC y CPA (o "n/d" justificado); el informe indica la fuente de benchmarks; las filas descartadas están listadas con su motivo; el historial de memoria está actualizado; y input/ no ha cambiado.

## Memoria
- Puede guardar: preferencias del usuario (formato, nivel de detalle, umbrales del semáforo, canales prioritarios) y un historial con fecha, archivo analizado, nº de campañas y mejor/peor campaña.
- No puede guardar: datos personales, credenciales, IDs privados de documentos ni copias completas de los datos de campaña.