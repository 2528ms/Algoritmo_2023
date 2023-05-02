"""
Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena
"""


def invertir_NumInt(num):
    if num // 10 == 0 :
        return num
    else:
        return (num %10) * 10 ** len(str(num//10)) + invertir_NumInt(num %10)

print(invertir_NumInt(568))


