"""
Módulo para calcular medidas de tendencia central para datos agrupados.
"""

import pandas as pd
from typing import Dict, Tuple


class TendenciaCentral:
    """Clase para calcular medidas de tendencia central."""
    
    def __init__(self, tabla: pd.DataFrame):
        """
        Inicializa la clase con la tabla de distribución de frecuencias.
        
        Args:
            tabla: DataFrame con la tabla de frecuencias (sin fila de totales)
        """
        # Excluir la fila de totales
        self.tabla = tabla[tabla['Intervalo'] != 'TOTAL'].copy()
        self.n = int(tabla[tabla['Intervalo'] == 'TOTAL']['fi (Frec. Absoluta)'].values[0])
        
    def calcular_media(self) -> Tuple[float, Dict]:
        """
        Calcula la media aritmética para datos agrupados.
        
        Returns:
            Tupla con (resultado, diccionario de pasos)
        """
        pasos = {}
        
        # Crear tabla de cálculos
        tabla_calculos = self.tabla[['xi (Marca de Clase)', 'fi (Frec. Absoluta)']].copy()
        tabla_calculos['xi * fi'] = tabla_calculos['xi (Marca de Clase)'] * tabla_calculos['fi (Frec. Absoluta)']
        
        pasos['tabla'] = tabla_calculos
        
        # Calcular suma
        suma_xi_fi = tabla_calculos['xi * fi'].sum()
        pasos['suma_xi_fi'] = suma_xi_fi
        pasos['formula_suma'] = f"Σ(xi × fi) = {suma_xi_fi:.4f}"
        
        # Calcular media
        media = suma_xi_fi / self.n
        pasos['media'] = media
        pasos['formula_final'] = f"x̄ = Σ(xi × fi) / n = {suma_xi_fi:.4f} / {self.n} = {media:.2f}"
        
        return media, pasos
    
    def calcular_mediana(self) -> Tuple[float, Dict]:
        """
        Calcula la mediana para datos agrupados.
        
        Returns:
            Tupla con (resultado, diccionario de pasos)
        """
        pasos = {}
        
        # Posición de la mediana
        posicion_mediana = self.n / 2
        pasos['posicion'] = posicion_mediana
        pasos['formula_posicion'] = f"n/2 = {self.n}/2 = {posicion_mediana}"
        
        # Encontrar clase mediana (donde Fi >= n/2)
        clase_mediana_idx = None
        for idx, row in self.tabla.iterrows():
            if row['Fi (Frec. Acumulada)'] >= posicion_mediana:
                clase_mediana_idx = idx
                break
        
        clase_mediana = self.tabla.loc[clase_mediana_idx]
        pasos['clase_mediana'] = clase_mediana['Intervalo']
        
        # Parámetros para la fórmula
        Li = clase_mediana['Li']
        fi = clase_mediana['fi (Frec. Absoluta)']
        
        # Frecuencia acumulada anterior
        if clase_mediana_idx == self.tabla.index[0]:
            Fi_anterior = 0
        else:
            Fi_anterior = self.tabla.loc[clase_mediana_idx - 1, 'Fi (Frec. Acumulada)']
        
        # Amplitud (diferencia entre límites)
        A = clase_mediana['Ls'] - clase_mediana['Li']
        
        pasos['Li'] = Li
        pasos['fi'] = fi
        pasos['Fi_anterior'] = Fi_anterior
        pasos['A'] = A
        
        # Calcular mediana
        mediana = Li + ((posicion_mediana - Fi_anterior) / fi) * A
        
        pasos['formula'] = f"Me = Li + [(n/2 - Fi-1) / fi] × A"
        pasos['sustitucion'] = f"Me = {Li} + [({posicion_mediana} - {Fi_anterior}) / {fi}] × {A}"
        pasos['calculo'] = f"Me = {Li} + [{posicion_mediana - Fi_anterior} / {fi}] × {A}"
        pasos['resultado'] = mediana
        pasos['formula_final'] = f"Me = {mediana:.2f}"
        
        return mediana, pasos
    
    def calcular_moda(self) -> Tuple[float, Dict]:
        """
        Calcula la moda para datos agrupados.
        
        Returns:
            Tupla con (resultado, diccionario de pasos)
        """
        pasos = {}
        
        # Encontrar clase modal (mayor frecuencia)
        clase_modal_idx = self.tabla['fi (Frec. Absoluta)'].idxmax()
        clase_modal = self.tabla.loc[clase_modal_idx]
        
        pasos['clase_modal'] = clase_modal['Intervalo']
        pasos['fi_modal'] = clase_modal['fi (Frec. Absoluta)']
        
        # Parámetros para la fórmula
        Li = clase_modal['Li']
        fi_modal = clase_modal['fi (Frec. Absoluta)']
        
        # Frecuencia anterior
        if clase_modal_idx == self.tabla.index[0]:
            fi_anterior = 0
        else:
            fi_anterior = self.tabla.loc[clase_modal_idx - 1, 'fi (Frec. Absoluta)']
        
        # Frecuencia posterior
        if clase_modal_idx == self.tabla.index[-1]:
            fi_posterior = 0
        else:
            fi_posterior = self.tabla.loc[clase_modal_idx + 1, 'fi (Frec. Absoluta)']
        
        # Amplitud
        A = clase_modal['Ls'] - clase_modal['Li']
        
        # Diferencias
        d1 = fi_modal - fi_anterior
        d2 = fi_modal - fi_posterior
        
        pasos['Li'] = Li
        pasos['fi_modal'] = fi_modal
        pasos['fi_anterior'] = fi_anterior
        pasos['fi_posterior'] = fi_posterior
        pasos['d1'] = d1
        pasos['d2'] = d2
        pasos['A'] = A
        
        # Calcular moda
        if d1 + d2 == 0:
            moda = Li + A / 2  # Si no hay diferencia, usar punto medio
        else:
            moda = Li + (d1 / (d1 + d2)) * A
        
        pasos['formula'] = f"Mo = Li + [d1 / (d1 + d2)] × A"
        pasos['d1_formula'] = f"d1 = fi_modal - fi_anterior = {fi_modal} - {fi_anterior} = {d1}"
        pasos['d2_formula'] = f"d2 = fi_modal - fi_posterior = {fi_modal} - {fi_posterior} = {d2}"
        pasos['sustitucion'] = f"Mo = {Li} + [{d1} / ({d1} + {d2})] × {A}"
        pasos['resultado'] = moda
        pasos['formula_final'] = f"Mo = {moda:.2f}"
        
        return moda, pasos
