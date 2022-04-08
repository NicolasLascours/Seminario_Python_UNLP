from collections import Counter

palabra = input("Ingrese una palabra: ")

copia_palabra = palabra
copia_palabra = ''.join(copia_palabra.split(' '))
copia_palabra = ''.join(copia_palabra.split('-'))

if (Counter(copia_palabra).most_common()[0][1]) > 1:
    print(f"La palabra ingresada: '{palabra}' no es heterónoma")
else:
    print(f"La palabra ingresada: '{palabra}' es heterónoma")


#match palabra:
 #   case palabra if (palabra[i] in palabra) > 1: print(f"La palabra ingresada: '{palabra}' no es heterónoma")
 #   case _: print(f"La palabra ingresada: '{palabra}' es heterónoma")