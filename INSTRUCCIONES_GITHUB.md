# 📤 Guía para Subir el Proyecto a GitHub

## Pasos para Publicar en GitHub

### 1. Crear el Repositorio en GitHub
1. Ve a [GitHub](https://github.com) e inicia sesión
2. Haz clic en el botón **"New"** (repositorio nuevo)
3. Configura el repositorio:
   - **Nombre**: `ProyectoEstadistica` o `AnalizadorEstadistico`
   - **Descripción**: "Aplicación de escritorio para análisis estadístico de datos agrupados con PyQt6"
   - **Visibilidad**: Público (para que otros puedan descargarlo)
   - **NO marques** "Add README" (ya tenemos uno)
4. Haz clic en **"Create repository"**

### 2. Inicializar Git Local (Primera Vez)

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
cd C:\Users\eliza\Documents\ProyectoEstadistica

# Inicializar repositorio Git
git init

# Agregar todos los archivos
git add .

# Hacer el primer commit
git commit -m "🎉 Versión inicial: Analizador Estadístico completo con ejecutable"

# Conectar con GitHub (reemplaza USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/USUARIO/ProyectoEstadistica.git

# Renombrar rama a main
git branch -M main

# Subir al repositorio
git push -u origin main
```

### 3. Crear un Release con el Ejecutable

#### Opción A: Desde la Web de GitHub
1. Ve a tu repositorio en GitHub
2. Haz clic en **"Releases"** (lado derecho)
3. Haz clic en **"Create a new release"**
4. Configura el release:
   - **Tag version**: `v1.0.0`
   - **Release title**: `Analizador Estadístico v1.0.0`
   - **Description**: 
     ```
     🎉 Primera versión estable del Analizador Estadístico
     
     ## 📥 Descarga
     Descarga el archivo `AnalizadorEstadistico.exe` para Windows (no requiere Python)
     
     ## ✨ Características
     - Análisis de distribución de frecuencias
     - Medidas de tendencia central (Media, Mediana, Moda)
     - Medidas de dispersión (DM, DE)
     - 4 tipos de gráficas interactivas
     - Interfaz moderna con PyQt6
     ```
5. Arrastra el archivo `dist\AnalizadorEstadistico.exe` a la sección "Attach binaries"
6. Haz clic en **"Publish release"**

#### Opción B: Desde la Línea de Comandos (GitHub CLI)
```powershell
# Instalar GitHub CLI si no lo tienes: https://cli.github.com/

# Autenticarte
gh auth login

# Crear release y subir el ejecutable
gh release create v1.0.0 `
  dist/AnalizadorEstadistico.exe `
  --title "Analizador Estadístico v1.0.0" `
  --notes "Primera versión estable con ejecutable para Windows"
```

### 4. Actualizar Enlaces en README

Después de crear el release, actualiza el README.md:

1. Reemplaza `USUARIO` con tu usuario real de GitHub en todos los enlaces
2. Verifica que el enlace de descarga funcione:
   ```
   https://github.com/TU_USUARIO/ProyectoEstadistica/releases/download/v1.0.0/AnalizadorEstadistico.exe
   ```

### 5. Actualizaciones Futuras

Para subir cambios:

```powershell
# Ver archivos modificados
git status

# Agregar cambios
git add .

# Hacer commit con mensaje descriptivo
git commit -m "Descripción de los cambios"

# Subir a GitHub
git push
```

Para crear una nueva versión:

```powershell
# Crear nuevo tag
git tag v1.1.0

# Subir tag
git push origin v1.1.0

# Crear release en GitHub con el nuevo ejecutable
```

## 📋 Checklist Final

- [ ] Repositorio creado en GitHub
- [ ] Código subido con `git push`
- [ ] Release v1.0.0 creado
- [ ] Ejecutable AnalizadorEstadistico.exe subido al release
- [ ] Enlaces del README.md actualizados con tu usuario
- [ ] Verificar que el enlace de descarga funciona
- [ ] Agregar captura de pantalla (opcional pero recomendado)

## 🎨 Mejoras Opcionales

### Agregar Captura de Pantalla
1. Ejecuta la aplicación
2. Toma una captura de pantalla
3. Guárdala como `screenshot.png` en la carpeta del proyecto
4. Agrega al README después de los badges:
   ```markdown
   ![Screenshot](screenshot.png)
   ```

### Agregar Licencia
Crea un archivo `LICENSE` con la licencia MIT (o la que prefieras)

### Agregar Badge de Descargas
Después de tener descargas, el badge se actualizará automáticamente:
```markdown
[![Downloads](https://img.shields.io/github/downloads/USUARIO/ProyectoEstadistica/total)](https://github.com/USUARIO/ProyectoEstadistica/releases)
```

---

## ❓ Solución de Problemas

### "Git no reconocido como comando"
- Instala Git: https://git-scm.com/download/win

### "Permission denied (publickey)"
- Usa HTTPS en lugar de SSH, o configura SSH keys en GitHub

### El ejecutable no se sube (demasiado grande)
- GitHub permite archivos hasta 100 MB en releases (nuestro .exe es 69 MB, ✅ OK)
- Si fuera más grande, considera usar Git LFS o subir a otro servicio

### Windows Defender bloquea el ejecutable
- Es normal para aplicaciones sin firma digital
- Los usuarios pueden hacer clic en "Más información" → "Ejecutar de todas formas"

---

**¡Listo para Compartir!** 🚀

Una vez completados estos pasos, cualquier persona podrá:
- Ver tu código en GitHub
- Descargar el ejecutable con un clic
- Contribuir al proyecto
- Reportar issues

¡Mucho éxito con tu proyecto! 🎉
