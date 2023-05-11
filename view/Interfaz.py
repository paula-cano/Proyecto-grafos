import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


# Crea la ventana principal
ventana = tk.Tk()

# Carga la imagen, es extraño que no funcione la ruta relativa ./fondo.jpg
img = Image.open("C:/Users/Julian/OneDrive/Escritorio/Proyecto-grafos/assets/fondo.jpg") 
img = img.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
img = ImageTk.PhotoImage(img)

# Crea el canvas y agrega la imagen de fondo
canvas = tk.Canvas(ventana, width=ventana.winfo_screenwidth(), height=ventana.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=img, anchor="nw")

# Agrega el resto de los widgets a la ventana
# ...
# Cargar la imagen
imagen = Image.open("C:/Users/Julian/OneDrive/Escritorio/Proyecto-grafos/assets/jupiter.png")

# Redimensionar la imagen a un nuevo tamaño
nuevo_tamano = (40, 30)  # Especifica el nuevo tamaño deseado
imagen_redimensionada = imagen.resize(nuevo_tamano, Image.ANTIALIAS)

imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

# Crear un widget Label para mostrar la imagen
label_imagen = Label(ventana, image=imagen_tk)

# Opción 1: Utilizar la función pack()
label_imagen.pack()

# Opción 2: Utilizar la función place() para especificar las coordenadas
label_imagen.place(x=500, y=500)

# Inicia el bucle principal
ventana.mainloop()

