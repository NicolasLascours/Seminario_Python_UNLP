cadena = "sopa"
cadena_encriptada = list (map (lambda x: chr(ord(x)+1), cadena))
print(cadena_encriptada)