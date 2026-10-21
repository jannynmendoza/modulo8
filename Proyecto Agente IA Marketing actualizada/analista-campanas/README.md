# Analista de Campañas de Marketing

Un agente de Claude Code especializado en análisis de campañas de marketing digital. Calcula indicadores clave (CTR, CPC, CPA) y genera informes comparativos con benchmarks.

## ¿Qué hace este proyecto?

Analiza los resultados de campañas de marketing desde archivos CSV o Excel, calcula indicadores clave y los compara con objetivos de rendimiento. Genera informes ejecutivos con recomendaciones accionables.

## Requisitos

- Claude Code instalado
- Python 3.8 o superior
- uv (para el MCP de Google Sheets, opcional)

## Estructura de carpetas

```
analista-campanas/
├── CLAUDE.md                      # Instrucciones del agente
├── README.md                      # Esta guía
├── .mcp.json                      # Configuración del MCP de Google Sheets
├── .env.example                   # Variables de entorno de ejemplo
├── .gitignore                     # Archivos excluidos
├── .claude/                       # Configuración de Claude Code
│   ├── settings.json              # Permisos y configuración
│   └── skills/                    # Skills del agente
├── skills/                        # Copia visible de las skills
├── scripts/                       # Scripts Python
├── input/                         # Datos de entrada (CSV/Excel)
├── output/                        # Resultados generados
├── memory/                        # Memoria del agente
├── config/                        # Configuración y benchmarks
├── docs/                          # Documentación
└── tests/                         # Pruebas del sistema
```

## Instalación paso a paso

1. **Clona o descomprime** el proyecto en tu equipo
2. **Abre la carpeta** en Claude Code
3. **Configura el MCP de Google Sheets** (opcional):
   - Sigue la guía en [docs/mcp_google_sheets.md](docs/mcp_google_sheets.md)
   - Copia `.env.example` a `.env` y configura las variables
4. **Coloca tus datos** en la carpeta `input/` (formato CSV o Excel)

## Cómo usarlo sin MCP

Si no configuras el MCP de Google Sheets, el agente usará automáticamente los benchmarks de `config/benchmarks_respaldo.csv`. Solo tendrás que colocar tus archivos CSV en `input/` y pedir al agente que los analice.

## Ejemplos de prompts para el usuario

- `¿Qué archivos hay en input/ y qué columnas tienen?`
- `Analiza las campañas de septiembre y genera el informe.`
- `¿Qué canal tiene el mejor CPA?`
- `Compara los resultados con los benchmarks del sector.`
- `¿Cuáles son las 3 mejores campañas por CTR?`

## Ejecutar las pruebas

```bash
python -m unittest discover tests
```

## Glosario

- **CTR (Click Through Rate)**: Porcentaje de personas que hicieron clic después de ver el anuncio. Fórmula: `(clics / impresiones) × 100`
- **CPC (Coste por clic)**: Coste medio de cada clic. Fórmula: `coste / clics`
- **CPA (Coste por adquisición)**: Coste medio de cada conversión. Fórmula: `coste / conversiones`

## Limitaciones conocidas

1. **Solo lectura**: No modifica los archivos originales en `input/`
2. **Formatos soportados**: CSV y Excel (necesita openpyxl para Excel)
3. **Moneda**: Euros por defecto, configurable en `memory/preferencias_usuario.md`
4. **MCP opcional**: Funciona con o sin conexión a Google Sheets

## Crear ZIP para entrega

Antes de comprimir:
- Borra `.env` si existe
- Borra la carpeta `credenciales/` si existe
- Asegúrate de que `output/` esté vacío o solo contenga ejemplos
- Verifica que `memory/historial_analisis.md` esté vacío

```bash
# En Linux/Mac
zip -r analista-campanas.zip analista-campanas -x "*/.env" "*/credenciales/*"

# En Windows: clic derecho > Comprimir después de borrar los archivos sensibles
```