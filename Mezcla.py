def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # Dividir la lista en dos partes
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    # Llamadas recursivas para ordenar cada mitad
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)

    # Unir ambas mitades ordenadas
    return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    # Comparar elementos de ambas listas
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Añadir elementos restantes de cada mitad (si hay)
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

# Prueba del algoritmo
if __name__ == "__main__":
    lista = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", lista)
    ordenada = merge_sort(lista)
    print("Lista ordenada:", ordenada)