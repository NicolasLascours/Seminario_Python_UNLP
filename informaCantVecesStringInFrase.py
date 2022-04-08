# Dada una frase y un string ingresados por teclado (en ese orden), e informe la cantidad de
# veces que se encuentra el string en la frase. No distingir entre mayúsculas y minúsculas
import re

frase = input("ingrese una frase :").lower().split()
palabra = input("Ingrese una palabra: ").lower()

print(frase)
print(palabra)

frase_sin_comas = frase
for i in range(len(frase_sin_comas)):
    frase_sin_comas[i] = frase_sin_comas[i].replace(",", "")
    frase_sin_comas[i] = frase_sin_comas[i].replace(".", "")

cant = 0
for elem in frase_sin_comas:
    if palabra == elem:
        cant+= 1

print(f"La cantidad de veces que aparece la palabra {palabra} en la frase: {frase} es igual a {cant} veces")

