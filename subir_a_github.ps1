# Script para subir el proyecto a GitHub
# Reemplaza USUARIO con tu usuario de GitHub antes de ejecutar

# Navegar a la carpeta del proyecto
Set-Location "C:\Users\eliza\Documents\ProyectoEstadistica"

# Verificar que Git esté instalado
$gitInstalled = Get-Command git -ErrorAction SilentlyContinue
if (-not $gitInstalled) {
    Write-Host "❌ Git no está instalado. Descárgalo desde: https://git-scm.com/download/win" -ForegroundColor Red
    exit
}

Write-Host "🚀 Iniciando proceso de subida a GitHub..." -ForegroundColor Cyan
Write-Host ""

# Solicitar usuario de GitHub
$usuario = Read-Host "Ingresa tu usuario de GitHub"

if ([string]::IsNullOrWhiteSpace($usuario)) {
    Write-Host "❌ Debes ingresar un usuario válido" -ForegroundColor Red
    exit
}

# Inicializar Git (si no está inicializado)
if (-not (Test-Path ".git")) {
    Write-Host "📦 Inicializando repositorio Git..." -ForegroundColor Yellow
    git init
} else {
    Write-Host "✅ Repositorio Git ya inicializado" -ForegroundColor Green
}

# Agregar todos los archivos
Write-Host "📝 Agregando archivos al repositorio..." -ForegroundColor Yellow
git add .

# Hacer commit
Write-Host "💾 Creando commit inicial..." -ForegroundColor Yellow
git commit -m "🎉 Versión inicial: Analizador Estadístico completo con ejecutable"

# Renombrar rama a main
Write-Host "🔄 Configurando rama principal..." -ForegroundColor Yellow
git branch -M main

# Agregar remote origin
$repoUrl = "https://github.com/$usuario/ProyectoEstadistica.git"
Write-Host "🔗 Conectando con GitHub: $repoUrl" -ForegroundColor Yellow

# Verificar si ya existe un remote
$existingRemote = git remote get-url origin 2>$null
if ($existingRemote) {
    git remote set-url origin $repoUrl
} else {
    git remote add origin $repoUrl
}

Write-Host ""
Write-Host "⚠️  IMPORTANTE: Ahora debes crear el repositorio en GitHub" -ForegroundColor Magenta
Write-Host ""
Write-Host "1. Ve a https://github.com/new" -ForegroundColor White
Write-Host "2. Nombre del repositorio: ProyectoEstadistica" -ForegroundColor White
Write-Host "3. Descripción: Aplicación de escritorio para análisis estadístico de datos agrupados" -ForegroundColor White
Write-Host "4. Visibilidad: Público" -ForegroundColor White
Write-Host "5. NO agregues README, .gitignore ni LICENSE (ya los tenemos)" -ForegroundColor White
Write-Host "6. Haz clic en 'Create repository'" -ForegroundColor White
Write-Host ""

$continuar = Read-Host "¿Ya creaste el repositorio en GitHub? (s/n)"

if ($continuar -eq "s" -or $continuar -eq "S") {
    Write-Host ""
    Write-Host "📤 Subiendo archivos a GitHub..." -ForegroundColor Yellow
    
    try {
        git push -u origin main
        Write-Host ""
        Write-Host "✅ ¡Proyecto subido exitosamente a GitHub!" -ForegroundColor Green
        Write-Host ""
        Write-Host "🎉 Próximos pasos:" -ForegroundColor Cyan
        Write-Host "1. Ve a: https://github.com/$usuario/ProyectoEstadistica/releases/new" -ForegroundColor White
        Write-Host "2. Tag version: v1.0.0" -ForegroundColor White
        Write-Host "3. Release title: Analizador Estadístico v1.0.0" -ForegroundColor White
        Write-Host "4. Arrastra el archivo: dist\AnalizadorEstadistico.exe" -ForegroundColor White
        Write-Host "5. Haz clic en 'Publish release'" -ForegroundColor White
        Write-Host ""
        Write-Host "📝 Recuerda actualizar los enlaces en README.md con tu usuario: $usuario" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "🌐 Tu proyecto estará en: https://github.com/$usuario/ProyectoEstadistica" -ForegroundColor Cyan
    }
    catch {
        Write-Host ""
        Write-Host "❌ Error al subir a GitHub: $_" -ForegroundColor Red
        Write-Host ""
        Write-Host "Verifica que:" -ForegroundColor Yellow
        Write-Host "- El repositorio existe en GitHub" -ForegroundColor White
        Write-Host "- Tienes permisos de escritura" -ForegroundColor White
        Write-Host "- Tu usuario/contraseña de Git están configurados" -ForegroundColor White
    }
} else {
    Write-Host ""
    Write-Host "⏸️  Proceso detenido. Ejecuta este script nuevamente cuando hayas creado el repositorio." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Presiona cualquier tecla para salir..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
