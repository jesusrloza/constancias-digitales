## 01 Debloat windows 10 (ChrisTitus)

```PowerShell
iwr -useb https://git.io/JJ8R4 | iex
```

Consultar:

- [Github](https://github.com/ChrisTitusTech/win10script)
- [Debloat Windows in 2022](https://www.christitus.com/debloat-windows-10-2020/)

## 02 - [opcional] Instalar chocolatey

https://chocolatey.org/
https://chocolatey.org/install

## 03 - Instalar software

```PowerShell
# Terminal de windows y programas de CLI
choco install microsoft-windows-terminal git neovim -y

# Programas de GUI
choco install keepassxc transmission sumatrapdf mpv sharex vscode  -y

# WinCDEmu arroja errores pero instala correctamente
choco install wincdemu -y

```
