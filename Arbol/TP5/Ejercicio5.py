# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic 
# Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
# A. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
# que indica si es un héroe o un villano, True y False respectivamente;
# B. listar los villanos ordenados alfabéticamente;
# C. mostrar todos los superhéroes que empiezan con C;
# D. determinar cuántos superhéroes hay el árbol;
# E. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# F. listar los superhéroes ordenados de manera descendente;
# G. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol

from binaryTree import BinaryTree #importamos clase binary Tree

from heroes_ejer5 import lista_heroes # importamos la lista de heroes

arbol = BinaryTree() #instanciamos un Tree

#--Punto A-- Cargamos el arbol con los datos de la lista heroes
for heroe in lista_heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'])

print('#--Punto B-- listar los villanos ordenados alfabéticamente')
#Esta funcion devuelve la lista ordenada alfa de super o villanos segun el valor que se le pase
arbol.inorden_super_or_villano(False)
print()

print('#--Punto C-- mostrar todos los superhéroes que empiezan con C')
#macht comiendo del nombre en el nodo con la cadena que se le pasa
arbol.inorden_start_with('c') 
print()

print('#--Punto D-- determinar cuántos superhéroes hay el árbol')
print('cantidad de superheroes', arbol.contar_heroes())
print()

print('#--Punto E-- Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre')
search = input('ingrese cadena que desea buscar: ')
arbol.search_by_coincidence(search)
print()

print('#--Punto F-- listar los superhéroes ordenados de manera descendente')
arbol.postorden()
print()

print('#--Punto G-- generar un bosque a partir de este árbol, un árbol superhéroes y otro villanos')
Tree_heroes = BinaryTree()
Tree_villanos = BinaryTree()

for hereo in lista_heroes:
    if hereo['heroe']:
        Tree_heroes.insert_node(hereo['name'])
    else:
        Tree_villanos.insert_node(hereo['name'])

print('I. determinar cuántos nodos tiene cada árbol')
print(f'el arbol superherores tiene {Tree_heroes.contar_nodo()} nodos')
print(f'el arbol villanos tiene {Tree_villanos.contar_nodo()} nodos')

print('II. realizar un barrido ordenado alfabéticamente de cada árbol')
print('*** arbol superheroes ***')
Tree_heroes.inorden()
print('*** arbol villanos ***')
Tree_villanos.inorden()

print()


#EJEMPLO DE COMO BUSCAR UN VALOR QUE COINCIDA CON LO GUARDADO EN EL PRIMER DATO DEL NOTO (en value)
# value = input('ingrese el nombre que desea modificar ')
# pos = arbol.search(value)
# if pos:
#     is_hero = pos.other_values
#     arbol.delete_node(value)
#     print('modificar')
#     new_value = input('ingrese en nuevo nombre ')
#     arbol.insert_node(new_value, is_hero)
# else:
#     print('no esta')
# print()
# arbol.inorden()
