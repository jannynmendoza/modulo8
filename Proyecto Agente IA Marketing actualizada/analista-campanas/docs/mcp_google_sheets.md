# MCP de Google Sheets - Configuración y Uso

Guía para configurar y usar el conector MCP de Google Sheets con el analista de campañas.

## 1. ¿Qué sistema conecta?

Conecta con **Google Sheets/Drive** para leer la hoja de benchmarks de campañas de marketing usando autenticación OAuth a través del navegador.

## 2. ¿Qué información puede consultar?

- Hoja "Benchmarks campañas" en Google Drive
- Columnas: `canal`, `ctr_objetivo`, `cpc_objetivo`, `cpa_objetivo`
- Solo lectura de celdas y rangos
- Archivos específicos que autorices durante la autenticación

## 3. ¿Qué acciones puede realizar?

- Listar hojas de cálculo autorizadas
- Leer celdas específicas o rangos completos
- Consultar nombres de hojas y estructura
- Buscar y describir hojas

## 4. ¿Qué permisos necesita?

Autenticación OAuth con tu cuenta personal de Google que otorga:
- Acceso de lectura a Google Sheets (scope: `drive.file`)
- Solo acceso a archivos específicos que selecciones durante la autenticación
- Permisos temporales que puedes revocar en cualquier momento

## 5. ¿Qué acciones tiene prohibidas?

❌ **Prohibido por configuración** (en `.claude/settings.json`):
- Escribir en hojas (aunque el servidor lo soporte, lo bloqueamos)
- Crear nuevas hojas o documentos
- Borrar archivos o contenido
- Compartir documentos
- Mover archivos

❌ **Prohibido por permisos** (scope `drive.file`):
- Acceso a todos tus archivos de Drive
- Modificar permisos de archivos
- Acceder a archivos no autorizados explícitamente

## 6. ¿Qué hacer si la conexión falla?

1. **Reintentar una vez**: El agente intenta reconectar automáticamente
2. **Usar respaldo local**: Si falla, usa `config/benchmarks_respaldo.csv`
3. **Indicar en el informe**: Muestra "Benchmarks: respaldo local (MCP no disponible)"
4. **Guía de solución**: Explicar al usuario cómo revisar la conexión con `/mcp`

## 7. Paso a paso para configurarlo

### Paso 1: Obtener API Key
1. Ve a [https://g.mcp.openbsp.dev](https://g.mcp.openbsp.dev)
2. Haz clic en **"Login with Google"**
3. Autoriza el acceso a:
   - Google Sheets (para leer benchmarks)
   - Selecciona tu hoja "Benchmarks campañas" cuando te lo pida
4. Después de autenticarte, copia el **API Key** que se te muestra

### Paso 2: Configurar variables de entorno
1. Copia `.env.example` a `.env`
2. Edita `.env` con tu API Key real:
   ```env
   GOOGLE_MCP_API_KEY=gmc_tu_api_key_real_aqui
   ```
3. **NUNCA** subas `.env` al ZIP de entrega

### Paso 3: Preparar la hoja de benchmarks
1. En Google Drive, asegúrate de tener una hoja llamada **"Benchmarks campañas"**
2. Copia el contenido de `config/benchmarks_respaldo.csv` a la hoja
3. La hoja debe tener las columnas: `canal`, `ctr_objetivo`, `cpc_objetivo`, `cpa_objetivo`

### Paso 4: Probar la conexión
1. Reinicia Claude Code (cierra y vuelve a abrir la carpeta)
2. En el chat, escribe `/mcp`
3. Deberías ver **"google-mcp"** como conectado
4. Prueba con: `¿Qué benchmarks tenemos en Google Sheets para Meta Ads?`

### Paso 5: Configurar acceso a archivos específicos
Durante la autenticación OAuth:
- Selecciona **solo la hoja "Benchmarks campañas"**
- No autorices acceso a todos tus archivos
- El scope `drive.file` solo da acceso a archivos seleccionados explícitamente

## 8. Alternativas de configuración

### Opción A: Autenticación OAuth (recomendada)
- **Ventajas**: Sin configuración de Google Cloud, autenticación por navegador, fácil de usar
- **Cómo**: Usa el servidor `google-mcp` de OpenBSP como está configurado
- **Seguridad**: Solo accede a archivos específicos que autorices

### Opción B: Usar solo respaldo local
- **Ventajas**: Sin conexión a internet, sin configuración compleja
- **Cómo**: Deja el MCP desactivado o sin API key
- **Funcionamiento**: El agente usará automáticamente `config/benchmarks_respaldo.csv`

### Opción C: Cuenta de servicio tradicional
- **Ventajas**: Más control, sin interacción humana necesaria para cada autenticación
- **Cómo**: Cambia la configuración en `.mcp.json` de vuelta a `google-sheets` con cuenta de servicio
- **Complejidad**: Requiere configuración de Google Cloud y cuenta de servicio

## 9. Solución de problemas

### Error: "MCP server google-mcp failed to connect"
- Verifica que tu API key es correcta en `.env`
- Asegúrate de que el API key no ha expirado (genera uno nuevo si es necesario)
- Verifica tu conexión a internet

### Error: "No authorized files found"
- Durante la autenticación, asegúrate de seleccionar tu hoja "Benchmarks campañas"
- Si no la seleccionaste, revoca el acceso y autentícate de nuevo
- Verifica que la hoja existe en tu Google Drive

### Error: "Permission denied"
- Revisa que autorizaste el acceso durante la autenticación OAuth
- Verifica que no revocaste el acceso desde tu cuenta de Google
- Genera un nuevo API key si es necesario

### Error: "API key invalid or expired"
- Ve a [https://g.mcp.openbsp.dev](https://g.mcp.openbsp.dev) y genera un nuevo API key
- Actualiza el valor en tu archivo `.env`
- Reinicia Claude Code

## 10. Seguridad y mejores prácticas

- **Nunca** incluyas tu API key real en el ZIP de entrega
- **Sí incluye** `.env.example` con valores ficticios
- Usa el scope `drive.file` que solo da acceso a archivos específicos
- Revoca el acceso desde [tu cuenta de Google](https://myaccount.google.com/permissions) si dejas de usar el proyecto
- Mantén tu API key segura y no la compartas
- Usa `.gitignore` para excluir archivos `.env` sensibles
- El servidor MCP no almacena tus datos, solo actúa como proxy entre Google y Claude Code