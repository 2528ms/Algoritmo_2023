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

p1 = Pokemon('pikachu', 'electrico', randint(1, 20),'volador')
p2 = Pokemon('vaporeon', 'agua', randint(1, 20),'volador')
p3 = Pokemon('jolteon', 'electrico', randint(1, 20),'planta')
p4 = Pokemon('leafeon', 'planta', randint(1, 20),'volador')
p5 = Pokemon('flareon', 'fuego', randint(1, 20),'planta')
p6 = Pokemon('Tyrantrum', 'fuego', randint(1, 20),'planta')
p7 = Pokemon('Terrakion', 'planta', randint(1, 20),'volador')
p8 = Pokemon('Wingull', 'electrico', randint(1, 20),'volador')

pokemons = [p1, p2, p3, p4, p5, p6, p7, p8]

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

print()
#Punto C, el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
pos_mayor = 0

for pos in range(1, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.ct_ganados > mayor_cantidad:
        pos_mayor = pos
        mayor_cantidad = entrenador.ct_ganados

valor = lista_entrenadores.get_element_by_index(pos_mayor)
entrenador, sublista = valor[0], valor[1]

if sublista.size() > 0:
    pokemon_mayor = sublista.get_element_by_index(0)
    for pos in range(1, sublista.size()):
        pokemon = sublista.get_element_by_index(pos)
        if pokemon.nivel > pokemon_mayor.nivel:
            pokemon_mayor = pokemon

print('***** Punto C ****')
print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} con nivel {pokemon_mayor.nivel} ')

print()
# d. mostrar todos los datos de un entrenador y sus Pokémos;
print('*** Punto D, mostrar todos los datos de un entrenador y sus Pokémos***')
pos = randint(0, lista_entrenadores.size()-1) #Obtenermos una posicion alazar

valor = lista_entrenadores.get_element_by_index(pos) #buscamos los datos del entrenador e imprimimos los datos
entrenador, pokemones= valor[0], valor[1]
print(f'{entrenador.nombre} - CT_ Ganados {entrenador.ct_ganados} - CB_Pedidas {entrenador.cb_perdidas} -  CB_Ganadas {entrenador.cb_ganadas}')

print('Pokemones:')       #Para poder acceder a los datos de la sub-lista hay que obtener cada  
if pokemones.size() > 0:  #dato de cada posicion de ella
    pokemon = pokemones.get_element_by_index(0)
    for pos in range(1, pokemones.size()):
        pokemon = pokemones.get_element_by_index(pos)
        print(pokemon.nombre)
print()
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print('*** Punto E, entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %***')
cant_entrendores = 0
for i in range(0,lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(i)
    porcen_ganadas = (entrenador[0].cb_ganadas * 100 / (entrenador[0].cb_ganadas + entrenador[0].cb_perdidas)) 
    if porcen_ganadas >= 79:
        print(f'{entrenador[0].nombre} porcentaje {porcen_ganadas} %')
        cant_entrendores = cant_entrendores + 1

if (cant_entrendores == 0 ):
    print('No hay entrenadores con porcentaje mayor o igual a 79%')

print()
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
print('****Entrenadores con pokemones de tipo fuego/planta o agua/volador****')
for i in range(0,lista_entrenadores.size()):
    valor = lista_entrenadores.get_element_by_index(i)
    entrenador, pokemones = valor[0],valor[1]
    
    for pos in range(0, pokemones.size()):
        pokemon = pokemones.get_element_by_index(pos)
        if ((pokemon.tipo == 'fuego' and pokemon.subtipo == 'planta') or 
            (pokemon.tipo == 'agua' and pokemon.subtipo == 'volador')):
            print(f'Entrenador: {entrenador.nombre} - pokemon: {pokemon.nombre}')

print()
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
print('***promedio de nivel de los Pokémons de un determinado entrenador***')
num_entrenador = randint(0,lista_entrenadores.size()-1)
valor = lista_entrenadores.get_element_by_index(num_entrenador)
entrenador, pokemones = valor[0],valor[1]
total_nivel = 0
for pos in range(0, pokemones.size()):
        pokemon = pokemones.get_element_by_index(pos)
        total_nivel = total_nivel + pokemon.nivel
if (pokemones.size()>0):
    nivel_promedio = total_nivel/pokemones.size()
else:
    nivel_promedio = 0
print(f'El entrenador {entrenador.nombre} tiene un nivel promedio de {nivel_promedio} entre sus pokemones')

print()
# j.determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
print('***Entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull***')
for i in range(0,lista_entrenadores.size()-1):
    valor = lista_entrenadores.get_element_by_index(i)
    entrenador, pokemones = valor[0],valor[1]
    
    for pos in range(0, pokemones.size()):
        pokemon = pokemones.get_element_by_index(pos)
        if (pokemon.nombre == "Tyrantrum" or pokemon.nombre ==  "Terrakion" or pokemon.nombre ==  "Wingull"):
        #if pokemon.nombre is ["Tyrantrum","Terrakion","Wingull"]:
            print(f'El entrenador {entrenador.nombre} tiene al pokemon {pokemon.nombre} entre sus pokemones')
print()
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
print('*** Ingrese entrenador y pokemon que desea buscar ***')
print('ingrese entredador')
entrenadorIngresado = input()
print('ingrese pokemon')
pokemonIngresado = input()
pos_entrenador = lista_entrenadores.search(entrenadorIngresado,'nombre')
entrenador = lista_entrenadores.get_element_by_index(pos_entrenador)

pokemones = entrenador[1]
encontrado = False
for i in range(0, pokemones.size()):
    pokemon = pokemones.get_element_by_index(i)
    if(pokemon.nombre == pokemonIngresado):
        print('El entrenador tiene el pokemon ingresado')
        print(f'Datos {entrenador[0].nombre} - CT_ Ganados: {entrenador[0].ct_ganados} - CB_Pedidas: {entrenador[0].cb_perdidas} -  CB_Ganadas: {entrenador[0].cb_ganadas}')
        print(f'Datos {pokemon.nombre } - Tipo: {pokemon.tipo } - Nivel: {pokemon.nivel } -  Subtipo: {pokemon.subtipo }')
        encontrado = True
if (not encontrado):
        print('El entrenador NO tiene el pokemon ingresado')



