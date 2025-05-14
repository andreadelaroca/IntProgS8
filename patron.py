#mostrar en la consola 1, 12, 123, 1234, 12345

for i in range (1,6):
    print(str(i)) #imprimir el valor de i como cadena
    for j in range (1,i+1): #bucle interno, variable j que va de 1 a i+1
        print(str(j), end="") #imprimir el valor de j como cadena
