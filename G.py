from queue import Queue

def contar_vocales_consonantes(cola):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador_vocales = 0
    contador_consonantes = 0

    while not cola.empty():
        elemento = cola.get()
        if elemento.isalpha():
            if elemento.lower() in vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1

    return contador_vocales, contador_consonantes

def main():
    cola = Queue()

    while True:
        entrada = input("Ingrese una letra (o un número para terminar): ")
        if entrada.isalpha():
            cola.put(entrada)
        elif entrada.isdigit():
            break
        else:
            print("Entrada inválida. Intente nuevamente.")

    elementos = list(cola.queue)
    print("Elementos ingresados:", elementos)

    contador_vocales, contador_consonantes = contar_vocales_consonantes(cola)
    print("Cantidad de vocales:", contador_vocales)
    print("Cantidad de consonantes:", contador_consonantes)

if __name__ == '__main__':
    main()
