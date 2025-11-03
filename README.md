# 📊 Analizador Estadístico - Datos Agrupados

Aplicación de escritorio desarrollada en Python con PyQt6 para realizar análisis estadístico completo de datos agrupados, incluyendo distribución de frecuencias, medidas de tendencia central, medidas de dispersión y visualizaciones gráficas interactivas.

[![Download](https://img.shields.io/badge/Download-Ejecutable-blue?style=for-the-badge&logo=windows)](https://github.com/eurizar/ProyectoEstadistica/releases/latest)
[![Python](https://img.shields.io/badge/Python-3.9+-green?style=for-the-badge&logo=python)](https://www.python.org/)
[![PyQt6](https://img.shields.io/badge/PyQt6-GUI-orange?style=for-the-badge&logo=qt)](https://www.riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

## 💾 Descarga Directa

### Ejecutable para Windows (Recomendado)

**¿No tienes Python instalado? ¡No hay problema!**

Descarga el ejecutable independiente que funciona sin necesidad de instalar Python ni dependencias:

📥 **[Descargar AnalizadorEstadistico.exe](https://github.com/eurizar/ProyectoEstadistica/releases/download/v1.0.0/AnalizadorEstadistico.exe)** (69 MB)

**Características del ejecutable:**
- ✅ No requiere instalación
- ✅ No necesita Python
- ✅ Incluye todas las dependencias
- ✅ Compatible con Windows 10/11 (64-bit)
- ✅ Un solo archivo .exe
- ✅ Doble clic y listo

**Instrucciones:**
1. Descarga el archivo `AnalizadorEstadistico.exe`
2. Haz doble clic para ejecutar
3. ¡Comienza a analizar tus datos!

> **Nota de Seguridad**: Si Windows Defender bloquea el ejecutable, haz clic en "Más información" → "Ejecutar de todas formas". Esto es normal para aplicaciones no firmadas digitalmente.

---

## 🎯 Características Principales

### 📈 Análisis Estadístico Completo
- **Distribución de Frecuencias**: Cálculo automático usando la Regla de Sturges
- **Medidas de Tendencia Central**: Media aritmética, Mediana y Moda
- **Medidas de Dispersión**: Desviación Media y Desviación Estándar
- **Cálculos Paso a Paso**: Muestra todo el proceso de cálculo detalladamente

### 📊 Visualizaciones Gráficas
- **Gráfica de Barras**: Visualización de frecuencias absolutas por intervalo
- **Gráfica de Pastel**: Distribución porcentual con leyenda externa
- **Gráfica de Puntos**: Frecuencias con líneas de tendencia central (Media, Mediana, Moda)
- **Histograma**: Representación continua con polígono de frecuencias

### 🎨 Interfaz de Usuario
- Diseño moderno y profesional con colores de alto contraste
- 5 pestañas organizadas para fácil navegación
- Tablas interactivas con columnas redimensionables
- Ventanas emergentes independientes para cada gráfica
- Validación de datos en tiempo real
- Icono personalizado en todas las ventanas

## 🚀 Instalación

### Requisitos Previos
- Python 3.9 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd ProyectoEstadistica
   ```

2. **Crear entorno virtual (recomendado)**
   ```bash
   python -m venv .venv
   ```

3. **Activar el entorno virtual**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Dependencias

El proyecto utiliza las siguientes bibliotecas:

```
PyQt6 >= 6.4.0          # Framework de interfaz gráfica
numpy >= 1.24.0         # Cálculos numéricos
pandas >= 2.0.0         # Manipulación de datos y tablas
matplotlib >= 3.7.0     # Generación de gráficas
```

## 🎮 Uso de la Aplicación

### Ejecutar la Aplicación

```bash
python main.py
```

### Flujo de Trabajo

1. **Ingresar Datos**
   - En el panel izquierdo, ingrese sus datos numéricos
   - Los datos pueden estar separados por: comas, espacios o saltos de línea
   - Mínimo requerido: 5 datos
   - Ejemplo: `12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40`

2. **Calcular Análisis**
   - Haga clic en el botón azul **"Calcular"**
   - La aplicación procesará los datos automáticamente
   - Se mostrarán los resultados en las 5 pestañas

3. **Revisar Resultados**
   - **Preliminares**: Datos ordenados, valores extremos, rango, número de clases y amplitud
   - **Tabla**: Tabla completa de distribución de frecuencias
   - **Tendencia Central**: Cálculos detallados de Media, Mediana y Moda
   - **Dispersión**: Cálculos de Desviación Media y Desviación Estándar
   - **Gráficas**: Botones para visualizar 4 tipos de gráficas

4. **Ver Gráficas**
   - Haga clic en cualquier botón de la pestaña "Gráficas"
   - Cada gráfica se abre en una ventana independiente
   - Puede abrir múltiples gráficas simultáneamente

5. **Limpiar y Nueva Consulta**
   - Use el botón naranja **"Limpiar"** para borrar los datos
   - O use el menú **Archivo → Limpiar Datos**

## 📋 Estructura del Proyecto

```
ProyectoEstadistica/
│
├── main.py                          # Punto de entrada de la aplicación
├── requirements.txt                  # Dependencias del proyecto
├── README.md                         # Documentación
├── icono.ico                         # Icono de la aplicación
│
├── core/                            # Lógica de negocio
│   ├── __init__.py
│   ├── distribucion_frecuencia.py   # Cálculo de distribución de frecuencias
│   ├── tendencia_central.py         # Cálculo de media, mediana, moda
│   ├── dispersion.py                # Cálculo de desviación media y estándar
│   └── estadistica.py               # Coordinador principal de análisis
│
└── ui/                              # Interfaz de usuario
    ├── __init__.py
    ├── main_window.py               # Ventana principal
    ├── data_input_widget.py         # Panel de entrada de datos
    ├── results_tabs.py              # Pestañas de resultados
    └── graficas_widget.py           # Widget de gráficas
```

## 📊 Detalles Técnicos

### Cálculos Estadísticos

#### 1. Distribución de Frecuencias
- **Regla de Sturges**: k = 1 + 3.322 × log₁₀(n)
- **Amplitud de clase**: A = Rango / k
- **Intervalos de clase**: [Li - Ls)
- **Frecuencias calculadas**:
  - fi: Frecuencia absoluta
  - Fi: Frecuencia acumulada
  - hi: Frecuencia relativa
  - hi%: Frecuencia relativa porcentual

#### 2. Medidas de Tendencia Central
- **Media Aritmética**: x̄ = Σ(xi × fi) / n
- **Mediana**: Me = Li + [(n/2 - Fi-1) / fi] × A
- **Moda**: Mo = Li + [d1 / (d1 + d2)] × A

#### 3. Medidas de Dispersión
- **Desviación Media**: DM = Σ|xi - x̄| × fi / n
- **Desviación Estándar**: σ = √[Σ(xi - x̄)² × fi / n]

### Arquitectura del Software

- **Patrón MVC**: Separación entre lógica de negocio (core) y presentación (ui)
- **Signals y Slots**: Comunicación entre componentes usando el sistema de Qt
- **Validación de Datos**: Verificación en tiempo real de la entrada del usuario
- **Manejo de Errores**: Try-catch en todas las operaciones críticas

## 🎨 Características de la Interfaz

### Paleta de Colores
- **Azul** (#2196F3): Botón Calcular, Encabezados, Gráfica de Barras
- **Naranja** (#FFB74D): Botón Limpiar
- **Verde** (#4CAF50): Gráfica de Pastel
- **Naranja Oscuro** (#FF9800): Gráfica de Puntos
- **Morado** (#9C27B0): Histograma
- **Rojo** (#F44336): Botones Cerrar

### Elementos Visuales
- Tablas con bordes de 2px y alto contraste
- Fuentes de 11-14pt para legibilidad
- Iconos emoji para identificación rápida
- Tooltips y mensajes informativos
- Botones deshabilitados hasta tener datos válidos

## 🔧 Funcionalidades Avanzadas

### Tablas Interactivas
- **Redimensionamiento manual** de columnas (estilo Excel)
- **Anchos iniciales optimizados** para cada columna
- **Última columna expandible** para usar todo el espacio
- **Resaltado de fila de totales** en negrita

### Ventanas de Gráficas
- **Independientes**: Cada gráfica en su propia ventana
- **Redimensionables**: Ajuste el tamaño según necesidad
- **Múltiples simultáneas**: Abra varias gráficas a la vez
- **Botón cerrar integrado**: Fácil cierre de ventanas

### Validación de Datos
- Mínimo 5 datos requeridos
- Solo acepta números (enteros o decimales)
- Mensajes de error descriptivos
- Contador de datos en tiempo real

## 📖 Ejemplos de Uso

### Ejemplo 1: Datos de Calificaciones
```
65, 72, 78, 85, 90, 68, 75, 82, 88, 95,
70, 77, 83, 89, 92, 66, 73, 80, 86, 93
```

### Ejemplo 2: Datos de Edades
```
18 20 22 25 28 30 32 35 38 40
42 45 48 50 52 55 58 60 62 65
```

### Ejemplo 3: Datos de Ventas
```
1200, 1500, 1800, 2100, 2400, 2700, 3000,
3300, 3600, 3900, 4200, 4500, 4800, 5100
```

## 🐛 Solución de Problemas

### Error: "No module named 'PyQt6'"
```bash
pip install PyQt6
```

### Error: "No se pudieron crear las gráficas"
- Verifique que matplotlib esté instalado: `pip install matplotlib`
- Asegúrese de tener al menos 5 datos válidos

### La aplicación no muestra el icono
- Verifique que el archivo `icono.ico` exista en la carpeta raíz
- El icono debe estar en formato .ico

### Las tablas no se ven correctamente
- Asegúrese de tener la última versión de PyQt6
- Intente maximizar la ventana para ver todas las columnas

## 👨‍💻 Desarrollo

### Agregar Nuevas Funcionalidades

Para extender la aplicación, puede:

1. **Agregar nuevos cálculos** en la carpeta `core/`
2. **Crear nuevas pestañas** en `ui/results_tabs.py`
3. **Agregar nuevas gráficas** en `ui/graficas_widget.py`

### Estilo de Código
- PEP 8 para nomenclatura
- Docstrings en todas las funciones
- Type hints cuando sea posible
- Comentarios descriptivos

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

Esto significa que puedes:
- ✅ Usar el código comercialmente
- ✅ Modificar el código
- ✅ Distribuir el código
- ✅ Usar de forma privada

## 👤 Desarrollado Por

**Esvin Elizandro Urizar**  
📧 Email: elizandrou@outlook.com  
🎓 Carné: 0902-24-3618  
🏫 Programa: Ingeniería en Sistemas y Ciencias de la Computación  

Para preguntas, sugerencias o reportar problemas, envía un correo electrónico o abre un [Issue en GitHub](https://github.com/eurizar/ProyectoEstadistica/issues).

## 🎓 Créditos

Desarrollado como herramienta educativa para análisis estadístico de datos agrupados.

### Tecnologías Utilizadas
- **PyQt6**: Framework de interfaz gráfica
- **NumPy**: Cálculos numéricos eficientes
- **Pandas**: Manipulación de datos tabulares
- **Matplotlib**: Generación de gráficas científicas

---

## 📚 Referencias Estadísticas

- **Regla de Sturges**: Sturges, H. A. (1926). "The choice of a class interval"
- **Estadística Descriptiva**: Métodos clásicos de análisis de datos agrupados
- **Visualización de Datos**: Principios de gráficas estadísticas

---

**Versión**: 1.0.0  
**Última Actualización**: Noviembre 2025  
**Estado**: Producción ✅

---

## 🎉 ¡Gracias por usar el Analizador Estadístico!

Esta aplicación fue diseñada para hacer el análisis estadístico más accesible e intuitivo. Esperamos que sea de gran utilidad en sus proyectos académicos o profesionales.
