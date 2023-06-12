# 14. Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no
# se puede convertir el número a cadena.

def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        ultimo_digito = numero % 10
        numero //= 10
        return ultimo_digito + suma_digitos(numero)


numero = int(input('Ingrese un numero entero: '))
suma = suma_digitos(numero)
print(f"La suma de los dígitos del número {numero} es: {suma}")

