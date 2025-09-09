# Programa para calcular el puntaje final de postulantes en una encuesta

def calcular_puntaje(respuestas_correctas, respuestas_incorrectas, respuestas_blanco):
    return respuestas_correctas * 3 + respuestas_incorrectas * -1 + respuestas_blanco * 0

num_postulantes = int(input("Ingrese el número de postulantes: "))

for i in range(num_postulantes):
    print(f"\nPostulante {i+1}:")
    correctas = int(input("Cantidad de respuestas correctas: "))
    incorrectas = int(input("Cantidad de respuestas incorrectas: "))
    blanco = int(input("Cantidad de respuestas en blanco: "))
    puntaje = calcular_puntaje(correctas, incorrectas, blanco)
    print(f"Puntaje final: {puntaje}")