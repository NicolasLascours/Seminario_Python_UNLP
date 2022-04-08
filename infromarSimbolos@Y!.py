cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no␣ contener los símbolos:@ y !):")

match cadena:
    case cadena if len(cadena) > 10: print("Ingresaste más de 10 carcateres")
    case cadena if "@" in cadena or "!" in cadena: print("Ingresaste alguno de estos símbolos: @ o !" )
    case _: print("Clave válida")





