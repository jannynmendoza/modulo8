#!/usr/bin/env python3
"""
Script para calcular KPIs de campañas de marketing.
Calcula CTR, CPC y CPA a partir de archivos CSV.

Uso:
    python calcular_kpis.py <archivo_entrada> <archivo_salida_csv>

Formato de entrada CSV:
    campana,canal,fecha_inicio,fecha_fin,impresiones,clics,coste,conversiones
"""

import csv
import sys
import argparse
from datetime import datetime
from collections import defaultdict


def validar_fila(fila, numero_fila):
    """
    Valida una fila del CSV y devuelve una lista de errores.
    """
    errores = []
    
    # Validar columnas obligatorias
    campos_obligatorios = ['campana', 'canal', 'impresiones', 'clics', 'coste', 'conversiones']
    for campo in campos_obligatorios:
        if campo not in fila or fila[campo] == '':
            errores.append(f"Campo '{campo}' vacío o faltante")
    
    if errores:
        return errores
    
    try:
        impresiones = int(fila['impresiones'])
        clics = int(fila['clics'])
        coste = float(fila['coste'])
        conversiones = int(fila['conversiones'])
        
        # Validaciones de negatividad
        if impresiones < 0:
            errores.append("Impresiones no puede ser negativo")
        if clics < 0:
            errores.append("Clics no puede ser negativo")
        if coste < 0:
            errores.append("Coste no puede ser negativo")
        if conversiones < 0:
            errores.append("Conversiones no puede ser negativo")
        
        # Validaciones de consistencia
        if clics > impresiones:
            errores.append("Clics no puede ser mayor que impresiones")
        if conversiones > clics:
            errores.append("Conversiones no puede ser mayor que clics")
            
    except ValueError as e:
        errores.append(f"Error de conversión de tipo: {str(e)}")
    
    return errores


def calcular_kpi_campana(fila):
    """
    Calcula KPIs para una campaña individual.
    """
    impresiones = int(fila['impresiones'])
    clics = int(fila['clics'])
    coste = float(fila['coste'])
    conversiones = int(fila['conversiones'])
    
    # Calcular CTR
    if impresiones > 0:
        ctr = (clics / impresiones) * 100
        ctr_str = f"{ctr:.2f}"
    else:
        ctr = None
        ctr_str = "n/d"
    
    # Calcular CPC
    if clics > 0:
        cpc = coste / clics
        cpc_str = f"{cpc:.2f}"
    else:
        cpc = None
        cpc_str = "n/d"
    
    # Calcular CPA
    if conversiones > 0:
        cpa = coste / conversiones
        cpa_str = f"{cpa:.2f}"
    else:
        cpa = None
        cpa_str = "n/d"
    
    return {
        'campana': fila['campana'],
        'canal': fila['canal'],
        'impresiones': impresiones,
        'clics': clics,
        'coste': coste,
        'conversiones': conversiones,
        'ctr': ctr,
        'cpc': cpc,
        'cpa': cpa,
        'ctr_str': ctr_str,
        'cpc_str': cpc_str,
        'cpa_str': cpa_str,
        'alertas': [] if conversiones > 0 else ['Sin conversiones']
    }


def calcular_kpis_agregados(campanas):
    """
    Calcula KPIs agregados por canal.
    """
    canales = defaultdict(lambda: {
        'impresiones': 0,
        'clics': 0,
        'coste': 0.0,
        'conversiones': 0,
        'campanas': []
    })
    
    for campana in campanas:
        canal = campana['canal']
        canales[canal]['impresiones'] += campana['impresiones']
        canales[canal]['clics'] += campana['clics']
        canales[canal]['coste'] += campana['coste']
        canales[canal]['conversiones'] += campana['conversiones']
        canales[canal]['campanas'].append(campana['campana'])
    
    resultados = []
    for canal, datos in canales.items():
        impresiones = datos['impresiones']
        clics = datos['clics']
        coste = datos['coste']
        conversiones = datos['conversiones']
        
        # CTR agregado
        if impresiones > 0:
            ctr = (clics / impresiones) * 100
            ctr_str = f"{ctr:.2f}"
        else:
            ctr = None
            ctr_str = "n/d"
        
        # CPC agregado
        if clics > 0:
            cpc = coste / clics
            cpc_str = f"{cpc:.2f}"
        else:
            cpc = None
            cpc_str = "n/d"
        
        # CPA agregado
        if conversiones > 0:
            cpa = coste / conversiones
            cpa_str = f"{cpa:.2f}"
        else:
            cpa = None
            cpa_str = "n/d"
        
        resultados.append({
            'canal': canal,
            'impresiones': impresiones,
            'clics': clics,
            'coste': coste,
            'conversiones': conversiones,
            'ctr': ctr,
            'cpc': cpc,
            'cpa': cpa,
            'ctr_str': ctr_str,
            'cpc_str': cpc_str,
            'cpa_str': cpa_str,
            'campanas': len(datos['campanas'])
        })
    
    return resultados


def procesar_csv(archivo_entrada):
    """
    Procesa un archivo CSV y calcula los KPIs.
    """
    campanas_validas = []
    campanas_invalidas = []
    
    # Intentar diferentes codificaciones
    encodings = ['utf-8', 'latin-1', 'cp1252']
    
    for encoding in encodings:
        try:
            with open(archivo_entrada, 'r', encoding=encoding) as f:
                reader = csv.DictReader(f)
                
                for i, fila in enumerate(reader, 1):
                    errores = validar_fila(fila, i)
                    
                    if errores:
                        campanas_invalidas.append({
                            'fila': i,
                            'datos': fila,
                            'errores': errores
                        })
                    else:
                        kpis = calcular_kpi_campana(fila)
                        campanas_validas.append(kpis)
            
            # Si llegamos aquí, la codificación funcionó
            break
        except UnicodeDecodeError:
            continue
    else:
        # Si ninguna codificación funcionó, usar utf-8 con errors='replace'
        with open(archivo_entrada, 'r', encoding='utf-8', errors='replace') as f:
            reader = csv.DictReader(f)
            
            for i, fila in enumerate(reader, 1):
                errores = validar_fila(fila, i)
                
                if errores:
                    campanas_invalidas.append({
                        'fila': i,
                        'datos': fila,
                        'errores': errores
                    })
                else:
                    kpis = calcular_kpi_campana(fila)
                    campanas_validas.append(kpis)
    
    kpis_agregados = calcular_kpis_agregados(campanas_validas)
    
    return {
        'campanas_validas': campanas_validas,
        'campanas_invalidas': campanas_invalidas,
        'kpis_agregados': kpis_agregados,
        'total_campanas': len(campanas_validas) + len(campanas_invalidas),
        'campanas_validas_count': len(campanas_validas),
        'campanas_invalidas_count': len(campanas_invalidas)
    }


def guardar_resultados(resultados, archivo_salida):
    """
    Guarda los resultados en un archivo CSV.
    """
    with open(archivo_salida, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        
        # Escribir encabezado
        writer.writerow([
            'campana', 'canal', 'impresiones', 'clics', 'coste', 'conversiones',
            'ctr', 'cpc', 'cpa', 'alertas'
        ])
        
        # Escribir datos de campañas válidas
        for campana in resultados['campanas_validas']:
            writer.writerow([
                campana['campana'],
                campana['canal'],
                campana['impresiones'],
                campana['clics'],
                f"{campana['coste']:.2f}",
                campana['conversiones'],
                campana['ctr_str'],
                campana['cpc_str'],
                campana['cpa_str'],
                ';'.join(campana['alertas']) if campana['alertas'] else ''
            ])


def main():
    parser = argparse.ArgumentParser(description='Calcula KPIs de campañas de marketing')
    parser.add_argument('archivo_entrada', help='Ruta al archivo CSV de entrada')
    parser.add_argument('archivo_salida', help='Ruta al archivo CSV de salida')
    
    args = parser.parse_args()
    
    print(f"Procesando archivo: {args.archivo_entrada}")
    resultados = procesar_csv(args.archivo_entrada)
    
    # Mostrar resumen
    print(f"\nResumen de procesamiento:")
    print(f"  - Total de filas procesadas: {resultados['total_campanas']}")
    print(f"  - Campañas válidas: {resultados['campanas_validas_count']}")
    print(f"  - Campañas inválidas (excluidas): {resultados['campanas_invalidas_count']}")
    
    if resultados['campanas_invalidas']:
        print(f"\nCampañas excluidas por errores:")
        for invalida in resultados['campanas_invalidas']:
            print(f"  - Fila {invalida['fila']}: {', '.join(invalida['errores'])}")
    
    # Guardar resultados
    guardar_resultados(resultados, args.archivo_salida)
    print(f"\nResultados guardados en: {args.archivo_salida}")
    
    # Mostrar KPIs agregados por canal
    print(f"\nKPIs agregados por canal:")
    for kpi in resultados['kpis_agregados']:
        print(f"  - {kpi['canal']}: CTR={kpi['ctr_str']}%, CPC={kpi['cpc_str']}€, CPA={kpi['cpa_str']}€")


if __name__ == '__main__':
    main()