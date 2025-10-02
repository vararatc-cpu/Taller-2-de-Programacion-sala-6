import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def abrir_imagen():
    ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
    if ruta:
        img = Image.open(ruta)
        img = img.resize((300, 300))  # ajustar tamaño
        foto = ImageTk.PhotoImage(img)
        etiqueta_imagen.config(image=foto)
        etiqueta_imagen.image = foto

ventana = tk.Tk()
ventana.title("Visor simple de imágenes")

etiqueta_imagen = tk.Label(ventana, text="No hay imagen")
etiqueta_imagen.pack(padx=10, pady=10)

boton = tk.Button(ventana, text="Abrir imagen", command=abrir_imagen)
boton.pack(pady=5)

ventana.mainloop()
