def contadorPalabras(vector, palabra, contador=0):
    if not vector:
        return contador
    if vector[0] == palabra:
        contador += 1
    return contadorPalabras(vector[1:], palabra, contador)


vector = ["Datos", "Algoritmos", "Mundo", "Algoritmos", "Algoritmos"]
buscado = "Algoritmos"

cont = contadorPalabras(vector, buscado)
print(f"La palabra '{buscado}' aparece {cont} veces en el vector.")
