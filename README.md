# Laberinto Saltarín

Este proyecto resuelve el problema del **Laberinto Saltarín** utilizando algoritmos de búsqueda en grafos. Fue desarrollado como parte de la **Tarea 1** del curso **Inteligencia Artificial**.

---

## Descripción

El Laberinto Saltarín es una grilla $m \times n$ donde cada celda contiene un número que indica exactamente cuántas celdas puede saltar en dirección vertical u horizontal.

El objetivo es encontrar el **camino con la menor cantidad de movimientos** desde una posición inicial a una meta final, respetando las reglas de movimiento.

---

## Funcionalidades

- Carga **múltiples laberintos** desde un archivo `.txt`.
- Resolución del laberinto usando:
  - 🔵 **Búsqueda en Profundidad (DFS)**.
  - 🟢 **Búsqueda por Costo (unitario) Uniforme (UCS)**.
  - 🔴 **Búsqueda por Costo Uniforme (UCS2)**
- Visualización gráfica usando **Pygame**:
  - Representación del tablero.
  - Animación del avance paso a paso.
  - Cambio entre algoritmos en tiempo real.
  - Avance al siguiente laberinto.

---

## Estructura del Proyecto

- `laberintoSaltarin.py`: Clase que modela la lógica del laberinto.
- `dfs.py`: Implementación del algoritmo de búsqueda en profundidad.
- `ucs.py`: Implementación del algoritmo de búsqueda por costo uniforme con costos unitarios (cada movimiento cuesta 1).
- `ucs2.py`: Implementación del algoritmo de búsqueda por costo uniforme con costos variables (cada movimiento cuesta el número que tiene en la cuadrícula).
- `grafics.py`: Interfaz gráfica usando **Pygame**.
- `main.py`: Script principal que lanza la ejecución.
- `laberintos.txt`: Archivo de entrada con múltiples laberintos de ejemplo.

---

## Requisitos

- **Python 3.12+**
- **Pygame** (`pip install pygame`)
- **Numpy** (`pip install numpy`)

---

## 📦 Cómo ejecutar

```bash
git clone [https://github.com/Nikolexion/Tarea1IA.git]
python main.py
