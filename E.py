class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def obtener_elementos(self):
        return self.items


def contar_vocales_consonantes(pila):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador_vocales = 0
    contador_consonantes = 0

    for elemento in pila.obtener_elementos():
        if elemento.isalpha():
            if elemento.lower() in vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1

    return contador_vocales, contador_consonantes


def main():
    pila = Pila()

    while True:
        entrada = input("Ingrese una letra (o un número para terminar): ")

        if entrada.isalpha():
            pila.apilar(entrada)
        elif entrada.isdigit():
            break
        else:
            print("Entrada inválida. Intente nuevamente.")

    elementos = pila.obtener_elementos()
    print("Elementos ingresados:", elementos)

    contador_vocales, contador_consonantes = contar_vocales_consonantes(pila)
    print("Cantidad de vocales:", contador_vocales)
    print("Cantidad de consonantes:", contador_consonantes)


if __name__ == '__main__':
    main()

