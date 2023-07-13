def consonante(palabra):
    vocales = ('a', 'e', 'i', 'o', 'u')
    consonante = ''.join(letra for letra in palabra if letra.lower() not in vocales)
    return consonante


def validar(caracter):
    # Verificar si es una letra y no un número ni signo especial
    if caracter.isalpha():
        return True
    else:
        return False


while True:
    ingreso = input("Ingrese una palabra: ")

    if all(validar(caracter) for caracter in ingreso):
        break
    else:
        print("Error: La palabra debe contener solo letras.")

lista_de_consonante = consonante(ingreso)

print("Palabra ingresada: " + ingreso)
print("Consonante: " + lista_de_consonante)
