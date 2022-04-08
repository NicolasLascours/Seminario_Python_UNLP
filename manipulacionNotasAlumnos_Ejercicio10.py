archivo1 = open('eval1.txt', 'r', encoding="utf8")
archivo2 = open('eval2.txt','r', encoding="utf8")
archivo_nombres = open ('nombres_1.txt', 'r', encoding="utf8")

def limpiar_archivos_de_notas(notas, lista_de_notas):
    for elem in notas.readlines():
        lista_de_notas.append(float(elem.replace(",", "").replace("\n", "").strip()))
    return lista_de_notas

def limpiar_archivos_de_nombres(nombres,lista_nueva_de_nombres):
    for nom in nombres.readlines():
        lista_nueva_de_nombres.append (nom.replace(",", "").replace("\n", "").replace("'", "").strip())
    return lista_nueva_de_nombres

lista_nueva_de_nombres= []
suma_notas = []

def limpiar_nombres_notas (nombres, notas1, notas2,lista_nueva_de_nombres, suma_notas):
    lista_nueva_de_notas1= []
    lista_nueva_de_notas2= []
    limpiar_archivos_de_nombres(nombres, lista_nueva_de_nombres)
    limpiar_archivos_de_notas(notas1, lista_nueva_de_notas1)
    limpiar_archivos_de_notas(notas2, lista_nueva_de_notas2)
    for i in range(len(lista_nueva_de_notas1)):
        suma_notas.append(lista_nueva_de_notas1[i] + lista_nueva_de_notas2[i])
    return lista_nueva_de_nombres,suma_notas
    

limpiar_nombres_notas(archivo_nombres,archivo1,archivo2,lista_nueva_de_nombres, suma_notas)
promedio = sum(suma_notas)/len(suma_notas)
print(promedio)
dicc_de_lista = dict(zip(lista_nueva_de_nombres, suma_notas))
print(dicc_de_lista) 

def alumnos_debajo_del_promedio(dicc):
    print ("los alumnos que están por debajo de la nota promedio son: ")
    for key, value in dicc.items():
        if value < promedio:
           print (key)
    

alumnos_debajo_del_promedio(dicc_de_lista)