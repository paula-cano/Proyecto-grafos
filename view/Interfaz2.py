import tkinter as tk
from tkinter import *
import canvas as canvas
from PIL import ImageTk, Image

from controller.Grafo import Grafo
from model.LoadFiles import Files

# Crea la ventana principal
ventana = tk.Tk()

# Carga la imagen, es extraño que no funcione la ruta relativa ./fondo.jpg
img = Image.open("C:/Users/sam/PycharmProjects/Proyecto-grafos/assets/fondo.jpg")
img = img.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
img = ImageTk.PhotoImage(img)

canvas = tk.Canvas(ventana, width=ventana.winfo_screenwidth(), height=ventana.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=img, anchor="nw")

# Crea el grafo
grafo = Grafo()
grafo.createGrafo()

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
    canvas.create_image(coordenada_x - 25, coordenada_y + 20, image=imagen, anchor="nw")


ventana.mainloop()