import tkinter as tk
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

# Inicia el bucle principal
ventana.mainloop()

