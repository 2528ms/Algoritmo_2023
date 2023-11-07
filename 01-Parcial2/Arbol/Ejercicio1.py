# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 

from binaryTree import BinaryTree 
from pokemones import lista_pokemones 

#Punto A
name_tree = BinaryTree()
numero_tree = BinaryTree()
tipo_tree = BinaryTree()

for pokemon in lista_pokemones:
    name = pokemon['name']
    numero = pokemon['numero']
    tipo = pokemon['tipos']
    name_tree.insert_node(name, pokemon)
    numero_tree.insert_node(numero, pokemon)
    tipo_tree.insert_node(tipo, pokemon)

#Punto B
numero = int(input('ingrese el numero del pokemon que desea buscar '))
pokemon_encontrado = numero_tree.search_pokemon_num(numero)
if pokemon_encontrado is not None:
    print("Datos del Pokemon encontrado:")
    print(pokemon_encontrado.other_values)
else:
    print("No se encontro ningun Pokemon con el numero", numero)

search= input('ingrese caracteres de los nombres que desea buscar')
name_tree.search_by_coincidence(search)




#Punto C
tipo_tree.inorden_tipo_agua()
print()

# Punto D
print("Listado en orden ascendente por numero:")
numero_tree.inorden()
print()
print("Listado en orden ascendente por nombre:")
name_tree.inorden()
print()
print("Listado por nivel por nombre:")
name_tree.by_level()
print()

#Punto E
pokemon_encontrado = name_tree.search('Jolteon')
if pokemon_encontrado is not None:
    print("Datos del Pokémon Jolteon:")
    for key, value in pokemon_encontrado.other_values.items():
        print(f"{key}: {value}")
else:
    print(f"No se encontró ningún Pokémon con el nombre Jolteon.")

print()
pokemon_encontrado = name_tree.search('Lycanroc')
if pokemon_encontrado is not None:
    print("Datos del Pokémon Lycanroc:")
    for key, value in pokemon_encontrado.other_values.items():
        print(f"{key}: {value}")
else:
    print(f"No se encontró ningún Pokémon con el nombre Lycanroc.")

print()
pokemon_encontrado = name_tree.search('Tyrantrum')
if pokemon_encontrado is not None:
    print("Datos del Pokémon Tyrantrum:")
    for key, value in pokemon_encontrado.other_values.items():
        print(f"{key}: {value}")
else:
    print(f"No se encontró ningún Pokémon con el nombre Tyrantrum.")

print()

#Punto F
tipo = input('ingrese tipo de pokemon que desea buscar ')
total = tipo_tree.contar_tipos(tipo)
print(f'la cantidad de pokemones del tipo {tipo} son {total}')


