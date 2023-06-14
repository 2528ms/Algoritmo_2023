# 22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

class Jedi:
    def __init__(self, nombre, maestros, colores_sable, especie):
        self.nombre = nombre
        self.maestros = maestros
        self.colores_sable = colores_sable
        self.especie = especie
    def __str__(self):
        return f'{self.nombre} - {self.maestros} - {self.colores_sable} - {self.especie }'

# Crear instancias de Jedi
jedi1 = Jedi("Luke Skywalker", ["Obi-Wan Kenobi", "Yoda"], ["azul", "verde"], "Humano")
jedi2 = Jedi("Obi-Wan Kenobi", ["Qui-Gon Jinn"], ["azul"], "Humano")
jedi3 = Jedi("Mace Windu", [], ["morado"], "Humano")
jedi4 = Jedi("Ahsoka Tano", ["Anakin Skywalker"], ["verde", "blanco"], "Togruta")
jedi5 = Jedi("Kit Fisto", ["Anakin Skywalker"], ["azul", "amarrillo", "rojo"], "twi'lek")

# Crear lista de Jedi
jedis= [jedi1, jedi4, jedi2, jedi3, jedi5 ]

from listaClass import Lista
jedi_list = Lista()
#Cargamos todas las instancias de personaje a la lista creada, a medida que lo insertamos en la lista indicamos que los ordene por nombre
for jedi in jedis :
    jedi_list.insert(jedi,"nombre")

# print('********Punto A listado ordenado por nombre y por especie ********')
# print('********listado por nombre********')
# jedi_list.barrido()
# print('********listado por especie********')
# jedi_list.order_by('especie')
# jedi_list.barrido()
# jedi_list.order_by('nombre')

# print('********Punto B mostrar toda la información de Ahsoka Tano y Kit Fisto ********')
# print('información de Ahsoka Tano ->', jedi_list.get_element_by_index(jedi_list.search("Ahsoka Tano","nombre")))
# print('información de Kit Fisto ->', jedi_list.get_element_by_index(jedi_list.search("Kit Fisto","nombre")))

print("********Punto D mostrar los Jedi de especie humana y twi'lek********")
for i in range(0,jedi_list.size()):
    if jedi_list.get_element_by_index(i).especie == "Humano" or jedi_list.get_element_by_index(i).especie == "twi'lek":
        print(jedi_list.get_element_by_index(i).nombre +', '+ jedi_list.get_element_by_index(i).especie)

print("********Punto E listar todos los Jedi que comienzan con A*******")
for i in range(0,jedi_list.size()):
    if jedi_list.get_element_by_index(i).nombre[0] == "A" :
        print(jedi_list.get_element_by_index(i).nombre)

print("********Punto F mostrar los Jedi que usaron sable de luz de más de un color*******")
for i in range(0,jedi_list.size()):
    if len(jedi_list.get_element_by_index(i).colores_sable) > 1 :
        print(jedi_list.get_element_by_index(i).nombre+', sables '+ str(jedi_list.get_element_by_index(i).colores_sable))

print("********Punto G indicar los Jedi que utilizaron sable de luz amarillo o violeta*******")
for i in range(0,jedi_list.size()):
    for j in range(0,len(jedi_list.get_element_by_index(i).colores_sable)):
        jedi_list.get_element_by_index(i).nombre+', sables '+ str(jedi_list.get_element_by_index(i).colores_sable)