# Ejercicio 3: Analista de campañas (CTR, CPC, CPA) con Claude Code

Herramienta elegida: **Claude Code** (funciona sobre una carpeta local).
Fuente externa por defecto: **Google Sheets en Google Drive**, mediante un MCP. Si preferís otra (Excel, una base de datos), solo cambia la sección del MCP.

## Cómo usar este documento

1. Enviad al profesor el texto de la **Parte 1** y esperad la aprobación.
2. Cread una carpeta vacía (por ejemplo `analista-campanas`), abridla en Claude Code y pegad el **prompt maestro** de la **Parte 2**.
3. Cread en Google Drive la hoja de benchmarks descrita en la **Parte 3** y conectad el MCP.
4. Lanzad los **prompts de prueba** de la **Parte 4** y rellenad `tests/resultados_pruebas.md`.
5. Revisad la **checklist de entrega** de la **Parte 5** antes de crear el ZIP.

---

## Parte 1. Propuesta para el profesor (texto listo para enviar)

> **Propuesta de proyecto agéntico: Analista de campañas de marketing**
>
> **Herramienta:** Claude Code, trabajando sobre una carpeta local.
>
> **Problema que resolvemos:** los equipos de marketing reciben exportaciones de sus plataformas de anuncios (Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads) en archivos separados y tardan en calcular y comparar los indicadores clave. Sin una comparación homogénea es difícil saber qué campaña rinde mejor y dónde se está gastando de más.
>
> **Usuario:** un responsable o técnico de marketing digital (por ejemplo, del departamento de marketing de un hotel) sin conocimientos de programación, que quiere saber qué campañas funcionan y cuáles hay que optimizar.
>
> **Información que recibirá:** un archivo CSV o Excel por periodo con los datos de cada campaña (campaña, canal, fechas, impresiones, clics, coste y conversiones), que el usuario deja en la carpeta `input/`. Además, consultará en Google Sheets una hoja con los objetivos y benchmarks de CTR, CPC y CPA por canal.
>
> **Resultado que generará:** en la carpeta `output/`, un informe comparativo en Markdown con el ranking de campañas, un semáforo frente a los objetivos y recomendaciones, y un CSV con los indicadores calculados. Nunca modificará los archivos originales.
>
> **Skills:**
> 1. `calcular-kpis`: valida los datos y calcula CTR, CPC y CPA de cada campaña y canal.
> 2. `informe-comparativo`: compara los resultados con los benchmarks, ordena las campañas y redacta el informe con recomendaciones.
>
> **MCP:** servidor MCP de Google Sheets/Drive en modo solo lectura, para consultar la hoja de objetivos y benchmarks. Si la conexión falla, el agente usará una copia local de respaldo y lo indicará en el informe.

---

## Parte 2. Prompt maestro para crear el proyecto

Pegadlo completo en Claude Code dentro de la carpeta vacía del proyecto.

````text
Quiero que crees en esta carpeta un proyecto agéntico local para Claude Code. Es un ejercicio de clase: otro equipo descomprimirá el ZIP y deberá poder entenderlo y probarlo sin nuestra ayuda. Todo el contenido debe estar en español, ser claro y no incluir contraseñas, claves ni datos sensibles.

## Rol del agente
Eres un analista de mercado especializado en campañas de marketing digital. Comparas los resultados de las campañas mediante tres indicadores:
- CTR (Click Through Rate) = clics / impresiones × 100 (en %).
- CPC (Coste por clic) = coste / clics (en €).
- CPA (Coste por adquisición) = coste / conversiones (en €).

## 1. Estructura de carpetas que debes crear
analista-campanas/
├── CLAUDE.md                      # instrucciones del agente (Claude Code lo carga automáticamente)
├── README.md                      # guía para quien recibe el ZIP
├── .mcp.json                      # configuración del MCP de Google Sheets (sin credenciales)
├── .env.example                   # variables necesarias, con valores de ejemplo
├── .gitignore                     # excluye .env, credenciales/ y output/*
├── .claude/
│   ├── settings.json              # permisos: proteger input/ y bloquear acciones de escritura del MCP
│   └── skills/
│       ├── calcular-kpis/SKILL.md
│       └── informe-comparativo/SKILL.md
├── skills/                        # copia visible de las skills para la entrega y documentación
│   ├── README.md
│   ├── calcular-kpis/SKILL.md
│   └── informe-comparativo/SKILL.md
├── scripts/
│   └── calcular_kpis.py           # cálculo reproducible (solo librería estándar de Python)
├── input/                         # datos de entrada del usuario (solo lectura para el agente)
│   └── campanas_2026_09.csv
├── output/                        # resultados generados por el agente
│   └── .gitkeep
├── memory/
│   ├── README.md                  # qué se puede y qué no se puede guardar
│   ├── preferencias_usuario.md
│   └── historial_analisis.md
├── config/
│   └── benchmarks_respaldo.csv    # copia local de la hoja de Google Sheets para cuando falle el MCP
├── docs/
│   ├── arquitectura_claude_code.md
│   └── mcp_google_sheets.md
└── tests/
    ├── README.md
    ├── datos/
    │   ├── campanas_ejemplo.csv
    │   └── campanas_con_errores.csv
    ├── resultados_esperados.md
    ├── test_calcular_kpis.py
    └── resultados_pruebas.md      # plantilla para anotar las pruebas

## 2. docs/arquitectura_claude_code.md
Explica brevemente, basándote en la documentación oficial de Claude Code (https://docs.claude.com/en/docs/claude-code), cómo organiza Claude Code cada elemento y cómo lo hemos aplicado:
| Elemento | Cómo lo organiza Claude Code | Dónde está en nuestro proyecto |
- Instrucciones del agente: archivo CLAUDE.md en la raíz, que se carga al iniciar la sesión.
- Entradas y salidas: no hay carpetas fijas; las definimos en CLAUDE.md (input/ y output/).
- Memoria: CLAUDE.md (memoria de proyecto) y archivos importados con @ruta; nosotros añadimos memory/.
- Skills: carpetas con SKILL.md en .claude/skills/ (con nombre y descripción en el encabezado YAML); la copia en skills/ es para la entrega.
- MCP: archivo .mcp.json en la raíz (ámbito de proyecto) y comando /mcp para ver el estado.
- Permisos: .claude/settings.json con reglas allow/deny.
- Pruebas: Claude Code no trae un sistema de pruebas propio; usamos datos de ejemplo, resultados esperados, un test en Python y una checklist manual.
Si alguna ruta o funcionalidad ha cambiado en la documentación actual, corrígela y anótalo.

## 3. CLAUDE.md (contenido obligatorio)
Redáctalo en segunda persona dirigido al agente, con estos apartados:

### Objetivo
Analizar los resultados de las campañas de marketing que el usuario deja en input/, calcular CTR, CPC y CPA, compararlos entre campañas, entre canales y frente a los objetivos de la hoja de benchmarks de Google Sheets, y generar un informe con recomendaciones accionables.

### Usuario
Responsable o técnico de marketing digital sin conocimientos de programación. Lenguaje claro, sin jerga técnica innecesaria, explicando qué significa cada indicador la primera vez.

### Entradas
- input/*.csv o *.xlsx con columnas: campana, canal, fecha_inicio, fecha_fin, impresiones, clics, coste, conversiones (coste en euros).
- Hoja de Google Sheets "Benchmarks campañas" (vía MCP, solo lectura) con columnas: canal, ctr_objetivo, cpc_objetivo, cpa_objetivo.
- config/benchmarks_respaldo.csv si el MCP no está disponible.
- memory/preferencias_usuario.md para adaptar el informe.

### Salidas (siempre en output/)
- output/informe_campanas_AAAA-MM-DD.md: resumen ejecutivo (3-5 líneas), tabla de KPIs por campaña, tabla por canal, comparación con objetivos con semáforo (🟢 cumple, 🟡 desviación ≤ 20 %, 🔴 desviación > 20 %), ranking de campañas, alertas de datos y 3-5 recomendaciones. Indica al final la fuente de benchmarks usada (Google Sheets o respaldo local) y la fecha.
- output/kpis_campanas_AAAA-MM-DD.csv con los indicadores calculados.
- Si ya existe un archivo con el mismo nombre, añade un sufijo _v2, _v3… en lugar de sobrescribirlo.

### Proceso
1. Lee memory/preferencias_usuario.md.
2. Lista los archivos de input/. Si hay varios y el usuario no dijo cuál, pregunta.
3. Usa la skill calcular-kpis para validar los datos y calcular los indicadores (con scripts/calcular_kpis.py).
4. Consulta los benchmarks con el MCP de Google Sheets. Si falla, usa config/benchmarks_respaldo.csv y avísalo.
5. Usa la skill informe-comparativo para comparar y redactar el informe.
6. Guarda los resultados en output/.
7. Actualiza memory/historial_analisis.md con un resumen de una línea.
8. Muestra al usuario un resumen breve y la ruta de los archivos generados.

### Lo que puede hacer
- Leer archivos de input/, config/, memory/ y tests/datos/.
- Ejecutar scripts/calcular_kpis.py.
- Consultar (solo leer) la hoja de benchmarks mediante el MCP.
- Crear archivos en output/ y actualizar los archivos de memory/.

### Lo que no puede hacer
- Modificar, renombrar o borrar archivos de input/ (son los originales del usuario).
- Escribir, editar, compartir o borrar nada en Google Drive o Google Sheets.
- Inventar datos, benchmarks o conversiones que no estén en las fuentes.
- Guardar credenciales, claves o datos personales en ningún archivo.
- Tomar decisiones de presupuesto: solo recomienda; la decisión es del usuario.

### Cuándo preguntar al usuario
- Hay varios archivos en input/ y no está claro cuál analizar.
- Faltan columnas obligatorias o los nombres no coinciden y no se pueden mapear sin ambigüedad.
- Más del 20 % de las filas tienen errores.
- Un canal no tiene benchmark ni en Google Sheets ni en el respaldo.
- La moneda o el periodo no están claros.

### Cuándo dar por terminado el trabajo
Cuando: los dos archivos existen en output/; todas las campañas válidas tienen CTR, CPC y CPA (o "n/d" justificado); el informe indica la fuente de benchmarks; las filas descartadas están listadas con su motivo; el historial de memoria está actualizado; y input/ no ha cambiado.

### Memoria
- Puede guardar: preferencias del usuario (formato, nivel de detalle, umbrales del semáforo, canales prioritarios) y un historial con fecha, archivo analizado, nº de campañas y mejor/peor campaña.
- No puede guardar: datos personales, credenciales, IDs privados de documentos ni copias completas de los datos de campaña.

## 4. Skills
Cada SKILL.md debe tener un encabezado YAML con `name` y `description` (la descripción debe decir cuándo usarla) y después instrucciones paso a paso, ejemplo de entrada y de salida. Crea las dos en .claude/skills/ y copia idéntica en skills/. En skills/README.md explica por qué hay dos copias.

### Skill 1: calcular-kpis
- Valida el archivo: columnas obligatorias, números no negativos, clics ≤ impresiones, conversiones ≤ clics, filas sin valores vacíos.
- Las filas con errores no se corrigen: se excluyen y se listan con su motivo.
- Calcula CTR, CPC y CPA por campaña y agregados por canal (sumando impresiones, clics, coste y conversiones antes de dividir, nunca promediando ratios).
- Casos límite: si clics = 0, CPC = "n/d"; si conversiones = 0, CPA = "n/d" y genera una alerta "campaña sin conversiones"; si impresiones = 0, CTR = "n/d".
- Redondeo: CTR con 2 decimales (%), CPC y CPA con 2 decimales (€).
- Usa scripts/calcular_kpis.py: `python scripts/calcular_kpis.py <archivo_entrada> <archivo_salida_csv>`. Solo librería estándar (csv, argparse). Si el archivo es .xlsx, pide al usuario que lo exporte a CSV o usa openpyxl solo si está instalado.

### Skill 2: informe-comparativo
- Compara cada campaña y canal con su benchmark: para CTR más alto es mejor; para CPC y CPA más bajo es mejor.
- Calcula la desviación en % frente al objetivo y asigna el semáforo.
- Ranking por CPA (menor es mejor); las campañas sin conversiones van al final.
- Redacta las recomendaciones conectando la causa con el indicador (ej.: CTR bajo → revisar creatividades y segmentación; CPC alto → revisar pujas y palabras clave; CPA alto con buen CTR → revisar landing page o proceso de reserva).
- Usa la plantilla del informe descrita en CLAUDE.md.

## 5. MCP de Google Sheets
- En .mcp.json configura un servidor llamado "google-sheets" usando el paquete comunitario mcp-google-sheets (https://github.com/xing5/mcp-google-sheets), lanzado con `uvx mcp-google-sheets@latest`, con autenticación por cuenta de servicio. Las rutas e IDs deben venir de variables de entorno con la sintaxis ${VARIABLE} de Claude Code, nunca escritos a mano. Comprueba en el README del paquete el nombre exacto de las variables (por ejemplo SERVICE_ACCOUNT_PATH y DRIVE_FOLDER_ID).
- En .env.example pon esas variables con valores ficticios.
- En .claude/settings.json:
  - deny: Edit y Write sobre ./input/**, Read de ./.env y ./credenciales/**.
  - deny de las herramientas del MCP que escriben, crean, comparten o borran (por ejemplo las que contengan update, create, batch_update, share, add_rows, add_columns, copy, rename). Ejecuta /mcp o revisa la documentación del paquete para obtener los nombres exactos con el formato mcp__google-sheets__<herramienta> y escríbelos.
  - allow: herramientas de lectura del MCP y `Bash(python scripts/calcular_kpis.py:*)`.
- En docs/mcp_google_sheets.md documenta:
  1. Qué sistema conecta: Google Sheets/Drive.
  2. Qué información puede consultar: la hoja "Benchmarks campañas" (canal, ctr_objetivo, cpc_objetivo, cpa_objetivo).
  3. Qué acciones puede realizar: listar hojas de la carpeta compartida y leer celdas.
  4. Qué permisos necesita: una cuenta de servicio de Google Cloud con las APIs de Sheets y Drive activadas, y la hoja compartida con esa cuenta como "Lector".
  5. Qué acciones tiene prohibidas: escribir, crear, borrar, compartir o mover archivos (bloqueadas en settings.json y por el permiso de lector).
  6. Qué hacer si la conexión falla: reintentar una vez, usar config/benchmarks_respaldo.csv, indicar en el informe "Benchmarks: respaldo local (MCP no disponible)" y explicar al usuario cómo revisar la conexión con /mcp.
  7. Paso a paso para configurarlo (crear proyecto en Google Cloud, activar APIs, crear cuenta de servicio, descargar el JSON a credenciales/ fuera del ZIP, compartir la hoja, rellenar .env, reiniciar Claude Code y comprobar con /mcp).
  8. Alternativa sin Google Cloud: el conector de Google Drive de la app de Claude, o trabajar solo con el respaldo local.

## 6. Datos de ejemplo
input/campanas_2026_09.csv y tests/datos/campanas_ejemplo.csv con este contenido exacto (campañas de un hotel; conversiones = reservas):
campana,canal,fecha_inicio,fecha_fin,impresiones,clics,coste,conversiones
Search_Reservas_Verano,Google Ads,2026-09-01,2026-09-30,50000,2500,1250,100
Retargeting_Web,Meta Ads,2026-09-01,2026-09-30,120000,1800,900,45
Stories_Escapadas,Meta Ads,2026-09-01,2026-09-30,80000,640,480,12
Eventos_Empresa,LinkedIn Ads,2026-09-01,2026-09-30,30000,150,600,5
Video_Prueba,TikTok Ads,2026-09-01,2026-09-30,60000,900,270,0

tests/datos/campanas_con_errores.csv: incluye una fila válida, una con clics > impresiones, una con coste negativo, una con un valor vacío y una con conversiones > clics.

config/benchmarks_respaldo.csv (valores didácticos, no benchmarks reales del sector; indícalo en un comentario del README):
canal,ctr_objetivo,cpc_objetivo,cpa_objetivo
Google Ads,3.00,1.00,25.00
Meta Ads,1.00,0.80,20.00
LinkedIn Ads,0.60,3.50,80.00
TikTok Ads,1.00,0.50,30.00

## 7. Pruebas
- tests/resultados_esperados.md con los valores correctos del archivo de ejemplo:
  - Search_Reservas_Verano: CTR 5,00 %, CPC 0,50 €, CPA 12,50 €
  - Retargeting_Web: CTR 1,50 %, CPC 0,50 €, CPA 20,00 €
  - Stories_Escapadas: CTR 0,80 %, CPC 0,75 €, CPA 40,00 €
  - Eventos_Empresa: CTR 0,50 %, CPC 4,00 €, CPA 120,00 €
  - Video_Prueba: CTR 1,50 %, CPC 0,30 €, CPA n/d (alerta sin conversiones)
  - Canal Meta Ads agregado: CTR 1,22 %, CPC 0,57 €, CPA 24,21 €
  Comprueba tú mismo estos valores con el script y corrige cualquier discrepancia.
- tests/test_calcular_kpis.py: test con unittest (solo librería estándar) que ejecute el cálculo sobre los dos archivos de tests/datos/ y compruebe los valores esperados y que las 4 filas erróneas se excluyen.
- tests/README.md con la tabla de pruebas: Prueba | Qué comprueba | Cómo se ejecuta | Resultado esperado, cubriendo: 1) lee las entradas, 2) sigue las instrucciones, 3) usa las skills, 4) accede al MCP, 5) guarda en output/, 6) no modifica input/ (comparar hash SHA-256 antes y después), 7) funciona con el MCP desconectado, 8) pregunta cuando hay datos ambiguos.
- tests/resultados_pruebas.md: plantilla vacía con las mismas 8 pruebas y columnas Fecha | Resultado (OK/KO) | Observaciones.

## 8. memory/
- README.md con las reglas de memoria de CLAUDE.md.
- preferencias_usuario.md con valores por defecto: idioma español, moneda €, umbral del semáforo 20 %, informe con resumen ejecutivo al principio.
- historial_analisis.md vacío con encabezado de tabla: Fecha | Archivo | Nº campañas | Mejor campaña (CPA) | Peor campaña (CPA) | Fuente benchmarks.

## 9. README.md
Para alguien que no nos conoce: qué hace el proyecto, requisitos (Claude Code, Python 3, uv para el MCP), estructura de carpetas, instalación paso a paso, cómo configurar el MCP (enlace a docs/mcp_google_sheets.md), cómo usarlo sin MCP, ejemplos de prompts para el usuario ("Analiza las campañas de septiembre", "¿Qué canal tiene el mejor CPA?"), cómo ejecutar las pruebas (`python -m unittest discover tests`), limitaciones conocidas y cómo crear el ZIP sin .env ni credenciales/. Incluye un glosario de CTR, CPC y CPA.

## 10. Al terminar
1. Ejecuta los tests y muéstrame el resultado.
2. Ejecuta un análisis completo de input/campanas_2026_09.csv usando el respaldo local de benchmarks y guarda el resultado en output/.
3. Comprueba que input/ no ha cambiado.
4. Muéstrame el árbol final de carpetas y una lista de lo que tengo que hacer yo manualmente (configurar Google Cloud, crear la hoja, rellenar .env).
````

---

## Parte 3. Hoja de Google Sheets que tenéis que crear

1. En Google Drive, cread una carpeta `Analista campañas` y dentro una hoja de cálculo llamada **Benchmarks campañas**.
2. Copiad en ella el mismo contenido que `config/benchmarks_respaldo.csv` (canal, ctr_objetivo, cpc_objetivo, cpa_objetivo).
3. Compartid la carpeta con el correo de la cuenta de servicio como **Lector**.
4. Seguid el paso a paso de `docs/mcp_google_sheets.md` para rellenar el `.env` y comprobad con `/mcp` en Claude Code que el servidor aparece conectado.

Consejo para la prueba del MCP: cambiad un valor en la hoja de Google (por ejemplo el CPA objetivo de Meta Ads a 22,00). Si el informe usa 22,00 y no 20,00, queda demostrado que el agente lee la fuente externa y no el respaldo.

---

## Parte 4. Prompts de prueba (lanzadlos uno a uno en Claude Code)

| # | Qué comprueba | Prompt |
|---|---|---|
| 1 | Lee las entradas | `¿Qué archivos hay en input/ y qué columnas tienen?` |
| 2 | Sigue sus instrucciones y usa las skills | `Analiza las campañas de septiembre y genera el informe.` (debe mencionar las skills calcular-kpis e informe-comparativo) |
| 3 | Accede al MCP | `¿Qué benchmarks tenemos en Google Sheets para Meta Ads?` |
| 4 | Guarda en la carpeta correcta | `¿Dónde has guardado los resultados?` (deben estar en `output/`) |
| 5 | No modifica los originales | Antes y después del análisis: `sha256sum input/*` (en Windows: `Get-FileHash input\*`). Los hashes deben coincidir. |
| 6 | Respeta lo prohibido | `Corrige directamente los errores del archivo de input.` (debe negarse y proponer una copia en output/) |
| 7 | Funciona sin MCP | Desactivad el servidor con `/mcp` y repetid el prompt 2 (debe usar el respaldo y avisarlo) |
| 8 | Pregunta cuando debe | Copiad `tests/datos/campanas_con_errores.csv` a `input/` y pedid `Analiza las campañas.` (debe preguntar qué archivo usar y avisar de las filas con errores) |
| 9 | Memoria | `A partir de ahora quiero el semáforo con umbral del 10 %.` y comprobad que se guarda en `memory/preferencias_usuario.md` |

Anotad cada resultado en `tests/resultados_pruebas.md`.

---

## Parte 5. Checklist de entrega (ZIP)

- [ ] El README explica la instalación y el uso sin necesidad de preguntaros nada.
- [ ] No hay `.env`, ni JSON de la cuenta de servicio, ni carpeta `credenciales/` (solo `.env.example`).
- [ ] No hay IDs reales de carpetas o documentos de Drive en ningún archivo.
- [ ] `output/` está vacío (o solo con un informe de ejemplo, si lo queréis mostrar).
- [ ] `memory/historial_analisis.md` está vacío o solo con datos de ejemplo.
- [ ] Los tests pasan: `python -m unittest discover tests`.
- [ ] `tests/resultados_pruebas.md` está rellenado.
- [ ] Comprimid la carpeta: `zip -r analista-campanas.zip analista-campanas -x "*/.env" "*/credenciales/*"` (en Windows: clic derecho > Comprimir, tras borrar `.env` y `credenciales/`).

Para la reflexión final (qué habéis creado, qué habéis aprendido, dónde os habéis bloqueado, qué descubrió el otro equipo y qué mejoraríais), id anotando durante el trabajo los bloqueos reales; la configuración de Google Cloud y los permisos del MCP suelen ser el punto más difícil y dan buen material para la presentación.
