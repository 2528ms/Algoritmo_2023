# Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de naci-
# miento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos
# tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
# siguientes consignas:
# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
# b. realizar un barrido inorden del árbol por nombre y ranking;
# c. realizar un barrido por nivel de los árboles por ranking y especie;
# d. mostrar toda la información de Yoda y Luke Skywalker;
# e. mostrar todos los Jedi con ranking “Jedi Master”;
# f. listar todos los Jedi que utilizaron sabe de luz color verde;
# g. listar todos los Jedi cuyos maestros están en el archivo;
# h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre

from binaryTree import BinaryTree, get_value_from_file

file_jedi = open('Arbol/TP5/jedis.txt') #Abre Archivo con los datos de los Jedi
read_lines = file_jedi.readlines() # lee el archivo línea por línea y crea una lista donde cada elemento de la lista es una línea del archivo.
file_jedi.close() #Cierra el archivo luego de realizar la lectura

#Punta A - crear tres árboles de acceso a los datos: por nombre, ranking y especie
name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()

#Se cargan los datos a cada arbol
read_lines.pop(0) #Elimina el primera linea que contiene el encabezado del arcchivo
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';') #Para cada línea, se divide la línea en campos con ; como separador y se almacena en la var jedi
    jedi.pop() #Elimina el ultimo campo de cada linea que fue separado por la instruccion anterior
    name_tree.insert_node(jedi[0], index+2)     #index en Python comienza en 0, pero los datos en el archivo estan 
    ranking_tree.insert_node(jedi[1], index+2)  #a partir de la linea 2 (linea 1 contiene el encabezado)
    specie_tree.insert_node(jedi[2], index+2)   #para compensar ese desplazamiento y que las lineas de datos se asocien con la clave correcta de cada arbol se usa el '+2'

print('***Punto B - realizar un barrido inorden del árbol por nombre y ranking***')
print('*** Arbol Nombre ***')
name_tree.inorden()
# print('*** Arbol Ranking ***')
# ranking_tree.inorden()
print()

print('*** Punto C - realizar un barrido por nivel de los árboles por ranking y especie ***')
# print('*** Arbol Ranking ***')
# ranking_tree.by_level()
# print('*** Arbol Especie ***')
# specie_tree.by_level()
# print()

print('*** Punto D - mostrar toda la información de Yoda y Luke Skywalker ***')
# search1 = input('Ingrese nombre primer Jedi a buscar ')
# pos = name_tree.search(search1.swapcase().lower())
# if pos:
#     print(get_value_from_file('jedis.txt', pos.other_values))
# else:
#     print(f'{search1} no esta en la lista')

# search2 = input('Ingrese nombre segundo Jedi a buscar ')
# pos = name_tree.search(search2.swapcase().lower())
# if pos:
#     print(get_value_from_file('jedis.txt', pos.other_values))
# else:
#     print(f'{search2} no esta en la lista')
print()

print('*** Punto E - mostrar todos los Jedi con ranking “Jedi Master” ***')
datos = name_tree.inorden_return()
for dato in datos:
    pos = name_tree.search(dato).other_values
    if get_value_from_file('jedis.txt', pos)[1] == "jedi master":
        print(get_value_from_file('jedis.txt', pos)[0])

print()
print('*** Punto F - listar todos los Jedi que utilizaron sabe de luz color verde ***')
name_tree.inorden_file_lightsaber('jedis.txt', 'green')

print()
print('*** PUNTO G - listar todos los Jedi cuyos maestros están en el archivo ***')
datos = name_tree.inorden_return()
for dato in datos:
    pos = name_tree.search(dato).other_values
    if get_value_from_file('jedis.txt', pos)[3] != '-':
        print(get_value_from_file('jedis.txt', pos)[0])

print()
print('*** PUNTO H mostrar todos los Jedi de especie “Togruta” o “Cerean” ***')
datos = name_tree.inorden_return()
for dato in datos:
    pos = name_tree.search(dato).other_values
    if get_value_from_file('jedis.txt', pos)[2] in ["togruta", "cerean"]:
        print(get_value_from_file('jedis.txt', pos)[0], get_value_from_file('jedis.txt', pos)[2])

print()
print('*** PUNTO I - listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre ***')
print('** Jedis con nombres comenzados con a **')
name_tree.inorden_start_with('a')
print('** Jedis que contienen - en su nombre **')
test = name_tree.search_by_coincidence_2('-')
for index in test:
    print(index)
