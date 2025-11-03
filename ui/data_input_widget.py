"""
Widget para la entrada de datos.
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QTextEdit, QPushButton, 
                              QLabel, QMessageBox, QHBoxLayout)
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QFont


class DataInputWidget(QWidget):
    """Widget para ingresar datos numéricos."""
    
    dataReady = pyqtSignal(list)  # Señal que emite los datos validados
    
    def __init__(self):
        super().__init__()
        self.setupUI()
        
    def setupUI(self):
        """Configura la interfaz del widget."""
        layout = QVBoxLayout()
        
        # Título
        titulo = QLabel("📊 ENTRADA DE DATOS")
        titulo_font = QFont()
        titulo_font.setPointSize(12)
        titulo_font.setBold(True)
        titulo.setFont(titulo_font)
        layout.addWidget(titulo)
        
        # Instrucciones
        instrucciones = QLabel(
            "Ingrese los datos numéricos separados por:\n"
            "• Comas (,)\n"
            "• Espacios\n"
            "• Saltos de línea"
        )
        layout.addWidget(instrucciones)
        
        # Área de texto para datos
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText(
            "Ejemplo:\n12, 15, 18, 20, 22\n25, 28, 30, 32, 35"
        )
        self.text_edit.setMinimumHeight(200)
        layout.addWidget(self.text_edit)
        
        # Label para mostrar cantidad de datos
        self.label_cantidad = QLabel("Datos ingresados: 0")
        layout.addWidget(self.label_cantidad)
        
        # Botones
        btn_layout = QHBoxLayout()
        
        self.btn_limpiar = QPushButton("LIMPIAR")
        self.btn_limpiar.clicked.connect(self.limpiar_datos)
        self.btn_limpiar.setStyleSheet("""
            QPushButton {
                background-color: #FFB74D;
                color: #000000;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FFA726;
            }
        """)
        btn_layout.addWidget(self.btn_limpiar)
        
        self.btn_calcular = QPushButton("CALCULAR")
        self.btn_calcular.clicked.connect(self.validar_y_calcular)
        self.btn_calcular.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        btn_layout.addWidget(self.btn_calcular)
        
        layout.addLayout(btn_layout)
        layout.addStretch()
        
        self.setLayout(layout)
        
    def limpiar_datos(self):
        """Limpia el área de texto y reinicia el contador."""
        self.text_edit.clear()
        self.label_cantidad.setText("Datos ingresados: 0")
        
    def validar_y_calcular(self):
        """Valida los datos ingresados y emite señal si son válidos."""
        texto = self.text_edit.toPlainText().strip()
        
        if not texto:
            QMessageBox.warning(
                self,
                "Datos vacíos",
                "Por favor, ingrese al menos 5 datos numéricos."
            )
            return
        
        # Separar por comas, espacios y saltos de línea
        import re
        elementos = re.split(r'[,\s\n]+', texto)
        elementos = [e.strip() for e in elementos if e.strip()]
        
        # Convertir a números
        datos = []
        for elemento in elementos:
            try:
                numero = float(elemento)
                datos.append(numero)
            except ValueError:
                QMessageBox.critical(
                    self,
                    "Error de formato",
                    f"El valor '{elemento}' no es un número válido."
                )
                return
        
        # Validar cantidad mínima
        if len(datos) < 5:
            QMessageBox.warning(
                self,
                "Datos insuficientes",
                f"Se necesitan al menos 5 datos. Actualmente hay {len(datos)}."
            )
            return
        
        # Actualizar label de cantidad
        self.label_cantidad.setText(f"Datos ingresados: {len(datos)}")
        
        # Emitir señal con datos validados
        self.dataReady.emit(datos)
