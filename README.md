# **Análisis de Imágenes y Generación de Prompts con Stable Diffusion**

Este proyecto implementa un sistema que analiza características visuales de imágenes y genera un **prompt personalizado** para herramientas de generación de imágenes como **Stable Diffusion**. Incluye análisis de brillo, contraste, textura y una paleta de colores dominantes.

## **Características del Proyecto**
- **Análisis de Imágenes:**
  - Cálculo de brillo, contraste y textura.
  - Generación de una paleta de colores dominantes utilizando K-Means.
- **Comparación de Imágenes:**
  - Determinación de la imagen ganadora basada en características analizadas.
  - Historial de características almacenadas.
- **Generación de Prompts:**
  - Creación de descripciones detalladas para aplicaciones como Stable Diffusion.
  - Inclusión de características visuales y colores dominantes.

## **Requisitos**
- Python 3.8+
- Bibliotecas necesarias:
  - `opencv-python`
  - `numpy`
  - `matplotlib`
  - `scikit-learn`

Puedes instalar las dependencias ejecutando:

```bash
pip install opencv-python numpy matplotlib scikit-learn`
```
## **Uso**
- **Carga de Imágenes**
  Especifica las rutas de dos imágenes en las variables ruta_imagenA y ruta_imagenB.

- **Análisis y Comparación**
  El script analizará ambas imágenes y determinará la ganadora según las características.

- **Generación de Prompt**
Se genera un prompt para crear una imagen con características similares a la ganadora.

- **Ejecución del Script**
  Ejecuta el script principal:

```bash
python script.py
```
## **Resultados**
Los resultados incluyen:
- **Características de ambas imágenes.**
    - **Paleta de colores de la imagen ganadora.**
    - **Prompt generado para herramientas de generación de imágenes.**

## **Estructura del Código**
**Funciones principales:**
- `mostrar_imagen(img)`: Muestra una imagen en pantalla.
- `extraer_paleta_de_colores(img, num_clusters)`: Obtiene los colores dominantes.
- `mostrar_paleta(colores_proporcion)`: Visualiza una paleta de colores.
- `cargar_y_extraer_caracteristicas(ruta_imagen)`: Calcula brillo, contraste, textura, y la paleta de colores.
- `mostrar_resultados(...)`: Muestra las características analizadas de las imágenes.
- `generar_prompt_stable_diffusion(...)`: Genera el prompt para Stable Diffusion.

Ejemplo de Prompt Generado
```bash
Generá una imagen de una hamburguesa con las siguientes características:
- Brillo promedio: 128.54 (Neutral)
- Contraste: 12.34 (Ligeramente deseable)
- Textura medida: 2345.67 (Deseable)

Paleta de colores dominantes:
- Color RGB (255, 0, 0) con proporción: 40.23%
- Color RGB (0, 255, 0) con proporción: 30.15%
- Color RGB (0, 0, 255) con proporción: 29.62%

La imagen debe ser vívida, detallada y atractiva.
