"""
Módulo para calcular medidas de dispersión para datos agrupados.
"""

import pandas as pd
import math
from typing import Dict, Tuple


class Dispersion:
    """Clase para calcular medidas de dispersión."""
    
    def __init__(self, tabla: pd.DataFrame, media: float):
        """
        Inicializa la clase con la tabla de distribución de frecuencias y la media.
        
        Args:
            tabla: DataFrame con la tabla de frecuencias (sin fila de totales)
            media: Media aritmética calculada previamente
        """
        self.tabla = tabla[tabla['Intervalo'] != 'TOTAL'].copy()
        self.n = int(tabla[tabla['Intervalo'] == 'TOTAL']['fi (Frec. Absoluta)'].values[0])
        self.media = media
        
    def calcular_desviacion_media(self) -> Tuple[float, Dict]:
        """
        Calcula la desviación media para datos agrupados.
        
        Returns:
            Tupla con (resultado, diccionario de pasos)
        """
        pasos = {}
        
        # Crear tabla de cálculos
        tabla_calculos = self.tabla[['xi (Marca de Clase)', 'fi (Frec. Absoluta)']].copy()
        tabla_calculos['xi - x̄'] = tabla_calculos['xi (Marca de Clase)'] - self.media
        tabla_calculos['|xi - x̄|'] = tabla_calculos['xi - x̄'].abs()
        tabla_calculos['|xi - x̄| × fi'] = tabla_calculos['|xi - x̄|'] * tabla_calculos['fi (Frec. Absoluta)']
        
        pasos['tabla'] = tabla_calculos
        pasos['media'] = self.media
        
        # Calcular suma
        suma = tabla_calculos['|xi - x̄| × fi'].sum()
        pasos['suma'] = suma
        pasos['formula_suma'] = f"Σ|xi - x̄| × fi = {suma:.4f}"
        
        # Calcular desviación media
        dm = suma / self.n
        pasos['resultado'] = dm
        pasos['formula'] = f"DM = Σ|xi - x̄| × fi / n"
        pasos['formula_final'] = f"DM = {suma:.4f} / {self.n} = {dm:.2f}"
        
        return dm, pasos
    
    def calcular_desviacion_estandar(self) -> Tuple[float, Dict]:
        """
        Calcula la desviación estándar para datos agrupados.
        
        Returns:
            Tupla con (resultado, diccionario de pasos)
        """
        pasos = {}
        
        # Crear tabla de cálculos
        tabla_calculos = self.tabla[['xi (Marca de Clase)', 'fi (Frec. Absoluta)']].copy()
        tabla_calculos['xi - x̄'] = tabla_calculos['xi (Marca de Clase)'] - self.media
        tabla_calculos['(xi - x̄)²'] = tabla_calculos['xi - x̄'] ** 2
        tabla_calculos['(xi - x̄)² × fi'] = tabla_calculos['(xi - x̄)²'] * tabla_calculos['fi (Frec. Absoluta)']
        
        pasos['tabla'] = tabla_calculos
        pasos['media'] = self.media
        
        # Calcular suma
        suma = tabla_calculos['(xi - x̄)² × fi'].sum()
        pasos['suma'] = suma
        pasos['formula_suma'] = f"Σ(xi - x̄)² × fi = {suma:.4f}"
        
        # Calcular varianza
        varianza = suma / self.n
        pasos['varianza'] = varianza
        pasos['formula_varianza'] = f"σ² = {suma:.4f} / {self.n} = {varianza:.4f}"
        
        # Calcular desviación estándar
        desv_estandar = math.sqrt(varianza)
        pasos['resultado'] = desv_estandar
        pasos['formula'] = f"σ = √[Σ(xi - x̄)² × fi / n]"
        pasos['formula_final'] = f"σ = √{varianza:.4f} = {desv_estandar:.2f}"
        
        return desv_estandar, pasos
