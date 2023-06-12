def decimal_a_binario(numero):
    if numero <= 0:
        return 0
    else:
        return (numero % 2) + 10 * decimal_a_binario(numero // 2)

# Ejemplo de uso
numero_decimal = int(input('Ingrese un numero entero: '))
numero_binario = decimal_a_binario(numero_decimal)
print(f"El número decimal {numero_decimal} en binario es: {numero_binario}")