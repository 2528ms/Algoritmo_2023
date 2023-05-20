import sys #Import library 'sys'
sys.path.append('/home/ms/Algoritmo_2023_MS/Pila') 
import pilaClass #select file that contain of folder added

personajes = [
                {'personaje': 'Iron Man', 'peliculas': 11},
                {'personaje': 'Thor', 'peliculas': 9},
                {'personaje': 'Captain America ', 'peliculas': 8},                
                {'personaje': 'Hulk', 'peliculas': 6},
                {'personaje': 'Rocket Raccoon', 'peliculas': 5},
                {'personaje': 'Black Widow', 'peliculas': 7},
                {'personaje': 'Hawkeye', 'peliculas': 5},
                {'personaje': 'Nick Fury', 'peliculas': 9},
                {'personaje': 'SpiderMan', 'peliculas': 4},
                {'personaje': 'Doctor Strange', 'peliculas': 2},
                {'personaje': 'Groot', 'peliculas': 5},
                {'personaje': 'Black Panther', 'peliculas': 4},
                {'personaje': 'Gamora', 'peliculas': 4},
                {'personaje': 'Drax', 'peliculas': 4}
            ] 

stack = pilaClass.Pila()
stack_Aux = pilaClass.Pila()
stack_cantPelis = pilaClass.Pila()
stack_nombreIni = pilaClass.Pila()

personaje1 = input('ingrese primer personaje que desea buscar ')
personaje2 = input('ingrese segundo personaje que desea buscar ')
personaje3 = 'Black Widow'

posPersonaje1 = 0
posPersonaje2 = 0
posBlackWidow = 0

for i in range(len(personajes)):
    stack.push(personajes[i])

for i in range(1,len(personajes)+1):
    value = stack.pop()
    if value['personaje'] == personaje1:
        posPersonaje1 = i
        stack_Aux.push(value)
    elif value['personaje'] == personaje2:
        posPersonaje2 = i
        stack_Aux.push(value)
    
    if value['personaje'] == personaje3:
        posBlackWidow = i 
        stack_Aux.push(value)
    else:
        stack_Aux.push(value)
    

while stack_Aux.size() > 0:
    value = stack_Aux.pop()
    if value['peliculas'] > 5:
        stack_cantPelis.push(value)
        stack.push(value)
    stack.push(value)
    
while stack.size() > 0:
    value = stack.pop()
    if value['personaje'][0] in ['C','D','G']:
        stack_nombreIni.push(value)


print('**************** Punto A del ejercicio ****************************')
print(f'El personaje "{personaje1}" buscado se encuentra en la posicion {posPersonaje1} de la pila')
print(f'El personaje "{personaje2}" buscado se encuentra en la posicion {posPersonaje2} de la pila')

print('**************** Punto B del ejercicio ****************************')
print('Los personajes que participaron en mas de 5 peliculas de la saga son:')
stackSize1 = stack_cantPelis.size()
for i in range(stackSize1):
    value = stack_cantPelis.pop()
    cant = value['peliculas']
    print(f'#{i} '+value['personaje'] + 'en ' + f'{cant}' +' peliculas'  )
    

print('**************** Punto C del ejercicio ****************************')
if posBlackWidow == 0:
    print('La personaje Black Widow no se encuentra en la pila')
else:
    cant = personajes[len(personajes)-(posBlackWidow)]['peliculas']
    print(f'La personaje Black Widow participo en {cant} peliculas')

print('**************** Punto D del ejercicio ****************************')
print('Los personajes cuyos nombre empiezan con C, D y G son:')
stackSize2 = stack_nombreIni.size()
for i in range(stackSize2):
    value = stack_nombreIni.pop()
    print(f'#{i} '+value['personaje'])
