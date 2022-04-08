# crear matriz
def matriz(filas,columnas,caracter=False):
    tablero = []
    for i in range(0,filas):
        v = [caracter]*columnas
        tablero.append(v)
    return tablero

filas = 4
columnnas = 4

print(matriz(5,4, '_'))