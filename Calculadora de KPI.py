import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


ventana = tk.Tk()
ventana.title("Visor simple de imágenes")
ventana.geometry("400x300")  # ancho x alto en píxeles
ventana.resizable(False, False)  # no se puede agrandar ni achicar
ventana.configure(bg="lightblue")

etiqueta = tk.Label(ventana, text="Hola, soy un texto en la ventana", font=("Arial", 12), fg="blue")
etiqueta.pack(pady=20)  # .pack coloca el widget dentro de la ventana

ventana.mainloop()