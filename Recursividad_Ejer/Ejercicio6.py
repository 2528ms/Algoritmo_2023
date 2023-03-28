"""
Dada una secuencia de caracteres, obtener dicha secuencia invertida.
"""

def invertirCadena(input):
    if len(input) == 0:
        return ' '
    else:
        return input[-1] + invertirCadena(input[:-1])
    

print(invertirCadena('hola'))