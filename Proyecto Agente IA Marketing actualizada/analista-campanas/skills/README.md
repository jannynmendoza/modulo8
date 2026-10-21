# Skills del Agente - Copia Documental

Esta carpeta contiene copias idénticas de las skills que el agente usa realmente, ubicadas en `.claude/skills/`. Estas copias existen para:

## ¿Por qué hay dos copias?

1. **`.claude/skills/`** (operativa):
   - Claude Code carga las skills desde aquí automáticamente
   - Es la ubicación oficial que reconoce Claude Code
   - El agente busca skills en esta ubicación al iniciar

2. **`skills/`** (documental):
   - Copia visible para documentación y entrega
   - Permite examinar las skills sin acceder a `.claude/`
   - Facilita la revisión del proyecto por otros equipos
   - Mantiene la estructura del ZIP organizada

## Estructura de skills

Cada skill tiene:
- **Carpeta con nombre descriptivo**: `calcular-kpis/`, `informe-comparativo/`
- **Archivo `SKILL.md`**: Contenido completo de la skill
- **Encabezado YAML**: Con `name` y `description` (obligatorio para Claude Code)

## Skills disponibles

### 1. `calcular-kpis`
**Descripción**: Valida datos de campañas y calcula CTR, CPC y CPA.
**Cuándo usarla**: Cuando el usuario proporciona un archivo CSV/Excel con datos de campañas.

### 2. `informe-comparativo`  
**Descripción**: Compara KPIs con benchmarks y genera informe ejecutivo.
**Cuándo usarla**: Después de calcular KPIs, para generar el informe final.

## Mantenimiento

Cuando modifiques una skill:
1. Actualiza primero en `.claude/skills/<nombre>/SKILL.md`
2. Copia el cambio a `skills/<nombre>/SKILL.md`
3. Verifica que ambas copias sean idénticas

## Compatibilidad

- Claude Code v2.0+ (2026)
- Formato YAML en encabezado obligatorio
- Descripción clara y específica
- Instrucciones paso a paso