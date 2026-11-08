<div align="center">

# 🕵️‍♂️ Windows Keylogger Research (PoC)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/OS-Windows_10%2F11-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Security](https://img.shields.io/badge/Category-Cybersecurity-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)

**Una Prueba de Concepto (PoC) avanzada para la investigación de captura de entrada y persistencia en entornos Windows.**

*Descargo de responsabilidad: Este proyecto ha sido creado estrictamente con fines educativos y de investigación en ciberseguridad.*

</div>

---

## 📖 Descripción General

Este proyecto es una **Prueba de Concepto (Proof of Concept)** diseñada para demostrar cómo operan las técnicas de captura de pulsaciones (Keylogging) a nivel de sistema operativo. El script implementa varias tácticas de persistencia y exfiltración de datos, simulando el comportamiento de amenazas avanzadas (APTs) en un entorno controlado.

> ⚠️ **ADVERTENCIA LEGAL:** El uso de esta herramienta para interceptar comunicaciones sin el consentimiento explícito del propietario es **ilegal** y viola las leyes de privacidad. El autor no se hace responsable del uso indebido de este software. Úsalo exclusivamente en máquinas virtuales o dispositivos de tu propiedad.

---

## ✨ Características Principales

| Característica | Descripción |
| :--- | :--- |
| ⌨️ **Captura Global** | Intercepta todas las pulsaciones usando `pynput`, incluyendo teclas especiales (Ctrl, Alt, Enter, etc.). |
| 🔄 **Persistencia (Registry)** | Se añade automáticamente al inicio de Windows usando la clave de registro `HKCU\...\Run`. |
| 🛡️ **Evasión de Sandbox** | Detecta si se está ejecutando dentro de una máquina virtual (VMware, VirtualBox, QEMU) y se detiene. |
| 📡 **Exfiltración Automática** | Envía los registros a un Webhook (ej. Discord) de forma asíncrona cada 60 segundos sin bloquear el sistema. |
| 📝 **Registro Local** | Guarda un respaldo de las capturas en un archivo local `KeyStrokes.txt`. |

---

## 🚀 Instalación y Uso

### 1. Requisitos Previos
Asegúrate de tener **Python 3.8+** instalado en tu sistema Windows.

### 2. Clonar el repositorio
```bash
git clone https://github.com/jose-grito/windows-keylogger-research.git
cd windows-keylogger-research
