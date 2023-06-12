#11 .Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena

# def invertir_NumInt(num):
#     if num // 10 == 0 :
#         return num
#     else:
#         return (num %10) * 10 ** len(str(num//10)) + invertir_NumInt(num %10)

# print(invertir_NumInt(230))

def invertir_numero(numero):
    if numero < 10:
        return numero

    ultimo_digito = numero % 10
    numero //= 10

    longitud = len(str(numero))
    return ultimo_digito * (10 ** longitud) + invertir_numero(numero)

# Ejemplo de uso
numero = int(input('Ingrese un numero entero: '))
numero_invertido = invertir_numero(numero)
print(f"El número original: {numero}")
print(f"El número invertido: {numero_invertido}")
