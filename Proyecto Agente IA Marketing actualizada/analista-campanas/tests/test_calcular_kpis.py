#!/usr/bin/env python3
"""
Tests unitarios para el script calcular_kpis.py
"""

import unittest
import csv
import tempfile
import os
import sys

# Añadir el directorio scripts al path para importar el módulo
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from calcular_kpis import procesar_csv, calcular_kpi_campana, validar_fila


class TestCalcularKPIs(unittest.TestCase):
    """Tests para el cálculo de KPIs de campañas de marketing."""
    
    def setUp(self):
        """Configurar datos de prueba."""
        self.datos_validos = [
            {
                'campana': 'Campaña 1',
                'canal': 'Google Ads',
                'impresiones': '10000',
                'clics': '300',
                'coste': '150',
                'conversiones': '15',
                'fecha_inicio': '2026-09-01',
                'fecha_fin': '2026-09-30'
            }
        ]
        
        self.datos_ejemplo_csv = os.path.join(os.path.dirname(__file__), 'datos', 'campanas_ejemplo.csv')
        self.datos_errores_csv = os.path.join(os.path.dirname(__file__), 'datos', 'campanas_con_errores.csv')
    
    def test_validar_fila_valida(self):
        """Test: Validar una fila con datos válidos."""
        fila_valida = {
            'campana': 'Test Campaña',
            'canal': 'Meta Ads',
            'impresiones': '5000',
            'clics': '100',
            'coste': '50',
            'conversiones': '5'
        }
        
        errores = validar_fila(fila_valida, 1)
        self.assertEqual(len(errores), 0, "Una fila válida no debe tener errores")
    
    def test_validar_fila_clics_mayor_impresiones(self):
        """Test: Validar fila con clics > impresiones."""
        fila_invalida = {
            'campana': 'Test',
            'canal': 'Google Ads',
            'impresiones': '1000',
            'clics': '1500',
            'coste': '75',
            'conversiones': '10'
        }
        
        errores = validar_fila(fila_invalida, 1)
        self.assertIn("Clics no puede ser mayor que impresiones", errores)
    
    def test_validar_fila_conversiones_mayor_clics(self):
        """Test: Validar fila con conversiones > clics."""
        fila_invalida = {
            'campana': 'Test',
            'canal': 'LinkedIn Ads',
            'impresiones': '2000',
            'clics': '50',
            'coste': '100',
            'conversiones': '60'
        }
        
        errores = validar_fila(fila_invalida, 1)
        self.assertIn("Conversiones no puede ser mayor que clics", errores)
    
    def test_validar_fila_coste_negativo(self):
        """Test: Validar fila con coste negativo."""
        fila_invalida = {
            'campana': 'Test',
            'canal': 'TikTok Ads',
            'impresiones': '3000',
            'clics': '150',
            'coste': '-50',
            'conversiones': '5'
        }
        
        errores = validar_fila(fila_invalida, 1)
        self.assertIn("Coste no puede ser negativo", errores)
    
    def test_validar_fila_campo_vacio(self):
        """Test: Validar fila con campo vacío."""
        fila_invalida = {
            'campana': 'Test',
            'canal': 'Google Ads',
            'impresiones': '',
            'clics': '100',
            'coste': '50',
            'conversiones': '5'
        }
        
        errores = validar_fila(fila_invalida, 1)
        self.assertIn("Campo 'impresiones' vacío o faltante", errores)
    
    def test_calcular_kpi_campana_normal(self):
        """Test: Calcular KPIs para una campaña normal."""
        fila = {
            'campana': 'Test Campaña',
            'canal': 'Google Ads',
            'impresiones': '10000',
            'clics': '300',
            'coste': '150',
            'conversiones': '15'
        }
        
        resultado = calcular_kpi_campana(fila)
        
        self.assertEqual(resultado['ctr_str'], "3.00")  # (300/10000)*100 = 3.00%
        self.assertEqual(resultado['cpc_str'], "0.50")  # 150/300 = 0.50€
        self.assertEqual(resultado['cpa_str'], "10.00")  # 150/15 = 10.00€
        self.assertEqual(len(resultado['alertas']), 0)
    
    def test_calcular_kpi_campana_sin_conversiones(self):
        """Test: Calcular KPIs para campaña sin conversiones."""
        fila = {
            'campana': 'Test Sin Conversiones',
            'canal': 'Meta Ads',
            'impresiones': '5000',
            'clics': '100',
            'coste': '50',
            'conversiones': '0'
        }
        
        resultado = calcular_kpi_campana(fila)
        
        self.assertEqual(resultado['ctr_str'], "2.00")  # (100/5000)*100 = 2.00%
        self.assertEqual(resultado['cpc_str'], "0.50")  # 50/100 = 0.50€
        self.assertEqual(resultado['cpa_str'], "n/d")   # División por cero
        self.assertIn("Sin conversiones", resultado['alertas'])
    
    def test_calcular_kpi_campana_sin_clics(self):
        """Test: Calcular KPIs para campaña sin clics."""
        fila = {
            'campana': 'Test Sin Clics',
            'canal': 'LinkedIn Ads',
            'impresiones': '2000',
            'clics': '0',
            'coste': '100',
            'conversiones': '0'
        }
        
        resultado = calcular_kpi_campana(fila)
        
        self.assertEqual(resultado['ctr_str'], "0.00")  # (0/2000)*100 = 0.00%
        self.assertEqual(resultado['cpc_str'], "n/d")   # División por cero
        self.assertEqual(resultado['cpa_str'], "n/d")   # División por cero
        self.assertIn("Sin conversiones", resultado['alertas'])
    
    def test_procesar_csv_ejemplo(self):
        """Test: Procesar archivo CSV de ejemplo completo."""
        resultados = procesar_csv(self.datos_ejemplo_csv)
        
        # Verificar conteos
        self.assertEqual(resultados['total_campanas'], 5)
        self.assertEqual(resultados['campanas_validas_count'], 5)
        self.assertEqual(resultados['campanas_invalidas_count'], 0)
        
        # Verificar KPIs específicos
        campanas = resultados['campanas_validas']
        
        # Buscar Search_Reservas_Verano
        for campana in campanas:
            if campana['campana'] == 'Search_Reservas_Verano':
                self.assertEqual(campana['ctr_str'], "5.00")
                self.assertEqual(campana['cpc_str'], "0.50")
                self.assertEqual(campana['cpa_str'], "12.50")
                break
        
        # Verificar agregados por canal
        self.assertEqual(len(resultados['kpis_agregados']), 4)  # 4 canales
    
    def test_procesar_csv_con_errores(self):
        """Test: Procesar archivo CSV con errores."""
        resultados = procesar_csv(self.datos_errores_csv)
        
        # Debería tener 1 válida y 4 inválidas
        self.assertEqual(resultados['total_campanas'], 5)
        self.assertEqual(resultados['campanas_validas_count'], 1)
        self.assertEqual(resultados['campanas_invalidas_count'], 4)
        
        # Verificar que se detectaron los errores correctos
        errores_detectados = set()
        for invalida in resultados['campanas_invalidas']:
            for error in invalida['errores']:
                errores_detectados.add(error)
        
        # Verificar tipos de errores esperados
        self.assertIn("Clics no puede ser mayor que impresiones", errores_detectados)
        self.assertIn("Coste no puede ser negativo", errores_detectados)
        self.assertIn("Campo 'clics' vacío o faltante", errores_detectados)
        self.assertIn("Conversiones no puede ser mayor que clics", errores_detectados)
    
    def test_integracion_completa(self):
        """Test de integración: procesar y guardar resultados."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as temp_file:
            # Crear archivo CSV temporal
            writer = csv.writer(temp_file)
            writer.writerow(['campana', 'canal', 'fecha_inicio', 'fecha_fin', 
                            'impresiones', 'clics', 'coste', 'conversiones'])
            writer.writerow(['Integración Test', 'Google Ads', '2026-09-01', '2026-09-30',
                            '10000', '500', '250', '25'])
        
        try:
            # Procesar el archivo
            resultados = procesar_csv(temp_file.name)
            
            # Verificar resultados
            self.assertEqual(resultados['campanas_validas_count'], 1)
            campana = resultados['campanas_validas'][0]
            self.assertEqual(campana['ctr_str'], "5.00")  # (500/10000)*100
            self.assertEqual(campana['cpc_str'], "0.50")  # 250/500
            self.assertEqual(campana['cpa_str'], "10.00")  # 250/25
            
        finally:
            # Limpiar archivo temporal
            os.unlink(temp_file.name)


if __name__ == '__main__':
    unittest.main()