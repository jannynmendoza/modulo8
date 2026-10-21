---
name: calcular-kpis
description: Usa esta skill cuando necesites validar datos de campañas y calcular sus indicadores CTR, CPC y CPA.
---

# Skill: Calcular KPIs

Valida archivos de campañas de marketing y calcula los indicadores clave de rendimiento.

## Cuándo usar esta skill

- El usuario ha proporcionado un archivo CSV o Excel con datos de campañas
- Necesitas calcular CTR, CPC y CPA para cada campaña
- Debes validar la calidad de los datos antes de proceder al análisis
- Es el primer paso antes de generar el informe comparativo

## Pasos a seguir

### 1. Validar el archivo de entrada
- Verifica que el archivo existe en `input/`
- Confirma que tiene las columnas obligatorias:
  - `campana` (nombre de la campaña)
  - `canal` (plataforma: Google Ads, Meta Ads, etc.)
  - `impresiones` (número entero no negativo)
  - `clics` (número entero no negativo, ≤ impresiones)
  - `coste` (número decimal no negativo, en euros)
  - `conversiones` (número entero no negativo, ≤ clics)
- Las filas con errores no se corrigen: se excluyen y se listan con su motivo

### 2. Ejecutar el script de cálculo
```bash
python scripts/calcular_kpis.py <archivo_entrada> <archivo_salida_csv>
```

### 3. Procesar los resultados
- **CTR (Click Through Rate)**: `(clics / impresiones) × 100` (en %)
  - Si `impresiones = 0`: CTR = "n/d"
  - Redondeo: 2 decimales
- **CPC (Coste por clic)**: `coste / clics` (en €)
  - Si `clics = 0`: CPC = "n/d"
  - Redondeo: 2 decimales
- **CPA (Coste por adquisición)**: `coste / conversiones` (en €)
  - Si `conversiones = 0`: CPA = "n/d" y genera alerta "campaña sin conversiones"
  - Redondeo: 2 decimales

### 4. Calcular agregados por canal
- Suma impresiones, clics, coste y conversiones por canal
- Calcula CTR, CPC y CPA agregados (nunca promediar ratios)
- Conserva los cálculos individuales por campaña

### 5. Generar alertas
- Campañas sin conversiones (CPA = "n/d")
- Datos faltantes o inconsistentes
- Filas excluidas del análisis

## Ejemplo de entrada

```csv
campana,canal,fecha_inicio,fecha_fin,impresiones,clics,coste,conversiones
Search_Reservas_Verano,Google Ads,2026-09-01,2026-09-30,50000,2500,1250,100
Retargeting_Web,Meta Ads,2026-09-01,2026-09-30,120000,1800,900,45
```

## Ejemplo de salida

```csv
campana,canal,impresiones,clics,coste,conversiones,ctr,cpc,cpa,alertas
Search_Reservas_Verano,Google Ads,50000,2500,1250.00,100,5.00%,0.50€,12.50€,
Retargeting_Web,Meta Ads,120000,1800,900.00,45,1.50%,0.50€,20.00€,
```

## Casos límite

1. **Campaña sin clics** (`clics = 0`):
   - CTR = 0,00% (si hay impresiones)
   - CPC = "n/d"
   - CPA = "n/d" (si no hay conversiones)

2. **Campaña sin conversiones** (`conversiones = 0`):
   - CPA = "n/d"
   - Alerta: "campaña sin conversiones"

3. **Datos faltantes**:
   - Excluir fila del análisis
   - Registrar motivo: "Campo X vacío o faltante"

4. **Archivo Excel (.xlsx)**:
   - Pedir al usuario que lo exporte a CSV
   - O usar `openpyxl` solo si está instalado

## Validaciones implementadas

✅ **Validaciones de formato:**
- Columnas obligatorias presentes
- Valores numéricos donde corresponden
- No valores negativos

✅ **Validaciones de consistencia:**
- `clics ≤ impresiones`
- `conversiones ≤ clics`
- Fechas en formato válido

✅ **Validaciones de negocio:**
- Coste en euros (€)
- Períodos de tiempo razonables
- Canales reconocidos (Google Ads, Meta Ads, etc.)