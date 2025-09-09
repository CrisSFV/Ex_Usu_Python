# Promedio.py
# Programa que solicita tres notas parciales y calcula el promedio

nota1 = float(input("Ingrese la primera nota parcial: "))
nota2 = float(input("Ingrese la segunda nota parcial: "))
nota3 = float(input("Ingrese la tercera nota parcial: "))

# Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3

# Mostrar el resultado
print(f"El promedio de las tres notas parciales es: {promedio:.2f}")