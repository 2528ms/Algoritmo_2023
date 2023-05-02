#creamos un diccionario con la conversion 
dic = {'I': 1, 'V': 5,'X': 10,'L': 50,'C':100,'D':500,'M': 1000}
num_romano = input('Ingrese numero romano que desea convertir ').upper() #Metodo upper() convierte un string a mayusculas

def verificar_input(num_romano):
    #Verificar si todas las letras ingresadas son validas
    for num in num_romano:
        if not num in dic.keys():
            return False 
    #No se pueden repetir mas de 3 letras iguales seguidas"
    for num in num_romano:
        if  num * 4 in num_romano:
            return False
    #Verificacion de reglas
    for num in range(len(num_romano)-1):
        letra_actual = num_romano[num]
        letra_siguiente = num_romano[num+1]
        if letra_actual == letra_siguiente:
            if letra_actual in {"V", "L", "D"}: #Las letras D, L, V no se pueden repetir para sumar. Ni se pueden usar para restar
                return False
        elif letra_actual == "I" and letra_siguiente not in {"V", "X"}: #La letra I solo puede convinarse con las letras 'V' y 'X
            return False
    


def convert_romano_to_dec(num_romano):
    if verificar_input(num_romano) != False:
        if len(num_romano) == 1:
            return dic[num_romano]
        else:
            if dic[num_romano[0]] >= dic[num_romano[1]]:
                return  dic[num_romano[0]] + convert_romano_to_dec(num_romano[1:])  #permite extraer una serie de elementos del iterable, comenzando por el numerado como inicio y terminando por el numerado como fin-1, aumentando de paso.
            else:
                return  - dic[num_romano[0]] + convert_romano_to_dec(num_romano[1:]) #slice[start: end: step]
    else:
        return "Error al validar el numero"


print(convert_romano_to_dec(num_romano))

"""
#TESTING
tests = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "XIV", "CXC", "MIM","MCMXCVII", "XLVII", "XCII", "CXXXVI", "CDLXXI", "MDCCCLII", "DCCXXVIII", "XCIX", "CCLIX", "CMXXXVIII", "CDLXXVII", "CXII"]
#tests = ["DDCMXCVII", "XLVII", "VVCII", "CXXXVI", "CCDLXXI", "MDCCCLII", "DCCXXVIII", "XCIX", "CCLIX", "CMXXXXVIII", "CDLXXVII", "CVVII"]
for test in tests:
    print(test, convert_romano_to_dec(test))
"""
