"""
Módulo principal para el análisis estadístico completo.
"""

from typing import Dict, List
from .distribucion_frecuencia import DistribucionFrecuencia
from .tendencia_central import TendenciaCentral
from .dispersion import Dispersion


class AnalizadorEstadistico:
    """Clase principal que coordina todos los cálculos estadísticos."""
    
    def __init__(self, datos: List[float]):
        """
        Inicializa el analizador con los datos a procesar.
        
        Args:
            datos: Lista de valores numéricos
        """
        self.datos = datos
        self.resultados = {}
        
    def calcular_todo(self) -> Dict:
        """
        Realiza todos los cálculos estadísticos.
        
        Returns:
            Diccionario con todos los resultados y pasos
        """
        # 1. Distribución de frecuencias
        dist_freq = DistribucionFrecuencia(self.datos)
        tabla, parametros = dist_freq.generar_tabla()
        
        self.resultados['distribucion'] = {
            'tabla': tabla,
            'parametros': parametros
        }
        
        # 2. Tendencia central
        tend_central = TendenciaCentral(tabla)
        
        media, pasos_media = tend_central.calcular_media()
        mediana, pasos_mediana = tend_central.calcular_mediana()
        moda, pasos_moda = tend_central.calcular_moda()
        
        self.resultados['tendencia_central'] = {
            'media': {'valor': media, 'pasos': pasos_media},
            'mediana': {'valor': mediana, 'pasos': pasos_mediana},
            'moda': {'valor': moda, 'pasos': pasos_moda}
        }
        
        # 3. Dispersión
        dispersion = Dispersion(tabla, media)
        
        dm, pasos_dm = dispersion.calcular_desviacion_media()
        de, pasos_de = dispersion.calcular_desviacion_estandar()
        
        self.resultados['dispersion'] = {
            'desviacion_media': {'valor': dm, 'pasos': pasos_dm},
            'desviacion_estandar': {'valor': de, 'pasos': pasos_de}
        }
        
        return self.resultados
    
    def obtener_paso_a_paso(self) -> Dict:
        """
        Obtiene todos los cálculos paso a paso organizados.
        
        Returns:
            Diccionario con los pasos de cada cálculo
        """
        if not self.resultados:
            self.calcular_todo()
        
        return {
            'preliminares': self.resultados['distribucion']['parametros']['pasos'],
            'tabla': self.resultados['distribucion']['tabla'],
            'tendencia_central': {
                'media': self.resultados['tendencia_central']['media']['pasos'],
                'mediana': self.resultados['tendencia_central']['mediana']['pasos'],
                'moda': self.resultados['tendencia_central']['moda']['pasos']
            },
            'dispersion': {
                'desviacion_media': self.resultados['dispersion']['desviacion_media']['pasos'],
                'desviacion_estandar': self.resultados['dispersion']['desviacion_estandar']['pasos']
            }
        }
