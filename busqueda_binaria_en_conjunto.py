def busqueda_binaria(conjunto, elemento):
    izquierda, derecha = 0, len(conjunto) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = conjunto[medio]

        if valor_medio == elemento:
            return True  
        elif valor_medio < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return False 


conjunto_ordenado_otro = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Elemento a buscar
elemento_a_buscar_otro = 16


resultado_otro = busqueda_binaria(conjunto_ordenado_otro, elemento_a_buscar_otro)


if resultado_otro:
    print(f"El elemento {elemento_a_buscar_otro} está en el conjunto.")
else:
    print(f"El elemento {elemento_a_buscar_otro} no está en el conjunto.")

    # La búsqueda binaria en un conjunto, o cualquier lista ordenada, es un algoritmo
    #  eficiente que permite determinar si un elemento específico pertenece o no al conjunto.
    #  Este algoritmo divide repetidamente el conjunto por la mitad y compara el elemento
    #  buscado con el valor en el punto medio, eliminando así la mitad de la búsqueda en cada paso.