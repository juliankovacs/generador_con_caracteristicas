# Análisis de Imágenes y Generación de Imágenes con Stable Diffusion  

Este proyecto implementa un sistema completo para analizar características visuales de imágenes y generar prompts personalizados para herramientas como Stable Diffusion. Además, incluye la funcionalidad de regenerar imágenes basadas en características seleccionadas por el usuario mediante una interfaz gráfica interactiva.  

## Características del Proyecto  

### 1. Análisis de Imágenes  
- **Cálculo de características visuales**:  
  - Brillo promedio.  
  - Contraste promedio.  
  - Textura medida.  
  - Paleta de colores dominantes (utilizando K-Means).  

- **Comparación de imágenes**:  
  - Determina una imagen ganadora basada en características analizadas.  
  - Almacena un historial de características.  

### 2. Generación de Prompts  
- **Creación de descripciones detalladas** para aplicaciones como Stable Diffusion.  
- **Incorporación de características visuales** y paletas de colores dominantes al prompt.  

### 3. Generación de Imágenes  
- Genera imágenes a partir de dos iniciales, analizando características seleccionadas.  
- Permite la selección interactiva de imágenes mediante una interfaz gráfica simple con PySimpleGUI.  
- Regenera nuevas imágenes basadas en las elecciones del usuario.  

## Requisitos  

Para ejecutar este proyecto, asegúrate de tener instalados los siguientes requisitos:  

- **Python**: Versión 3.8 o superior.  
- **Bibliotecas necesarias**:  

```bash
pip install opencv-python numpy matplotlib sklearn diffusers PySimpleGUI Pillow
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
