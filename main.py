"""
Punto de entrada principal de la aplicación.
"""

import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow


def main():
    """Función principal que inicia la aplicación."""
    app = QApplication(sys.argv)
    
    # Configurar estilo de la aplicación
    app.setStyle("Fusion")
    
    # Crear y mostrar ventana principal
    window = MainWindow()
    window.show()
    
    # Ejecutar aplicación
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
