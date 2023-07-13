def validar(caracter):
    if caracter.isalpha():
        return True
    else:
        return False


def ingresar_frase():
    while True:
        frase = input("Ingrese una frase: ")
        if all(validar(caracter) for caracter in frase):
            return frase
        else:
            print("Error: La frase debe contener solo letras.")


primera_frase = ingresar_frase()
segunda_frase = ingresar_frase()

while len(primera_frase) != len(segunda_frase):
    print("Error: Las frases deben tener la misma cantidad.")
    primera_frase = ingresar_frase()
    segunda_frase = ingresar_frase()

combinacion = ""
for i in range(len(primera_frase)):
    combinacion += primera_frase[i]
    combinacion += segunda_frase[i]

print("Primera frase: " + primera_frase)
print("Segunda frase: " + segunda_frase)
print("Combinación: " + combinacion)
