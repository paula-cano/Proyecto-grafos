import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from controller.Grafo import Grafo
from model.LoadFiles import Files

grafo = Grafo()

def clear():
    os.system('cls')

def intInput(text):
    while(True):
        variable = input(text)
        try:
            integer = int(variable)
            break
        except ValueError:
            print("El dato ingresado no es un número, ingrese otro: ")
    return integer

# Crea la ventana principal
ventana = tk.Tk()

# Carga la imagen
img = Image.open("C:/Users/Julian/OneDrive/Escritorio/Proyecto-grafos/assets/fondo.jpg")
img = img.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
img = ImageTk.PhotoImage(img)

canvas = tk.Canvas(ventana, width=ventana.winfo_screenwidth(), height=ventana.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=img, anchor="nw")

# Crea el grafo
grafo = Grafo()
grafo.createGrafo()

imagenes_planetas = []
# Obtiene las coordenadas y rutas de los planetas

datos = Files.load_data()
planetas = datos["planetas"]
for planeta in planetas:
    coordenada_x = planeta["coordenadas"]["x"]
    coordenada_y = planeta["coordenadas"]["y"]
    ruta_imagen = planeta["ruta"]

    # Crea una etiqueta y una imagen para mostrar el planeta
    etiqueta = tk.Label(canvas, text=planeta["nombre"], font=("Arial", 16))
    etiqueta.place(x=coordenada_x, y=coordenada_y)
    imagen = ImageTk.PhotoImage(Image.open(ruta_imagen).resize((50, 50)))
    imagenes_planetas.append(imagen)  # Agrega la imagen a la lista

    # Agrega las imágenes al canvas
    for i, planeta in enumerate(planetas):
        coordenada_x = planeta["coordenadas"]["x"]
        coordenada_y = planeta["coordenadas"]["y"]
        if len(imagenes_planetas) >= i + 1:
            imagen = imagenes_planetas[i]  # Obtiene la imagen correspondiente
            canvas.create_image(coordenada_x - 25, coordenada_y + 20, image=imagen, anchor="nw")

ventana.mainloop()

n = "0"
while True:
    print("---------------------------------------------------------")
    print("****************** Sistema Star Wars ********************")
    print("---------------------------------------------------------")
    grafo.showVertices()
    print("---------------------------------------------------------")
    print("1. Hacer un recorrido básico")
    print("2. Mostrar los vertices Fuente")
    print("3. Mostrar los vertices Pozo")
    print("4. Kruskal")
    print("5. Imprimir las entradas de los vertices")
    print("6. Imprimir las salidas de los vertices")
    print("7. Salir del sistema")
    n = input("¿Qué deseas realizar?: ")

    if n == "1":
        print("1. Profundidad")
        print("2. Amplitud")
        option = intInput("¿Qué tipo de recorrido desea realizar?: ")
        if option == 1:
            grafo.recorridoEnProfundidad(input("Nombre del planeta de partida: "))
        elif option == 2:
            grafo.recorridoEnAmplitud(input("Nombre del planeta de partida: "))
        input("Enter para terminar.")
    elif n == "2":
        grafo.verticesFuente()
        input("Enter para terminar.")
    elif n == "3":
        grafo.verticesPozo()
        input("Enter para terminar.")
    elif n == "4":
        print("1. Paula")
        print("2. Julián")
        option = intInput("¿Cuál Kruskal quieres ver?: ")
        if option == 1:
            grafo.kruskal()
        elif option == 2:
           grafo.Kruskal()
        input("Enter para terminar.")
    elif n == "5":
        print(grafo.gradoVerticesEntrada())
        input("Enter para terminar.")
    elif n == "6":
        print(grafo.gradoVerticesSalida())
        input("Enter para terminar.")
    elif n == "7":
        break

    clear()
    print()

