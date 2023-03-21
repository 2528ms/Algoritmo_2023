#! para utilizar un modulo (libreria) lo primero que hay que hacer es importala

from math import sqrt #!Como ejemplo para no importar todo el modulo math con todas sus funciones, solo importamos la funcion sqrt

print(sqrt(9)) #! al importar solo la funcion no necesitamos llamar al modulo math.sqrt

import Introduccion_Python.mi_modulo as sumResMult #!Importa todo el modulo, si el nombre es largo o solo deseamos le podemos asignar un alias a nuestro modulo

print(sumResMult.suma(3,8))

