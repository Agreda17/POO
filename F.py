from queue import Queue

def calcular_promedio(cola):
    suma = 0
    contador = 0

    while not cola.empty():
        elemento = cola.get()
        suma += elemento
        contador += 1

    return suma / contador if contador > 0 else 0

def main():
    cola = Queue()

    while True:
        entrada = int(input("Ingrese un número entero (ingrese 0 para Finalizar): "))
        cola.put(entrada)

        if entrada == 0:
            break

    elementos = list(cola.queue)
    print("Numeros ingresados:", elementos)

    promedio = calcular_promedio(cola)
    print("Promedio:", promedio)

if __name__ == '__main__':
    main()
