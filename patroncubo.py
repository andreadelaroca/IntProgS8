#patron que muestre el cubo de 1 hasta el cinco
import math

for i in range (1,6): #bucle externo, variable i que va de 1 a 5 al cubo
    for j in range(1,i+1): #bucle interno, variable j que va de 1 a i+1
       print(str(pow(j,3)), end="") #imprimir el valor de i al cubo como cadena
    print()