"""
Ventana principal de la aplicación.
"""

from PyQt6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
                              QSplitter, QMessageBox, QMenuBar, QMenu)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from .data_input_widget import DataInputWidget
from .results_tabs import ResultsTabs
from core.estadistica import AnalizadorEstadistico
import os


class MainWindow(QMainWindow):
    """Ventana principal de la aplicación."""
    
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.connectSignals()
        
    def setupUI(self):
        """Configura la interfaz de usuario."""
        self.setWindowTitle("Analizador Estadístico - Datos Agrupados")
        self.setMinimumSize(1200, 800)
        
        # Establecer icono de la ventana
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'icono.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # Crear menú
        self.create_menu()
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Splitter para dividir la ventana
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Panel izquierdo: Entrada de datos
        self.data_input = DataInputWidget()
        self.data_input.setMaximumWidth(400)
        splitter.addWidget(self.data_input)
        
        # Panel derecho: Resultados
        self.results_tabs = ResultsTabs()
        splitter.addWidget(self.results_tabs)
        
        # Proporciones del splitter
        splitter.setSizes([300, 900])
        
        main_layout.addWidget(splitter)
        
        # Estilo de la ventana
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QWidget {
                color: #000000;
            }
            QLabel {
                color: #000000;
                font-size: 11pt;
            }
            QTextEdit {
                border: 2px solid #2196F3;
                border-radius: 5px;
                padding: 8px;
                background-color: white;
                color: #000000;
                font-size: 11pt;
            }
            QPushButton {
                padding: 10px 15px;
                border-radius: 5px;
                border: none;
                font-size: 11pt;
                font-weight: bold;
            }
            QTableWidget {
                border: 2px solid #2196F3;
                gridline-color: #cccccc;
                background-color: white;
                color: #000000;
                font-size: 11pt;
            }
            QTableWidget::item {
                padding: 8px;
                color: #000000;
            }
            QTableWidget::item:selected {
                background-color: #BBDEFB;
                color: #000000;
            }
            QHeaderView::section {
                background-color: #1976D2;
                color: white;
                padding: 8px;
                border: 1px solid #0D47A1;
                font-weight: bold;
                font-size: 11pt;
            }
            QTabWidget::pane {
                border: 2px solid #2196F3;
                background-color: white;
            }
            QTabBar::tab {
                background-color: #e0e0e0;
                color: #000000;
                padding: 10px 20px;
                margin-right: 2px;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                font-size: 11pt;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background-color: #2196F3;
                color: white;
            }
            QTabBar::tab:hover {
                background-color: #BBDEFB;
            }
            QScrollArea {
                background-color: white;
            }
            QMessageBox {
                background-color: white;
                color: #000000;
            }
            QMessageBox QLabel {
                color: #000000;
                font-size: 11pt;
            }
            QMessageBox QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
                min-width: 80px;
            }
            QMessageBox QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        
    def create_menu(self):
        """Crea el menú de la aplicación."""
        menubar = self.menuBar()
        
        # Menú Archivo
        menu_archivo = menubar.addMenu("Archivo")
        
        action_salir = QAction("Salir", self)
        action_salir.setShortcut("Ctrl+Q")
        action_salir.triggered.connect(self.close)
        menu_archivo.addAction(action_salir)
        
        # Menú Ayuda
        menu_ayuda = menubar.addMenu("Ayuda")
        
        action_acerca = QAction("Acerca de", self)
        action_acerca.triggered.connect(self.mostrar_acerca_de)
        menu_ayuda.addAction(action_acerca)
        
    def connectSignals(self):
        """Conecta las señales de los widgets."""
        self.data_input.dataReady.connect(self.procesar_datos)
        
    def procesar_datos(self, datos: list):
        """
        Procesa los datos ingresados y muestra los resultados.
        
        Args:
            datos: Lista de valores numéricos validados
        """
        try:
            # Crear analizador estadístico
            analizador = AnalizadorEstadistico(datos)
            
            # Calcular todo
            analizador.calcular_todo()
            
            # Obtener resultados paso a paso
            resultados = analizador.obtener_paso_a_paso()
            
            # Actualizar pestañas de resultados
            self.results_tabs.updateResults(resultados)
            
            # Cambiar a la primera pestaña de resultados
            self.results_tabs.setCurrentIndex(0)
            
            # Mostrar mensaje de éxito
            QMessageBox.information(
                self,
                "Cálculos completados",
                f"Se han procesado {len(datos)} datos exitosamente.\n"
                "Revise las pestañas para ver los resultados detallados."
            )
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error en el cálculo",
                f"Ocurrió un error al procesar los datos:\n{str(e)}"
            )
            
    def mostrar_acerca_de(self):
        """Muestra el diálogo Acerca de."""
        QMessageBox.about(
            self,
            "Acerca de Analizador Estadístico",
            "<h3>Analizador Estadístico</h3>"
            "<p>Aplicación para análisis estadístico de datos agrupados.</p>"
            "<p><b>Características:</b></p>"
            "<ul>"
            "<li>Distribución de frecuencias</li>"
            "<li>Medidas de tendencia central</li>"
            "<li>Medidas de dispersión</li>"
            "<li>Cálculos paso a paso</li>"
            "</ul>"
            "<p><b>Versión:</b> 1.0</p>"
            "<p><b>Desarrollado con:</b> Python y PyQt6</p>"
        )
