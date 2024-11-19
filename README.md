# Máquina de Turing: Alterador y Reconocedor

Este proyecto implementa dos Máquinas de Turing:

1. **Alterador:** Procesa cadenas marcando sus símbolos desde el inicio y el final.
2. **Reconocedor:** Verifica si las cadenas cumplen con la forma \(a^n b^n\), es decir, si tienen una cantidad igual de `a` y `b` de forma consecutiva.

Ambas máquinas están diseñadas para fines educativos y pueden ejecutarse con configuraciones YAML personalizadas.

---

## Tabla de Contenidos

- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Cómo Personalizar la Máquina](#cómo-personalizar-la-máquina)
- [Pruebas](#pruebas)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Características

- **Alterador:**
  - Marca los símbolos de la cadena desde el inicio y el final.
  - Puede aceptar o rechazar cadenas según la configuración.
- **Reconocedor:**
  - Comprueba si la cadena es válida en la forma \(a^n b^n\).
  - Acepta cadenas válidas y rechaza las inválidas.

---

## Requisitos Previos

- Python 3.8 o superior
- Bibliotecas necesarias (instaladas automáticamente):

  - `pyyaml`
  - `colorama`

---

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone 
   cd PROYECTO_TC

2. **Crear un entorno virtual:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # En Windows: venv\Scripts\activate

2. **Instalar dependencias:**

    ```bash
    pip install -r colorama 
    pip install pyyaml

## Tabla de Contenidos

    python3 main.py

## Opciones disponibles

- **[1] Correr pruebas de Alterador:**
  - Verifica si la máquina Alterador funciona correctamente con cadenas de ejemplo.

- **[2] Correr pruebas de Reconocedor:**
  - Valida la máquina Reconocedor con cadenas que cumplen o no la regla \(a^n b^n\).

- **[0] Salir:**
  - Finaliza el programa.


