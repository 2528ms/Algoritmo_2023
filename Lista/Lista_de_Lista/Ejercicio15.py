# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
# tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

from lista_lista import Lista as ListaDeLista
from random import randint

class Entrenador():

    def __init__(self,nombre, ct_ganados=0, cb_perdidas=0,cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self) -> str:
        return f'{self.nombre} --> torneoGanados:{self.ct_ganados}, batallasGanadas:{self.cb_ganadas}, batallasperdidas:{self.cb_perdidas}'
    
class Pokemon():

    def __init__(self, nombre, tipo, nivel=1, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre}-{self.tipo}-{self.nivel}-{self.subtipo}'


e1 = Entrenador('Juan', ct_ganados=randint(1, 10), cb_perdidas=randint(1, 10),cb_ganadas=randint(1, 10))
e2 = Entrenador('Maria', ct_ganados=randint(1, 10), cb_perdidas=randint(1, 10),cb_ganadas=randint(1, 10))
e3 = Entrenador('Ana', ct_ganados=randint(1, 10), cb_perdidas=randint(1, 10),cb_ganadas=randint(1, 10))

entrenadores = [e1, e2, e3]

lista_entrenadores = ListaDeLista()

p1 = Pokemon('pikachu', 'electrico', randint(1, 20))
p2 = Pokemon('jolteon', 'electrico', randint(1, 20))
p3 = Pokemon('vaporeon', 'agua', randint(1, 20))
p4 = Pokemon('flareon', 'fuego', randint(1, 20))
p5 = Pokemon('leafeon', 'planta', randint(1, 20))

pokemons = [p1, p2, p3, p4, p5]

#! lista principal
for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

#! lista secundaria
for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')


lista_entrenadores.barrido_entrenadores()
print()
#! Punto A
print('****Cantidad de Pokémons de un determinado entrenador****')
pos = lista_entrenadores.search('Juan', 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')

print()
#! Punto B
print('*****Lista entrenadores que hayan ganado más de tres torneos****')
for pos in range(lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.ct_ganados > 3:
        print(entrenador)