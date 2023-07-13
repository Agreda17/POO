lista = []
loop = True

while loop:
    try:
        numero = int(input("Ingrese un número o (presiona 0 para finalizar): "))

        if numero == 0:
            loop = False
            if len(lista) == 0:
                print("La pila está vacía.")
            else:
                promedio = sum(lista) / len(lista)
                print("Lista actual:", lista)
                print("El promedio es:", promedio)
                lista.clear()
        else:
            lista.insert(0, numero)
    except ValueError:
        print("Error: Ingrese solo números enteros.")

if len(lista) == 0:
    print("La pila ahora está vacía: ", lista)
else:
    print("La pila final:", lista)
    lista.clear()
    print("La pila ahora está vacía: ", lista)
