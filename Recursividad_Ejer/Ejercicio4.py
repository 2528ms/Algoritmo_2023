"""
Implementar una función para calcular la potencia dado dos números enteros, el primero re-
presenta la base y segundo el exponent
"""

#potencia(2,3) = num1 * potencia(num1, num2 - 1 )

def potencia(num1, num2):
    if (num2 == 0):
        return 1
    else:
        print(num1,num2)
        return num1 * potencia(num1, num2-1)
    

print(potencia(5,3))