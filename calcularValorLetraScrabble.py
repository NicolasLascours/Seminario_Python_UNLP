palabra = input("Ingrese una palabra: ").upper()

cuenta = 0
for carac in palabra:
    if  carac in ['A' , 'E' , 'I', 'O' , 'U' , 'L' , 'N' , 'R', 'S', 'T']:
         cuenta += 1
    elif carac in ['D' , 'G']:
         cuenta += 2
    elif carac in ['B' , 'C' , 'M' , 'P']:
         cuenta += 3
    elif carac in ['F' , 'H' , 'V' , 'W' , 'Y']:
         cuenta += 4
    elif carac in ['K']:
         cuenta += 5
    elif carac in ['J' , 'X']:
         cuenta += 8
    elif carac in ['D' , 'G']:
          cuenta += 10
    else: 
          pass

print (f"el valor de {palabra} es: ", cuenta)