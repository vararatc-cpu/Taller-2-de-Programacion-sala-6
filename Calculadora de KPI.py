# Programa para promediar 9 notas de un estudiante

notas = []  # lista vacía para guardar las notas

# Pedir las 9 notas
for i in range(1, 10):
    nota = float(input(f"Ingrese la nota {i}: "))
    notas.append(nota)

# Calcular el promedio
promedio = sum(notas) / len(notas)

# Mostrar resultado
print("\nNotas ingresadas:", notas)
print("Promedio del estudiante:", round(promedio, 2))
