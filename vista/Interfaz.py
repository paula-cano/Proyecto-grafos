import tkinter as tk
from PIL import Image, ImageTk

# Crea una instancia de la ventana principal
root = tk.Tk()

# Carga la imagen usando la biblioteca Pillow
image = Image.open("C:/Users/Julian/OneDrive/Imágenes/Saved Pictures/1b90e7f292b949d90c7a7ab02544fb40.jpg") #coloca aqui la imagen que querias añadir

# Crea una instancia de la clase PhotoImage de la imagen cargada
photo = ImageTk.PhotoImage(image)

# Crea un widget Label y establece la imagen como su contenido
label = tk.Label(root, image=photo)

# Ajusta el tamaño del widget para que se ajuste a la imagen
label.pack()

# Ejecuta el bucle de eventos de la ventana
root.mainloop()
