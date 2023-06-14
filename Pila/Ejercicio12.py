#12.Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
#que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.

from pilaClass import Pila

stack_personajes = Pila()
stack_aux = Pila()

personajes = ['Boba Fett','Conde Dooku','Darth Vader','Leia Organa','Yoda','Obi Wan Kenobi','Luke Skywalker']
busqueda1 = 'Boba Fett'
busqueda2 = 'Leia Organa'

print('******************Stack inicial*********************************')
for x in range(len(personajes)):
    stack_personajes.push(personajes[x])
    print(personajes[x])


print('**********************Stack Aux*****************************')
while stack_personajes.size() > 0:
    valor = stack_personajes.pop()
    if valor == busqueda1:
        print(f'El personaje {busqueda1} se encuentra en la pila')
    stack_aux.push(valor)
    print(valor)


print('*********************Stack final******************************')
while stack_aux.size() > 0:
    valor = stack_aux.pop()
    if valor == busqueda2:
        print(f'El personaje {busqueda2} se encuentra en la pila')
    stack_personajes.push(valor)
    print(valor)
