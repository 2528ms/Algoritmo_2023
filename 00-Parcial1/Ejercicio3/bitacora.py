from pilaClass import Pila

mision1 = {"planeta": "Martes", "capturado": "Juan", "costo": 20000}
mision2 = {"planeta": "Tatooine", "capturado": "Han Solo", "costo": 100000}
mision3 = {"planeta": "Bespin", "capturado": "Lando Calrissian", "costo": 50000}
mision4 = {"planeta": "Endor", "capturado": "Leia Organa", "costo": 75000}
misiones = [mision1,mision2,mision3,mision4]

bitacora = Pila()
bitacora_aux = Pila()
creditos = 0
contMision = 0
MisionBuscada = 0

for mision in misiones:
    bitacora.push(mision)

while bitacora.size() > 0:
    value = bitacora.pop()
    bitacora_aux.push(value)
    creditos += value["costo"]

print('*******A. Mostrar los planetas visitados en el orden hizo las misiones *******')
while bitacora_aux.size() > 0:
    value = bitacora_aux.pop()
    print(value["planeta"])
    contMision += 1
    if value["capturado"] == "Han Solo":
        MisionBuscada = contMision

print('*******B. Determinar cuántos créditos galácticos recaudo en total. *******')
print(f'El total recaudado es {creditos}')

print('*******C. Determinar el número de la misión en que capturo a Han Solo y en que planeta *******')
print(f'Han Solo fue capturado en la mision {MisionBuscada} en el planeta {misiones[MisionBuscada-1]["planeta"]}')

