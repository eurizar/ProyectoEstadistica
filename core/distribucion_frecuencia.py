"""
Módulo para calcular la distribución de frecuencias de datos agrupados.
"""

import math
import pandas as pd
from typing import Dict, List, Tuple


class DistribucionFrecuencia:
    """Clase para calcular la distribución de frecuencias de datos agrupados."""
    
    def __init__(self, datos: List[float]):
        """
        Inicializa la clase con los datos a analizar.
        
        Args:
            datos: Lista de valores numéricos
        """
        self.datos = sorted(datos)
        self.n = len(datos)
        self.pasos = {}
        
    def calcular_parametros(self) -> Dict:
        """
        Calcula los parámetros necesarios para la distribución de frecuencias.
        
        Returns:
            Diccionario con los parámetros calculados y los pasos
        """
        # Paso 1: Ordenar datos
        self.pasos['datos_ordenados'] = self.datos.copy()
        
        # Paso 2: Valor mínimo y máximo
        x_min = min(self.datos)
        x_max = max(self.datos)
        self.pasos['x_min'] = x_min
        self.pasos['x_max'] = x_max
        
        # Paso 3: Calcular rango
        rango = x_max - x_min
        self.pasos['rango'] = rango
        self.pasos['rango_formula'] = f"R = Xmax - Xmin = {x_max} - {x_min} = {rango}"
        
        # Paso 4: Calcular número de clases (Regla de Sturges)
        k_decimal = 1 + 3.322 * math.log10(self.n)
        k = math.ceil(k_decimal)
        self.pasos['k_decimal'] = k_decimal
        self.pasos['k'] = k
        self.pasos['k_formula'] = f"k = 1 + 3.322 × log10(n) = 1 + 3.322 × log10({self.n}) = {k_decimal:.4f} ≈ {k}"
        
        # Paso 5: Calcular amplitud
        amplitud_decimal = rango / k
        amplitud = math.ceil(amplitud_decimal)
        self.pasos['amplitud_decimal'] = amplitud_decimal
        self.pasos['amplitud'] = amplitud
        self.pasos['amplitud_formula'] = f"A = R / k = {rango} / {k} = {amplitud_decimal:.4f} ≈ {amplitud}"
        
        return {
            'x_min': x_min,
            'x_max': x_max,
            'rango': rango,
            'k': k,
            'amplitud': amplitud,
            'pasos': self.pasos
        }
    
    def crear_intervalos(self, x_min: float, amplitud: float, k: int) -> List[Tuple[float, float]]:
        """
        Crea los intervalos de clase.
        
        Args:
            x_min: Valor mínimo
            amplitud: Amplitud de cada intervalo
            k: Número de clases
            
        Returns:
            Lista de tuplas (límite_inferior, límite_superior)
        """
        intervalos = []
        for i in range(k):
            li = x_min + i * amplitud
            ls = li + amplitud
            intervalos.append((li, ls))
        return intervalos
    
    def calcular_frecuencias(self, intervalos: List[Tuple[float, float]]) -> pd.DataFrame:
        """
        Calcula las frecuencias para cada intervalo.
        
        Args:
            intervalos: Lista de intervalos de clase
            
        Returns:
            DataFrame con la tabla de distribución de frecuencias
        """
        # Preparar datos para la tabla
        tabla_data = []
        frecuencia_acumulada = 0
        
        for i, (li, ls) in enumerate(intervalos):
            # Marca de clase
            xi = (li + ls) / 2
            
            # Frecuencia absoluta (conteo de datos en el intervalo)
            if i == len(intervalos) - 1:
                # Último intervalo es cerrado [li, ls]
                fi = sum(1 for x in self.datos if li <= x <= ls)
            else:
                # Intervalo cerrado-abierto [li, ls)
                fi = sum(1 for x in self.datos if li <= x < ls)
            
            # Frecuencia acumulada
            frecuencia_acumulada += fi
            Fi = frecuencia_acumulada
            
            # Frecuencia relativa
            hi = fi / self.n
            
            # Frecuencia relativa porcentual
            hi_porcentaje = hi * 100
            
            tabla_data.append({
                'Intervalo': f"[{li:.2f} - {ls:.2f})",
                'Li': li,
                'Ls': ls,
                'xi (Marca de Clase)': xi,
                'fi (Frec. Absoluta)': fi,
                'Fi (Frec. Acumulada)': Fi,
                'hi (Frec. Relativa)': hi,
                'hi% (Frec. Relativa %)': hi_porcentaje
            })
        
        # Crear DataFrame
        df = pd.DataFrame(tabla_data)
        
        # Agregar fila de totales
        totales = {
            'Intervalo': 'TOTAL',
            'Li': '',
            'Ls': '',
            'xi (Marca de Clase)': '',
            'fi (Frec. Absoluta)': self.n,
            'Fi (Frec. Acumulada)': '',
            'hi (Frec. Relativa)': 1.00,
            'hi% (Frec. Relativa %)': 100.00
        }
        df = pd.concat([df, pd.DataFrame([totales])], ignore_index=True)
        
        return df
    
    def generar_tabla(self) -> Tuple[pd.DataFrame, Dict]:
        """
        Genera la tabla completa de distribución de frecuencias.
        
        Returns:
            Tupla con (DataFrame de la tabla, diccionario de parámetros)
        """
        parametros = self.calcular_parametros()
        intervalos = self.crear_intervalos(
            parametros['x_min'],
            parametros['amplitud'],
            parametros['k']
        )
        tabla = self.calcular_frecuencias(intervalos)
        
        return tabla, parametros
