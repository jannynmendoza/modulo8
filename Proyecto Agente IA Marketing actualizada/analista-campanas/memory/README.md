# Memoria del Agente

Esta carpeta contiene archivos que el agente puede usar para recordar preferencias del usuario y mantener un historial de análisis.

## Qué se puede guardar

✅ **Sí se puede guardar:**
- Preferencias del usuario (formato, nivel de detalle)
- Umbrales del semáforo para comparación
- Canales prioritarios para análisis
- Historial con fecha, archivo analizado, número de campañas
- Mejor y peor campaña por CPA

❌ **No se puede guardar:**
- Datos personales de usuarios
- Credenciales o claves de acceso
- IDs privados de documentos de Google Drive/Sheets
- Copias completas de los datos de campaña originales
- Información financiera confidencial

## Archivos de memoria

### 1. preferencias_usuario.md
Contiene las preferencias configuradas por el usuario:
- Idioma de los informes
- Moneda (€ por defecto)
- Umbral del semáforo (20% por defecto)
- Nivel de detalle en los informes
- Canales de mayor interés

### 2. historial_analisis.md
Registro de análisis realizados:
- Fecha del análisis
- Archivo analizado
- Número de campañas procesadas
- Mejor campaña (menor CPA)
- Peor campaña (mayor CPA)
- Fuente de benchmarks usada

## Actualización de memoria

El agente actualiza automáticamente estos archivos:
1. **preferencias_usuario.md**: Cuando el usuario indica nuevas preferencias
2. **historial_analisis.md**: Después de cada análisis completado

## Reglas de privacidad

- Los archivos de memoria **nunca** deben incluir información identificable
- No se almacenan datos crudos de campañas, solo resultados agregados
- Los nombres de campañas se mantienen tal cual, pero sin información adicional
- No se guardan datos de rendimiento financiero detallado