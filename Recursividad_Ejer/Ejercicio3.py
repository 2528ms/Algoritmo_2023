"""
EJERCICIO
Implementar una función para calcular el producto de dos números enteros dados.
"""
 # producto(4,3) =  num1 + producto(4,num2 -1)

def producto(num1,num2):
    if (num1 == 0 or num2 == 0):
        return 0
    else:
       print(num1, num2)
       return num1 + producto(num1, num2-1)


print(producto(3,3))
