# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;


from Criaturas import criaturas_lista as criaturas
from binaryTree import BinaryTree
from random import randint

arbol = BinaryTree() #instanciamos un Tree

#--Punto A -- Cargamos el arbol con los datos de la lista 
for criatura in criaturas:
    arbol.insert_node(criatura['name'], [criatura['descripcion'],criatura['derrotadoPorHeroe']])

print('PUNTO A - Listado inorden de las criaturas y quienes la derrotaron')
print()
criaturas_inorden = arbol.inorden_return()
for index in criaturas_inorden:
    dato = arbol.search(index)
    print(f'{dato.value}, derrotado por {dato.other_values[1]}')

print()
print('PUNTO B - se debe permitir cargar una breve descripción sobre cada criatura')
buscado = input('Ingrese nombre de la criatura para cargar descripcion: ')
nodo_encontrado = arbol.search(buscado)

if nodo_encontrado:
    print(f'** Datos acutales ** {nodo_encontrado.value} - {nodo_encontrado.other_values[0]} - {nodo_encontrado.other_values[1]}')
    # Eliminar el nodo existente para actualizar la información
    arbol.delete_node(buscado)
    nueva_descripcion = input('Ingrese la nueva descripción para {}: '.format(buscado))
    # Insertar el nodo actualizado en el árbol
    arbol.insert_node(buscado, [nueva_descripcion, nodo_encontrado.other_values[1]])
    for criatura in criaturas:
        if criatura['name'] == buscado:
            criatura['description'] = nueva_descripcion
    nuevo_nodo = arbol.search(buscado)
    print(f'** Datos modificados ** {nuevo_nodo.value} - {nuevo_nodo.other_values[0]} - {nuevo_nodo.other_values[1]}')
else:
    print('La criatura "{}" no se encuentra en el árbol.'.format(buscado))

print()
print('PUNTO C - mostrar toda la información de la criatura Talos;')
datos = arbol.search('Talos')
print(f'Criatura {datos.value} ; descripcion {datos.other_values[0]} ; derrotado por {datos.other_values[1]}')

print()
print('PUNTO D - determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;')

def contar_in_lista(lista):
    frecuencia = {} 
    for elemento in lista:
        if elemento is not None:
            frecuencia[elemento] = frecuencia.get(elemento, 0) + 1

    return frecuencia

lista = []
criaturas_inorden = arbol.inorden_return()
for index in criaturas_inorden:
    dato = arbol.search(index)
    lista.append(dato.other_values[1])


ranking_heroes = contar_in_lista(lista)
print(ranking_heroes)
ordenado = sorted(ranking_heroes.items(), key=lambda x: x[1], reverse=True)
print(f'Top 1 - {ordenado[0][0]} con {ordenado[0][1]} derrotas')
print(f'Top 2 - {ordenado[1][0]} con {ordenado[1][1]} derrotas')
print(f'Top 3 - {ordenado[2][0]} con {ordenado[2][1]} derrotas')

print()
print('PUNTO E - listar las criaturas derrotadas por Heracles;')
criaturas_inorden = arbol.inorden_return()
for index in criaturas_inorden:
    dato = arbol.search(index)
    if dato.other_values[1] == 'Heracles':
        print(f'{dato.value}, derrotado por {dato.other_values[1]}')

print()
print('PUNTO F - listar las criaturas que no han sido derrotadas;')
criaturas_inorden = arbol.inorden_return()
for index in criaturas_inorden:
    dato = arbol.search(index)
    if dato.other_values[1] == None:
        print(f'La criatura {dato.value} no ha sido derrotada')

print()
print('PUNTO G -además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;')

for criatura in criaturas:
    nuevocampo = {'capturadoPor': ''}
    arbol.delete_node(criatura['name'])
    arbol.insert_node(criatura['name'], [criatura['descripcion'],criatura['derrotadoPorHeroe'],nuevocampo['capturadoPor']])



print()
print('PUNTO H - h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;')
modificar = ['Cerbero', 'Toro de Creta', 'Jabalí de Erimanto', 'Cierva Cerinea']
datos = []
for index in modificar:
    datos.append(arbol.search(index))
    arbol.delete_node(index)

for index in datos:
    index.other_values[1] = "Heracles"
    arbol.insert_node(index.value,[index.other_values[0], index.other_values[1]])
    print(index.value, index.other_values[0], index.other_values[1])

print()
print('Punto I - se debe permitir búsquedas por coincidencia;')
buscar = input('Ingrese caracters para buscar nodo de criaturas ')
resultados = arbol.search_by_coincidence(buscar)

if not resultados:
    print('No se pudo encontrar ninguna coincidencia')
else:
    print('Coincidencias encontradas:')
    for resultado in resultados:
        print(resultado)

print()
print('PUNTO J - eliminar al Basilisco y a las Sirenas;')
eliminados = ['Basilisco','Sirenas']
for eliminar in eliminados:
    arbol.delete_node(eliminar)
    if arbol.search(eliminar) is None:
        print(f'La criatura {eliminar} se elimino correctamente')

print()
print('PUNTO K - modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias')
datos = arbol.search('Aves del Estínfalo')
print('DATOS ACTUALES')
print(f'{datos.value} ;{datos.other_values[0]} ; {datos.other_values[1]}' )
arbol.delete_node('Aves del Estínfalo')
datos.other_values[1] = "Heracles derroto varias"
arbol.insert_node(datos.value,[datos.other_values[0], datos.other_values[1]])

modificado = arbol.search('Aves del Estínfalo')
if modificado is not None:
    print('DATOS MODIFICADOS')
    print(f'{modificado.value} ; {modificado.other_values[0]} ; {modificado.other_values[1]}')
else:
    print('El nodo no fue encontrado en el árbol.')


print()
print('PUNTO L - modifique el nombre de la criatura Ladón por Dragón Ladón;')
datos = arbol.search('Ladón')
print('DATOS ACTUALES')
print(f'{datos.value} ; {datos.other_values[0]} ; {datos.other_values[1]}' )
arbol.delete_node('Ladón')
arbol.insert_node("Dragón Ladón",[datos.other_values[0], datos.other_values[1]])
modificado = arbol.search('Dragón Ladón')
print('DATOS MODIFICADOS')
print(f'{modificado.value} ; {modificado.other_values[0]} ; {modificado.other_values[1]}' )

print()
print('PUNTO M - realizar un listado por nivel del árbol;')
arbol.by_level()

