"""
EJERCICIO
Implementar una función que calcule la suma de todos los números enteros comprendidos
entre cero y un número entero positivo dado
"""
def SumEntPos(num):
    if (num <= 0):
        return 0
    else:
        return  num + SumEntPos(num-1)

     


print(SumEntPos(5))