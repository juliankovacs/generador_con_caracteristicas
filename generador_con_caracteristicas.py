import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter
import random

# Función para mostrar la imagen original
def mostrar_imagen(img):
    plt.axis('off')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

# Función para extraer la paleta de colores dominantes
def extraer_paleta_de_colores(img, num_clusters=5):
    # Redimensionar la imagen para acelerar el procesamiento (opcional)
    img = cv2.resize(img, (600, 400))

    # Convertir la imagen a un array de píxeles
    img_data = img.reshape((-1, 3))

    # Aplicar K-means
    kmeans = KMeans(n_clusters=num_clusters, n_init=10)
    kmeans.fit(img_data)

    # Obtener los colores dominantes
    colores = kmeans.cluster_centers_.astype(int)
    etiquetas = kmeans.labels_

    # Contar las etiquetas para obtener la frecuencia de cada color
    contador = Counter(etiquetas)
    total_puntos = np.sum(list(contador.values()))

    # Calcular la proporción de cada color y convertirlo a tupla
    proporciones = {tuple(colores[i]): contador[i] / total_puntos for i in contador}
    proporciones = dict(sorted(proporciones.items(), key=lambda item: item[1], reverse=True))

    return proporciones

# Función para visualizar la paleta de colores
def mostrar_paleta(colores_proporcion):
    paleta = np.zeros((50, 300, 3), dtype='uint8')
    start = 0

    for color, prop in colores_proporcion.items():
        end = start + int(prop * paleta.shape[1])
        paleta[:, start:end] = color
        start = end

    plt.axis('off')
    plt.imshow(cv2.cvtColor(paleta, cv2.COLOR_BGR2RGB))
    plt.show()

# Función para cargar imágenes y extraer características
def cargar_y_extraer_caracteristicas(ruta_imagen):
    # Cargar la imagen
    imagen = cv2.imread(ruta_imagen)
    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # Redimensionar la imagen para un tamaño uniforme
    gris = cv2.resize(gris, (100, 100))

    # Extraer características
    brillo = np.mean(gris)
    contraste = gris.std()
    textura = np.sum(cv2.Laplacian(gris, cv2.CV_64F))
    color = np.mean(imagen, axis=(0, 1))

    # Extraer la paleta de colores
    paleta_colores = extraer_paleta_de_colores(imagen)

    # Retornar un vector de características junto a la paleta
    return [brillo, contraste, textura, color[0], color[1], color[2]], paleta_colores

# Variables globales
matriz_historialA = []  # Historial de características de la imagen A
matriz_historialB = []  # Historial de características de la imagen B
imagenes_ganadoras = []  # Lista de imágenes ganadoras

# Cargar características de las imágenes A y B
ruta_imagenA = 'prueba.jpg'
ruta_imagenB = 'prueba2.jpg'

# Extraer características y paleta de colores
A, paleta_A = cargar_y_extraer_caracteristicas(ruta_imagenA)
B, paleta_B = cargar_y_extraer_caracteristicas(ruta_imagenB)

# Agregar los vectores a las matrices de historial
A.append(True)  # Marcar la imagen A como ganadora
B.append(False)  # Marcar la imagen B como perdedora
matriz_historialA.append(A)
matriz_historialB.append(B)

# Determinar cuál imagen es ganadora y agregarla a la lista de ganadoras
if A[5]:  # Si A es ganadora
    imagenes_ganadoras.append(A)
else:
    imagenes_ganadoras.append(B)

# Calcular la cantidad de columnas (características)
columnas = len(imagenes_ganadoras[0]) - 1

# Aplicar variaciones aleatorias a las características de las imágenes ganadoras
numeros_aleatorios = [random.randint(-5, 5) for _ in range(columnas)]

# Clasificación de puntuaciones
clasificacion = {
    -5: "Extremadamente indeseable",
    -4: "Muy indeseable",
    -3: "Indeseable",
    -2: "Poco indeseable",
    -1: "Ligeramente indeseable",
    0: "Neutral",
    1: "Ligeramente deseable",
    2: "Poco deseable",
    3: "Deseable",
    4: "Muy deseable",
    5: "Extremadamente deseable"
}

# Generar la puntuación basada en variaciones aleatorias
puntuacion = [(clasificacion[numeros_aleatorios[col]]) for col in range(columnas)]

# Mostrar los resultados
def mostrar_resultados(caracteristicas_A, caracteristicas_B, ganadora, puntuaciones, paleta_ganadora):
    print("\n--- Resultados de las Características ---")
    print("Características de la imagen A:")
    print(f"- Brillo: {caracteristicas_A[0]:.2f}")
    print(f"- Contraste: {caracteristicas_A[1]:.2f}")
    print(f"- Textura: {caracteristicas_A[2]:.2f}")

    print("\nCaracterísticas de la imagen B:")
    print(f"- Brillo: {caracteristicas_B[0]:.2f}")
    print(f"- Contraste: {caracteristicas_B[1]:.2f}")
    print(f"- Textura: {caracteristicas_B[2]:.2f}")

    print("\nCaracterísticas de la Imagen Ganadora:")
    print(f"- Brillo: {ganadora[0]:.2f} ({puntuaciones[0]})")
    print(f"- Contraste: {ganadora[1]:.2f} ({puntuaciones[1]})")
    print(f"- Textura: {ganadora[2]:.2f} ({puntuaciones[2]})")

# Llamar a la función para mostrar los resultados
mostrar_resultados(A[:-1], B[:-1], imagenes_ganadoras[-1][:-1], puntuacion, paleta_A if A[5] else paleta_B)

# Generar el prompt para Stable Diffusion basado en características
def generar_prompt_stable_diffusion(caracteristicas, puntuaciones, paleta_colores):
    prompt = "Generá una imagen de una hamburguesa con las siguientes características:\n"
    prompt += f"- Brillo promedio: {caracteristicas[0]:.2f} ({puntuaciones[0]})\n"
    prompt += f"- Contraste: {caracteristicas[1]:.2f} ({puntuaciones[1]})\n"
    prompt += f"- Textura medida: {caracteristicas[2]:.2f} ({puntuaciones[2]})\n"
    prompt += "\nPaleta de colores dominantes:\n"
    for color, prop in paleta_colores.items():
        color_rgb = tuple(map(int, color))  # Convertir los valores a enteros
        prompt += f"- Color RGB {color_rgb} con proporción: {prop:.2%}\n"
    
    prompt += "\nLa imagen debe ser vívida, detallada y atractiva."

    return prompt

# Generar y mostrar el prompt
prompt_resultante = generar_prompt_stable_diffusion(imagenes_ganadoras[-1][:-1], puntuacion, paleta_A if A[5] else paleta_B)
print("\nPrompt generado para Stable Diffusion:\n", prompt_resultante)
