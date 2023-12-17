def ordenamiento_insercion_palabras(lista):
    for i in range(1, len(lista)):
        palabra_actual = lista[i]
        j = i - 1
        while j >= 0 and palabra_actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = palabra_actual

# Ejemplo del ejercicio.........................................
        
if __name__ == "__main__":
    palabras_otro_ejemplo = ["python", "java", "ruby", "csharp", "javascript", "typescript"]
    
    print("Lista original:", palabras_otro_ejemplo)
    
    ordenamiento_insercion_palabras(palabras_otro_ejemplo)
    
    print("Lista ordenada:", palabras_otro_ejemplo)

    # El ordenamiento por inserción es un algoritmo utilizado para organizar elementos en 
    # una lista o conjunto de datos. Su propósito principal es ordenar los elementos de 
    # manera ascendente o descendente para facilitar la búsqueda y recuperación eficiente de información.