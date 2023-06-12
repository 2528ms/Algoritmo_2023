#10. Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

def cantDigitos(num):
    if num < 10:
        return 1
    else:
        return 1 + cantDigitos(num // 10) 
    

num = int(input('Ingrese un numero entero: '))
print(f'La cantidad de digitos del numero ingresado es: {cantDigitos(num)}')