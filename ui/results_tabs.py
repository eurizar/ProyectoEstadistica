"""
Widget con pestañas para mostrar los resultados del análisis estadístico.
"""

from PyQt6.QtWidgets import (QTabWidget, QWidget, QVBoxLayout, QTextEdit, 
                              QTableWidget, QTableWidgetItem, QLabel, QScrollArea, QHeaderView)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import pandas as pd
from .graficas_widget import GraficasWidget


class ResultsTabs(QTabWidget):
    """Widget con pestañas para mostrar todos los resultados."""
    
    def __init__(self):
        super().__init__()
        self.setupUI()
        
    def setupUI(self):
        """Configura las pestañas."""
        # Pestaña 1: Cálculos Preliminares
        self.tab_preliminares = QWidget()
        self.setup_tab_preliminares()
        self.addTab(self.tab_preliminares, "📋 Preliminares")
        
        # Pestaña 2: Tabla de Distribución
        self.tab_tabla = QWidget()
        self.setup_tab_tabla()
        self.addTab(self.tab_tabla, "📊 Tabla")
        
        # Pestaña 3: Tendencia Central
        self.tab_tendencia = QWidget()
        self.setup_tab_tendencia()
        self.addTab(self.tab_tendencia, "📈 Tendencia Central")
        
        # Pestaña 4: Dispersión
        self.tab_dispersion = QWidget()
        self.setup_tab_dispersion()
        self.addTab(self.tab_dispersion, "📉 Dispersión")
        
        # Pestaña 5: Gráficas
        self.tab_graficas = GraficasWidget()
        self.addTab(self.tab_graficas, "📊 Gráficas")
        
    def setup_tab_preliminares(self):
        """Configura la pestaña de cálculos preliminares."""
        layout = QVBoxLayout()
        self.text_preliminares = QTextEdit()
        self.text_preliminares.setReadOnly(True)
        self.text_preliminares.setFont(QFont("Courier New", 11))
        self.text_preliminares.setStyleSheet("""
            QTextEdit {
                background-color: white;
                color: #000000;
                border: 2px solid #2196F3;
                padding: 10px;
            }
        """)
        layout.addWidget(self.text_preliminares)
        self.tab_preliminares.setLayout(layout)
        
    def setup_tab_tabla(self):
        """Configura la pestaña de tabla de distribución."""
        layout = QVBoxLayout()
        self.tabla_widget = QTableWidget()
        layout.addWidget(self.tabla_widget)
        self.tab_tabla.setLayout(layout)
        
    def setup_tab_tendencia(self):
        """Configura la pestaña de tendencia central."""
        layout = QVBoxLayout()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { background-color: white; }")
        self.widget_tendencia = QWidget()
        self.widget_tendencia.setStyleSheet("QWidget { background-color: white; color: #000000; }")
        self.layout_tendencia = QVBoxLayout()
        self.widget_tendencia.setLayout(self.layout_tendencia)
        scroll.setWidget(self.widget_tendencia)
        layout.addWidget(scroll)
        self.tab_tendencia.setLayout(layout)
        
    def setup_tab_dispersion(self):
        """Configura la pestaña de dispersión."""
        layout = QVBoxLayout()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { background-color: white; }")
        self.widget_dispersion = QWidget()
        self.widget_dispersion.setStyleSheet("QWidget { background-color: white; color: #000000; }")
        self.layout_dispersion = QVBoxLayout()
        self.widget_dispersion.setLayout(self.layout_dispersion)
        scroll.setWidget(self.widget_dispersion)
        layout.addWidget(scroll)
        self.tab_dispersion.setLayout(layout)
        
    def updateResults(self, resultados: dict):
        """
        Actualiza todas las pestañas con los resultados calculados.
        
        Args:
            resultados: Diccionario con todos los resultados y pasos
        """
        self.mostrar_preliminares(resultados['preliminares'])
        self.mostrar_tabla(resultados['tabla'])
        self.mostrar_tendencia_central(resultados['tendencia_central'])
        self.mostrar_dispersion(resultados['dispersion'])
        
        # Mostrar gráficas
        self.tab_graficas.mostrar_graficas(resultados['tabla'], resultados)
        
    def mostrar_preliminares(self, pasos: dict):
        """Muestra los cálculos preliminares paso a paso."""
        texto = "=" * 60 + "\n"
        texto += "CÁLCULOS PRELIMINARES\n"
        texto += "=" * 60 + "\n\n"
        
        # Datos ordenados
        texto += "1. DATOS ORDENADOS:\n"
        datos = pasos['datos_ordenados']
        texto += f"   {datos}\n\n"
        
        # Mínimo y máximo
        texto += "2. VALOR MÍNIMO Y MÁXIMO:\n"
        texto += f"   Xmin = {pasos['x_min']}\n"
        texto += f"   Xmax = {pasos['x_max']}\n\n"
        
        # Rango
        texto += "3. RANGO:\n"
        texto += f"   {pasos['rango_formula']}\n\n"
        
        # Número de clases
        texto += "4. NÚMERO DE CLASES (Regla de Sturges):\n"
        texto += f"   {pasos['k_formula']}\n\n"
        
        # Amplitud
        texto += "5. AMPLITUD:\n"
        texto += f"   {pasos['amplitud_formula']}\n\n"
        
        texto += "=" * 60 + "\n"
        
        self.text_preliminares.setPlainText(texto)
        
    def mostrar_tabla(self, tabla: pd.DataFrame):
        """Muestra la tabla de distribución de frecuencias."""
        # Configurar tabla
        self.tabla_widget.setRowCount(len(tabla))
        self.tabla_widget.setColumnCount(len(tabla.columns))
        self.tabla_widget.setHorizontalHeaderLabels(tabla.columns)
        
        # Llenar tabla
        for i, row in tabla.iterrows():
            for j, (col_name, valor) in enumerate(row.items()):
                item = QTableWidgetItem()
                
                # Formatear valores
                if col_name == 'Intervalo':
                    item.setText(str(valor))
                elif isinstance(valor, (int, float)) and col_name != 'Li' and col_name != 'Ls':
                    if col_name in ['hi (Frec. Relativa)', 'hi% (Frec. Relativa %)']:
                        item.setText(f"{valor:.4f}" if col_name == 'hi (Frec. Relativa)' else f"{valor:.2f}")
                    elif col_name == 'xi (Marca de Clase)':
                        item.setText(f"{valor:.2f}")
                    else:
                        item.setText(str(int(valor)) if valor == int(valor) else str(valor))
                else:
                    item.setText(str(valor) if valor != '' else '')
                
                # Alinear a la derecha los números
                if col_name != 'Intervalo':
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                
                # Resaltar fila de totales
                if i == len(tabla) - 1:
                    font = item.font()
                    font.setBold(True)
                    item.setFont(font)
                
                self.tabla_widget.setItem(i, j, item)
        
        # Ajustar columnas al ancho disponible, pero permitir redimensionado manual
        self.tabla_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.tabla_widget.horizontalHeader().setStretchLastSection(True)
        
        # Establecer anchos iniciales de columnas (en píxeles)
        self.tabla_widget.setColumnWidth(0, 150)  # Intervalo
        self.tabla_widget.setColumnWidth(1, 80)   # Li
        self.tabla_widget.setColumnWidth(2, 80)   # Ls
        self.tabla_widget.setColumnWidth(3, 165)  # xi (Marca de Clase)
        self.tabla_widget.setColumnWidth(4, 165)  # fi (Frec. Absoluta)
        self.tabla_widget.setColumnWidth(5, 165)  # Fi (Frec. Acumulada)
        self.tabla_widget.setColumnWidth(6, 165)  # hi (Frec. Relativa)
        # La última columna (hi%) se estirará automáticamente
        
    def mostrar_tendencia_central(self, tc: dict):
        """Muestra las medidas de tendencia central con sus pasos."""
        # Limpiar layout anterior
        for i in reversed(range(self.layout_tendencia.count())):
            self.layout_tendencia.itemAt(i).widget().setParent(None)
        
        # MEDIA
        self.agregar_seccion_media(tc['media'])
        
        # MEDIANA
        self.agregar_seccion_mediana(tc['mediana'])
        
        # MODA
        self.agregar_seccion_moda(tc['moda'])
        
        self.layout_tendencia.addStretch()
        
    def agregar_seccion_media(self, pasos_media: dict):
        """Agrega la sección de media aritmética."""
        # Título
        titulo = QLabel("📊 MEDIA ARITMÉTICA")
        titulo_font = QFont()
        titulo_font.setPointSize(14)
        titulo_font.setBold(True)
        titulo.setFont(titulo_font)
        titulo.setStyleSheet("color: #0D47A1; background-color: #E3F2FD; padding: 10px; border-radius: 5px;")
        self.layout_tendencia.addWidget(titulo)
        
        # Fórmula
        formula = QLabel("Fórmula: x̄ = Σ(xi × fi) / n")
        formula.setFont(QFont("Courier New", 11))
        formula.setStyleSheet("color: #000000; padding: 5px;")
        self.layout_tendencia.addWidget(formula)
        
        # Tabla de cálculos
        tabla_df = pasos_media['tabla']
        tabla = QTableWidget()
        tabla.setRowCount(len(tabla_df))
        tabla.setColumnCount(len(tabla_df.columns))
        tabla.setHorizontalHeaderLabels(tabla_df.columns)
        
        for i, row in tabla_df.iterrows():
            for j, valor in enumerate(row):
                item = QTableWidgetItem(f"{valor:.4f}" if isinstance(valor, float) else str(int(valor)))
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                tabla.setItem(i, j, item)
        
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tabla.setMaximumHeight(200)
        self.layout_tendencia.addWidget(tabla)
        
        # Cálculo
        calculo = QLabel(f"• {pasos_media['formula_suma']}")
        calculo.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt; font-weight: bold;")
        self.layout_tendencia.addWidget(calculo)
        
        # Resultado
        resultado = QLabel(f"• {pasos_media['formula_final']}")
        resultado_font = QFont()
        resultado_font.setBold(True)
        resultado_font.setPointSize(12)
        resultado.setFont(resultado_font)
        resultado.setStyleSheet("color: #0D47A1; background-color: #E3F2FD; padding: 8px; border-left: 4px solid #2196F3;")
        self.layout_tendencia.addWidget(resultado)
        
        self.layout_tendencia.addSpacing(20)
        
    def agregar_seccion_mediana(self, pasos_mediana: dict):
        """Agrega la sección de mediana."""
        titulo = QLabel("📊 MEDIANA")
        titulo_font = QFont()
        titulo_font.setPointSize(14)
        titulo_font.setBold(True)
        titulo.setFont(titulo_font)
        titulo.setStyleSheet("color: #1B5E20; background-color: #E8F5E9; padding: 10px; border-radius: 5px;")
        self.layout_tendencia.addWidget(titulo)
        
        # Pasos
        paso_label = QLabel(f"• {pasos_mediana['formula_posicion']}")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt;")
        self.layout_tendencia.addWidget(paso_label)
        
        paso_label = QLabel(f"• Clase mediana: {pasos_mediana['clase_mediana']}")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt; font-weight: bold;")
        self.layout_tendencia.addWidget(paso_label)
        
        paso_label = QLabel(f"• {pasos_mediana['formula']}")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt;")
        self.layout_tendencia.addWidget(paso_label)
        
        paso_label = QLabel(f"• {pasos_mediana['sustitucion']}")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt;")
        self.layout_tendencia.addWidget(paso_label)
        
        paso_label = QLabel(f"• {pasos_mediana['calculo']}")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt;")
        self.layout_tendencia.addWidget(paso_label)
        
        # Resultado
        resultado = QLabel(f"• {pasos_mediana['formula_final']}")
        resultado_font = QFont()
        resultado_font.setBold(True)
        resultado_font.setPointSize(12)
        resultado.setFont(resultado_font)
        resultado.setStyleSheet("color: #1B5E20; background-color: #E8F5E9; padding: 8px; border-left: 4px solid #4CAF50;")
        self.layout_tendencia.addWidget(resultado)
        
        self.layout_tendencia.addSpacing(20)
        
    def agregar_seccion_moda(self, pasos_moda: dict):
        """Agrega la sección de moda."""
        titulo = QLabel("📊 MODA")
        titulo_font = QFont()
        titulo_font.setPointSize(14)
        titulo_font.setBold(True)
        titulo.setFont(titulo_font)
        titulo.setStyleSheet("color: #E65100; background-color: #FFF3E0; padding: 10px; border-radius: 5px;")
        self.layout_tendencia.addWidget(titulo)
        
        # Pasos
        paso_label = QLabel(f"• Clase modal: {pasos_moda['clase_modal']} (fi = {pasos_moda['fi_modal']})")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt; font-weight: bold;")
        self.layout_tendencia.addWidget(paso_label)
        
        paso_label = QLabel(f"• {pasos_moda['d1_formula']}")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt;")
        self.layout_tendencia.addWidget(paso_label)
        
        paso_label = QLabel(f"• {pasos_moda['d2_formula']}")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt;")
        self.layout_tendencia.addWidget(paso_label)
        
        paso_label = QLabel(f"• {pasos_moda['formula']}")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt;")
        self.layout_tendencia.addWidget(paso_label)
        
        paso_label = QLabel(f"• {pasos_moda['sustitucion']}")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt;")
        self.layout_tendencia.addWidget(paso_label)
        
        # Resultado
        resultado = QLabel(f"• {pasos_moda['formula_final']}")
        resultado_font = QFont()
        resultado_font.setBold(True)
        resultado_font.setPointSize(12)
        resultado.setFont(resultado_font)
        resultado.setStyleSheet("color: #E65100; background-color: #FFF3E0; padding: 8px; border-left: 4px solid #FF9800;")
        self.layout_tendencia.addWidget(resultado)
        
    def mostrar_dispersion(self, disp: dict):
        """Muestra las medidas de dispersión con sus pasos."""
        # Limpiar layout anterior
        for i in reversed(range(self.layout_dispersion.count())):
            self.layout_dispersion.itemAt(i).widget().setParent(None)
        
        # DESVIACIÓN MEDIA
        self.agregar_seccion_desviacion_media(disp['desviacion_media'])
        
        # DESVIACIÓN ESTÁNDAR
        self.agregar_seccion_desviacion_estandar(disp['desviacion_estandar'])
        
        self.layout_dispersion.addStretch()
        
    def agregar_seccion_desviacion_media(self, pasos_dm: dict):
        """Agrega la sección de desviación media."""
        titulo = QLabel("📉 DESVIACIÓN MEDIA")
        titulo_font = QFont()
        titulo_font.setPointSize(14)
        titulo_font.setBold(True)
        titulo.setFont(titulo_font)
        titulo.setStyleSheet("color: #01579B; background-color: #E1F5FE; padding: 10px; border-radius: 5px;")
        self.layout_dispersion.addWidget(titulo)
        
        # Fórmula
        formula = QLabel(f"Fórmula: DM = Σ|xi - x̄| × fi / n  (donde x̄ = {pasos_dm['media']:.2f})")
        formula.setFont(QFont("Courier New", 11))
        formula.setStyleSheet("color: #000000; padding: 5px;")
        self.layout_dispersion.addWidget(formula)
        
        # Tabla de cálculos
        tabla_df = pasos_dm['tabla']
        tabla = self.crear_tabla_from_df(tabla_df)
        tabla.setMaximumHeight(200)
        self.layout_dispersion.addWidget(tabla)
        
        # Cálculo
        paso_label = QLabel(f"• {pasos_dm['formula_suma']}")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt; font-weight: bold;")
        self.layout_dispersion.addWidget(paso_label)
        
        # Resultado
        resultado = QLabel(f"• {pasos_dm['formula_final']}")
        resultado_font = QFont()
        resultado_font.setBold(True)
        resultado_font.setPointSize(12)
        resultado.setFont(resultado_font)
        resultado.setStyleSheet("color: #01579B; background-color: #E1F5FE; padding: 8px; border-left: 4px solid #0288D1;")
        self.layout_dispersion.addWidget(resultado)
        
        self.layout_dispersion.addSpacing(20)
        
    def agregar_seccion_desviacion_estandar(self, pasos_de: dict):
        """Agrega la sección de desviación estándar."""
        titulo = QLabel("📉 DESVIACIÓN ESTÁNDAR")
        titulo_font = QFont()
        titulo_font.setPointSize(14)
        titulo_font.setBold(True)
        titulo.setFont(titulo_font)
        titulo.setStyleSheet("color: #263238; background-color: #ECEFF1; padding: 10px; border-radius: 5px;")
        self.layout_dispersion.addWidget(titulo)
        
        # Fórmula
        formula = QLabel(f"Fórmula: σ = √[Σ(xi - x̄)² × fi / n]  (donde x̄ = {pasos_de['media']:.2f})")
        formula.setFont(QFont("Courier New", 11))
        formula.setStyleSheet("color: #000000; padding: 5px;")
        self.layout_dispersion.addWidget(formula)
        
        # Tabla de cálculos
        tabla_df = pasos_de['tabla']
        tabla = self.crear_tabla_from_df(tabla_df)
        tabla.setMaximumHeight(200)
        self.layout_dispersion.addWidget(tabla)
        
        # Cálculos
        paso_label = QLabel(f"• {pasos_de['formula_suma']}")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt; font-weight: bold;")
        self.layout_dispersion.addWidget(paso_label)
        
        paso_label = QLabel(f"• {pasos_de['formula_varianza']}")
        paso_label.setStyleSheet("color: #000000; padding: 3px; font-size: 11pt; font-weight: bold;")
        self.layout_dispersion.addWidget(paso_label)
        
        # Resultado
        resultado = QLabel(f"• {pasos_de['formula_final']}")
        resultado_font = QFont()
        resultado_font.setBold(True)
        resultado_font.setPointSize(12)
        resultado.setFont(resultado_font)
        resultado.setStyleSheet("color: #263238; background-color: #ECEFF1; padding: 8px; border-left: 4px solid #546E7A;")
        self.layout_dispersion.addWidget(resultado)
        
    def crear_tabla_from_df(self, df: pd.DataFrame) -> QTableWidget:
        """Crea un QTableWidget desde un DataFrame."""
        tabla = QTableWidget()
        tabla.setRowCount(len(df))
        tabla.setColumnCount(len(df.columns))
        tabla.setHorizontalHeaderLabels(df.columns)
        
        for i, row in df.iterrows():
            for j, valor in enumerate(row):
                texto = f"{valor:.4f}" if isinstance(valor, float) else str(int(valor))
                item = QTableWidgetItem(texto)
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                tabla.setItem(i, j, item)
        
        # Ajustar columnas al ancho disponible
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        return tabla
