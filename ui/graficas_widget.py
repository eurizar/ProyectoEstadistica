"""
Widget para mostrar gráficas estadísticas.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt
import os


class GraficasWidget(QWidget):
    """Widget que muestra gráficas estadísticas."""
    
    def __init__(self):
        super().__init__()
        self.setupUI()
        
    def setupUI(self):
        """Configura la interfaz del widget."""
        layout = QVBoxLayout()
        layout.setSpacing(20)
        
        # Título
        titulo = QLabel("GRÁFICAS ESTADÍSTICAS")
        titulo.setStyleSheet("""
            QLabel {
                background-color: #2196F3;
                color: white;
                font-size: 14pt;
                font-weight: bold;
                padding: 8px;
                border-radius: 5px;
            }
        """)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)
        
        # Descripción
        descripcion = QLabel("Seleccione el tipo de gráfica que desea visualizar:")
        descripcion.setStyleSheet("font-size: 12pt; color: #555; padding: 10px;")
        descripcion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(descripcion)
        
        # Layout para botones
        botones_layout = QVBoxLayout()
        botones_layout.setSpacing(15)
        
        # Botón Gráfica de Barras
        self.btn_barras = QPushButton("Ver Gráfica de Barras")
        self.btn_barras.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 13pt;
                font-weight: bold;
                padding: 15px;
                border-radius: 8px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:disabled {
                background-color: #BDBDBD;
                color: #757575;
            }
        """)
        self.btn_barras.clicked.connect(self.mostrar_ventana_barras)
        self.btn_barras.setEnabled(False)
        botones_layout.addWidget(self.btn_barras)
        
        # Botón Gráfica de Pastel
        self.btn_pastel = QPushButton("Ver Gráfica de Pastel")
        self.btn_pastel.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 13pt;
                font-weight: bold;
                padding: 15px;
                border-radius: 8px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #388E3C;
            }
            QPushButton:disabled {
                background-color: #BDBDBD;
                color: #757575;
            }
        """)
        self.btn_pastel.clicked.connect(self.mostrar_ventana_pastel)
        self.btn_pastel.setEnabled(False)
        botones_layout.addWidget(self.btn_pastel)
        
        # Botón Gráfica de Puntos
        self.btn_puntos = QPushButton("Ver Gráfica de Puntos y Tendencias")
        self.btn_puntos.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                font-size: 13pt;
                font-weight: bold;
                padding: 15px;
                border-radius: 8px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
            QPushButton:disabled {
                background-color: #BDBDBD;
                color: #757575;
            }
        """)
        self.btn_puntos.clicked.connect(self.mostrar_ventana_puntos)
        self.btn_puntos.setEnabled(False)
        botones_layout.addWidget(self.btn_puntos)
        
        # Botón Histograma
        self.btn_histograma = QPushButton("Ver Histograma")
        self.btn_histograma.setStyleSheet("""
            QPushButton {
                background-color: #9C27B0;
                color: white;
                font-size: 13pt;
                font-weight: bold;
                padding: 15px;
                border-radius: 8px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #7B1FA2;
            }
            QPushButton:disabled {
                background-color: #BDBDBD;
                color: #757575;
            }
        """)
        self.btn_histograma.clicked.connect(self.mostrar_ventana_histograma)
        self.btn_histograma.setEnabled(False)
        botones_layout.addWidget(self.btn_histograma)
        
        layout.addLayout(botones_layout)
        layout.addStretch()
        
        self.setLayout(layout)
        
        # Variables para almacenar datos
        self.datos_grafica = None
        self.resultados = None
        
    def mostrar_graficas(self, tabla: pd.DataFrame, resultados: dict):
        """Prepara los datos para las gráficas y habilita los botones."""
        try:
            # Validar que la tabla tenga datos
            if tabla is None or len(tabla) <= 1:
                return
            
            # Guardar datos
            self.datos_grafica = {
                'intervalos': tabla['Intervalo'].iloc[:-1].tolist(),
                'frecuencias': tabla['fi (Frec. Absoluta)'].iloc[:-1].tolist(),
                'marcas_clase': tabla['xi (Marca de Clase)'].iloc[:-1].tolist(),
                'limites_inf': tabla['Li'].iloc[:-1].tolist(),
                'limites_sup': tabla['Ls'].iloc[:-1].tolist()
            }
            self.resultados = resultados
            
            # Habilitar botones
            self.btn_barras.setEnabled(True)
            self.btn_pastel.setEnabled(True)
            self.btn_puntos.setEnabled(True)
            self.btn_histograma.setEnabled(True)
            
        except Exception as e:
            print(f"Error al preparar gráficas: {e}")
            import traceback
            traceback.print_exc()
    
    def mostrar_ventana_barras(self):
        """Muestra la gráfica de barras en una ventana emergente."""
        if not self.datos_grafica:
            return
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Gráfica de Barras")
        dialog.setMinimumSize(900, 600)
        
        # Establecer icono
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'icono.ico')
        if os.path.exists(icon_path):
            dialog.setWindowIcon(QIcon(icon_path))
        
        layout = QVBoxLayout()
        
        fig = self.crear_grafica_barras(
            self.datos_grafica['intervalos'],
            self.datos_grafica['frecuencias']
        )
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        
        # Botón cerrar
        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                padding: 10px;
                font-size: 11pt;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #D32F2F;
            }
        """)
        btn_cerrar.clicked.connect(dialog.close)
        layout.addWidget(btn_cerrar)
        
        dialog.setLayout(layout)
        dialog.exec()
    
    def mostrar_ventana_pastel(self):
        """Muestra la gráfica de pastel en una ventana emergente."""
        if not self.datos_grafica:
            return
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Gráfica de Pastel")
        dialog.setMinimumSize(900, 600)
        
        # Establecer icono
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'icono.ico')
        if os.path.exists(icon_path):
            dialog.setWindowIcon(QIcon(icon_path))
        
        layout = QVBoxLayout()
        
        fig = self.crear_grafica_pastel(
            self.datos_grafica['intervalos'],
            self.datos_grafica['frecuencias']
        )
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        
        # Botón cerrar
        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                padding: 10px;
                font-size: 11pt;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #D32F2F;
            }
        """)
        btn_cerrar.clicked.connect(dialog.close)
        layout.addWidget(btn_cerrar)
        
        dialog.setLayout(layout)
        dialog.exec()
    
    def mostrar_ventana_histograma(self):
        """Muestra el histograma en una ventana emergente."""
        if not self.datos_grafica:
            return
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Histograma")
        dialog.setMinimumSize(1000, 600)
        
        # Establecer icono
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'icono.ico')
        if os.path.exists(icon_path):
            dialog.setWindowIcon(QIcon(icon_path))
        
        layout = QVBoxLayout()
        
        fig = self.crear_histograma(
            self.datos_grafica['limites_inf'],
            self.datos_grafica['limites_sup'],
            self.datos_grafica['frecuencias'],
            self.datos_grafica['marcas_clase']
        )
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        
        # Botón cerrar
        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                padding: 10px;
                font-size: 11pt;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #D32F2F;
            }
        """)
        btn_cerrar.clicked.connect(dialog.close)
        layout.addWidget(btn_cerrar)
        
        dialog.setLayout(layout)
        dialog.exec()
    
    def mostrar_ventana_puntos(self):
        """Muestra la gráfica de puntos en una ventana emergente."""
        if not self.datos_grafica:
            return
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Gráfica de Puntos y Tendencias")
        dialog.setMinimumSize(1000, 600)
        
        # Establecer icono
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'icono.ico')
        if os.path.exists(icon_path):
            dialog.setWindowIcon(QIcon(icon_path))
        
        layout = QVBoxLayout()
        
        fig = self.crear_grafica_puntos(
            self.datos_grafica['marcas_clase'],
            self.datos_grafica['frecuencias'],
            self.resultados
        )
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        
        # Botón cerrar
        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                padding: 10px;
                font-size: 11pt;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #D32F2F;
            }
        """)
        btn_cerrar.clicked.connect(dialog.close)
        layout.addWidget(btn_cerrar)
        
        dialog.setLayout(layout)
        dialog.exec()
        
    def crear_grafica_barras(self, intervalos, frecuencias):
        """Crea una gráfica de barras."""
        fig = Figure(figsize=(6, 4), facecolor='white')
        ax = fig.add_subplot(111)
        
        # Crear barras
        colores = plt.cm.Blues(range(50, 200, int(150/len(frecuencias))))
        barras = ax.bar(range(len(intervalos)), frecuencias, color=colores, edgecolor='black', linewidth=1.5)
        
        # Agregar valores sobre las barras
        for i, (barra, freq) in enumerate(zip(barras, frecuencias)):
            altura = barra.get_height()
            ax.text(barra.get_x() + barra.get_width()/2., altura,
                   f'{int(freq)}',
                   ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        # Configuración
        ax.set_xlabel('Intervalos', fontsize=11, fontweight='bold')
        ax.set_ylabel('Frecuencia Absoluta', fontsize=11, fontweight='bold')
        ax.set_title('Gráfica de Barras', fontsize=13, fontweight='bold', pad=15)
        ax.set_xticks(range(len(intervalos)))
        ax.set_xticklabels(intervalos, rotation=45, ha='right', fontsize=9)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        fig.tight_layout()
        return fig
        
    def crear_grafica_pastel(self, intervalos, frecuencias):
        """Crea una gráfica de pastel."""
        fig = Figure(figsize=(10, 6), facecolor='white')
        ax = fig.add_subplot(111)
        
        # Calcular total para porcentajes
        total = sum(frecuencias)
        
        # Crear gráfica de pastel sin etiquetas superpuestas
        colores = plt.cm.Set3(range(len(frecuencias)))
        
        # Función para mostrar porcentaje solo si es mayor a 3%
        def autopct_format(pct):
            return f'{pct:.1f}%' if pct > 3 else ''
        
        wedges, texts, autotexts = ax.pie(
            frecuencias, 
            labels=None,  # Sin etiquetas en el pastel
            autopct=autopct_format,
            startangle=90,
            colors=colores,
            textprops={'fontsize': 11, 'fontweight': 'bold'},
            pctdistance=0.80,
            explode=[0.02] * len(frecuencias)  # Pequeña separación entre porciones
        )
        
        # Mejorar texto de porcentajes
        for autotext in autotexts:
            autotext.set_color('black')
            autotext.set_fontsize(11)
            autotext.set_fontweight('bold')
        
        # Crear etiquetas para la leyenda con frecuencia y porcentaje
        labels_con_datos = []
        for intervalo, freq in zip(intervalos, frecuencias):
            porcentaje = (freq / total) * 100
            labels_con_datos.append(f'{intervalo}\n({int(freq)} - {porcentaje:.1f}%)')
        
        # Agregar leyenda fuera del gráfico
        ax.legend(wedges, labels_con_datos,
                 title="Intervalos\n(Frecuencia - %)",
                 loc="center left",
                 bbox_to_anchor=(1, 0, 0.5, 1),
                 fontsize=9,
                 title_fontsize=10,
                 frameon=True,
                 fancybox=True,
                 shadow=True)
        
        ax.set_title('Gráfica de Pastel - Distribución de Frecuencias', 
                    fontsize=14, fontweight='bold', pad=20)
        
        fig.tight_layout()
        return fig
        
    def crear_grafica_puntos(self, marcas_clase, frecuencias, resultados):
        """Crea una gráfica de puntos (dispersión) con líneas."""
        fig = Figure(figsize=(12, 4), facecolor='white')
        ax = fig.add_subplot(111)
        
        # Gráfica de puntos con líneas
        ax.plot(marcas_clase, frecuencias, 'o-', color='#2196F3', 
                linewidth=2.5, markersize=10, markerfacecolor='#1976D2',
                markeredgecolor='black', markeredgewidth=1.5, label='Frecuencia')
        
        # Agregar valores sobre los puntos
        for x, y in zip(marcas_clase, frecuencias):
            ax.text(x, y + max(frecuencias)*0.03, f'{int(y)}',
                   ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        # Líneas verticales para media, mediana y moda
        try:
            if 'tendencia_central' in resultados:
                tc = resultados['tendencia_central']
                # Intentar acceder a los valores con diferentes formatos posibles
                if 'media' in tc:
                    media_data = tc['media']
                    if isinstance(media_data, dict):
                        media = media_data.get('valor') or media_data.get('resultado', 0)
                    else:
                        media = media_data
                    
                    ax.axvline(media, color='#0D47A1', linestyle='--', linewidth=2, 
                              label=f'Media = {media:.2f}', alpha=0.7)
                
                if 'mediana' in tc:
                    mediana_data = tc['mediana']
                    if isinstance(mediana_data, dict):
                        mediana = mediana_data.get('valor') or mediana_data.get('resultado', 0)
                    else:
                        mediana = mediana_data
                    
                    ax.axvline(mediana, color='#1B5E20', linestyle='--', linewidth=2, 
                              label=f'Mediana = {mediana:.2f}', alpha=0.7)
                
                if 'moda' in tc:
                    moda_data = tc['moda']
                    if isinstance(moda_data, dict):
                        moda = moda_data.get('valor') or moda_data.get('resultado', 0)
                    else:
                        moda = moda_data
                    
                    ax.axvline(moda, color='#E65100', linestyle='--', linewidth=2, 
                              label=f'Moda = {moda:.2f}', alpha=0.7)
        except Exception as e:
            print(f"No se pudieron agregar líneas de tendencia: {e}")
        
        # Configuración
        ax.set_xlabel('Marca de Clase (xi)', fontsize=11, fontweight='bold')
        ax.set_ylabel('Frecuencia Absoluta', fontsize=11, fontweight='bold')
        ax.set_title('Gráfica de Puntos con Medidas de Tendencia Central', 
                    fontsize=13, fontweight='bold', pad=15)
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
        
        fig.tight_layout()
        return fig
    
    def crear_histograma(self, limites_inf, limites_sup, frecuencias, marcas_clase):
        """Crea un histograma con barras continuas."""
        fig = Figure(figsize=(12, 6), facecolor='white')
        ax = fig.add_subplot(111)
        
        # Crear los límites de los intervalos
        limites = limites_inf + [limites_sup[-1]]  # Agregar el último límite superior
        
        # Crear histograma con barras
        colores = plt.cm.Oranges(range(100, 250, int(150/len(frecuencias))))
        
        # Dibujar las barras del histograma
        for i, (li, ls, freq) in enumerate(zip(limites_inf, limites_sup, frecuencias)):
            ancho = ls - li
            ax.bar(li + ancho/2, freq, width=ancho, 
                  color=colores[i], edgecolor='black', linewidth=2,
                  alpha=0.8, align='center')
            
            # Agregar el valor de frecuencia sobre cada barra
            ax.text(li + ancho/2, freq, f'{int(freq)}',
                   ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        # Configuración
        ax.set_xlabel('Intervalos de Clase', fontsize=12, fontweight='bold')
        ax.set_ylabel('Frecuencia Absoluta', fontsize=12, fontweight='bold')
        ax.set_title('Histograma de Frecuencias', fontsize=14, fontweight='bold', pad=20)
        
        # Configurar el eje X con los límites de clase
        ax.set_xlim(limites[0] - (limites[1]-limites[0])*0.1, 
                    limites[-1] + (limites[-1]-limites[-2])*0.1)
        
        # Agregar líneas verticales en los límites
        for limite in limites:
            ax.axvline(limite, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)
        
        # Agregar etiquetas en el eje X
        ax.set_xticks(limites)
        ax.set_xticklabels([f'{l:.1f}' for l in limites], rotation=45, ha='right')
        
        # Grid
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        
        # Agregar polígono de frecuencias (línea que une las marcas de clase)
        ax.plot(marcas_clase, frecuencias, 'r-', linewidth=2.5, 
               marker='o', markersize=8, markerfacecolor='red',
               markeredgecolor='darkred', markeredgewidth=2,
               label='Polígono de Frecuencias', alpha=0.7)
        
        ax.legend(loc='upper right', fontsize=11, framealpha=0.9)
        
        fig.tight_layout()
        return fig
