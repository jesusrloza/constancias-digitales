# Instalar chocolatey (PowerShell como Administrador). Instrucciones en: https://chocolatey.org/ 

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

Write-Host "Reiniciar PowerShell y ejecutar 02_install_everything_else.ps1"
