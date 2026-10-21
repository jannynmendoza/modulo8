# Arquitectura en Claude Code

Documentación basada en la [documentación oficial de Claude Code](https://docs.claude.com/en/docs/claude-code), actualizada a octubre de 2026.

## Cómo organiza Claude Code cada elemento

| Elemento | Cómo lo organiza Claude Code | Dónde está en nuestro proyecto |
|----------|-----------------------------|--------------------------------|
| Instrucciones del agente | Archivo `CLAUDE.md` en la raíz, que se carga automáticamente al iniciar la sesión | `CLAUDE.md` (raíz del proyecto) |
| Entradas y salidas | No hay carpetas fijas; se definen en `CLAUDE.md` | `input/` (datos de entrada) y `output/` (resultados) definidos en `CLAUDE.md` |
| Memoria | `CLAUDE.md` (memoria de proyecto) y archivos importados con `@ruta` | `memory/` (preferencias e historial) |
| Skills | Carpetas con `SKILL.md` en `.claude/skills/` (con nombre y descripción en encabezado YAML) | `.claude/skills/` (skills operativas) y `skills/` (copia para documentación) |
| MCP | Archivo `.mcp.json` en la raíz (ámbito de proyecto) y comando `/mcp` para ver estado | `.mcp.json` (configuración del servidor Google Sheets) |
| Permisos | `.claude/settings.json` con reglas `allow`/`deny` | `.claude/settings.json` (control de acceso) |
| Pruebas | Claude Code no trae un sistema de pruebas propio; se implementa externamente | `tests/` (datos, scripts Python y checklist manual) |

## Detalles de implementación

### 1. Instrucciones del agente (`CLAUDE.md`)
Claude Code carga automáticamente el archivo `CLAUDE.md` cuando se inicia una sesión en la carpeta. Este archivo:
- Define el rol y comportamiento del agente
- Especifica entradas, salidas y proceso de trabajo
- Establece restricciones y permisos
- Se escribe en segunda persona dirigido al agente

### 2. Sistema de Skills
Las skills en Claude Code:
- Se almacenan en `.claude/skills/<nombre-skill>/SKILL.md`
- Cada `SKILL.md` tiene un encabezado YAML con `name` y `description`
- La descripción debe indicar cuándo usar la skill
- El agente puede invocar skills automáticamente según el contexto

**Cambios recientes (2026):** Claude Code ahora soporta habilidades más complejas con múltiples archivos por skill, pero mantenemos la estructura simple para compatibilidad.

### 3. Configuración MCP
El Model Context Protocol (MCP):
- Se configura en `.mcp.json` en la raíz del proyecto
- Los servidores pueden estar activos o desactivados (`disabled`)
- Claude Code soporta variables de entorno con sintaxis `${VARIABLE}`
- El estado se verifica con el comando `/mcp` en el chat

### 4. Permisos y seguridad
El archivo `.claude/settings.json` controla:
- Qué herramientas puede usar el agente
- Acceso a carpetas y archivos
- Permisos de lectura/escritura
- Restricciones específicas por herramienta

**Mejora de seguridad (2026):** Claude Code ahora tiene validación de rutas más estricta y soporta patrones glob complejos.

### 5. Memoria persistente
Mientras que Claude Code tiene memoria de sesión, nuestro proyecto añade:
- `memory/` para preferencias persistentes entre sesiones
- `memory/historial_analisis.md` para tracking de análisis
- Integración con la memoria nativa mediante referencias a archivos

### 6. Pruebas y validación
Aunque Claude Code no incluye framework de pruebas:
- Implementamos `tests/` con datos de ejemplo
- Scripts Python para validación reproducible
- Checklist manual para verificación de comportamiento
- Documentación de resultados esperados

## Flujo de trabajo recomendado

1. **Inicio**: Abrir la carpeta en Claude Code → Carga `CLAUDE.md`
2. **Configuración**: Verificar MCP con `/mcp`, ajustar `.env` si es necesario
3. **Datos**: Colocar archivos CSV/Excel en `input/`
4. **Análisis**: Solicitar análisis al agente → Usa skills automáticamente
5. **Resultados**: Revisar archivos en `output/`, historial en `memory/`
6. **Pruebas**: Ejecutar `python -m unittest discover tests` para validar

## Compatibilidad y versiones

Este proyecto está diseñado para:
- Claude Code v2.0+ (2026)
- Python 3.8+
- Sistemas: Windows, macOS, Linux
- Formatos: CSV (nativo), Excel (con openpyxl opcional)

**Nota**: La estructura de skills y MCP puede evolucionar. Consulta la documentación oficial para actualizaciones.