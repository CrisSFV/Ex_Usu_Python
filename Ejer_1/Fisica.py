def calcular_distancia(velocidad, tiempo):
    """
    Calcula la distancia recorrida en un movimiento rectilíneo uniforme.
    velocidad: en m/s
    tiempo: en s
    retorna: distancia en metros
    """
    return velocidad * tiempo

def main():
    print("Bienvenido al módulo de física.")
    velocidad = float(input("Ingrese la velocidad (m/s): "))
    tiempo = float(input("Ingrese el tiempo (s): "))
    distancia = calcular_distancia(velocidad, tiempo)
    print(f"La distancia recorrida es: {distancia} metros.")

if __name__ == "__main__":
    main()