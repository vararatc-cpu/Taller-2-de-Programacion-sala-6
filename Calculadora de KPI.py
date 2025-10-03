import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()
ventana.title("Visor simple de imágenes")
ventana.geometry("400x300")  # ancho x alto en píxeles
ventana.resizable(False, False)  # no se puede agrandar ni achicar
ventana.configure(bg="lightblue")

# --- Creamos un canvas con scrollbar ---
contenedor = tk.Frame(ventana)
contenedor.pack(fill="both", expand=True)

canvas = tk.Canvas(contenedor)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# --- Frame interno donde van los widgets ---
frame_interno = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_interno, anchor="nw")

# --- Importante: actualizar scroll ---
def actualizar_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame_interno.bind("<Configure>", actualizar_scroll)

etiqueta = tk.Label(frame_interno, text="Hola, soy un texto en la ventana", font=("Arial", 12), fg="blue")
etiqueta.pack(pady=20)  # .pack coloca el widget dentro de la ventana

def accion():
    print("Clic en el botón")

boton = tk.Button(frame_interno, text="Presióname", command=accion)
boton.pack(pady=10)

entrada = tk.Entry(frame_interno)
entrada.pack(pady=10)

texto = tk.Text(frame_interno, height=5, width=30)
texto.pack(pady=10)

opcion = tk.BooleanVar()
check = tk.Checkbutton(frame_interno, text="Aceptar términos", variable=opcion)
check.pack(pady=10)

opcion = tk.StringVar(value="Opción 1")

radio1 = tk.Radiobutton(frame_interno, text="Opción 1", variable=opcion, value="Opción 1")
radio2 = tk.Radiobutton(frame_interno, text="Opción 2", variable=opcion, value="Opción 2")

radio1.pack()
radio2.pack()

combo = ttk.Combobox(frame_interno, values=["Python", "Java", "C++"])
combo.pack(pady=10)


barra = ttk.Progressbar(frame_interno, length=200, mode="determinate")
barra["value"] = 50  # porcentaje (0 a 100)
barra.pack(pady=10)

ventana.mainloop()

#hola
