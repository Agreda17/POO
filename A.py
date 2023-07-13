# secuencia invertida #
def ingresar_caracteres():
    lista = []

    while True:
        caracter = input("Ingrese un caracter (o presiona Enter para finalizar ): ")

        if caracter == "":
            break
        elif len(caracter) == 1:

            lista.append(caracter)
        else:
            print("Error: se permite ingresar un solo caracter.")

    print("Lista ingresada:")
    print(lista)
    lista.reverse()
    print("Secuencia invertida :")
    print(lista)


ingresar_caracteres()