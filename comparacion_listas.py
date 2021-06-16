# Listas de prueba
lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = [15,14,13,12,11,10,9,8,7,6,5]

# Método para reversar la lista para prueba de orden
lista1.reverse()

# Función que encuentra los elementos en común entre las listas y 
# retorna una nueva lista con estos elementos en orden ascendente
def mismos(a, b):
    # Nueva lista con elementos en común
    resultado = []
    # Ciclo de comparación entre las listas
    for i in range (len(a)):
        for j in range (len(b)):
            # Test funcional
            #print("ciclo ", i, ",", j)
            # Condicional de comparación
            if a[i] == b[j]:
                # Test funcional
                #print("i: ", i, " j: ", j)
                # Adición del elemento en común a la lista final
                resultado.append(lista1[i])
                # Test funcional
                #print(resultado)
    return resultado

# Evalución de la función para lista1 y lista2
final = mismos(lista1, lista2)
# Método de ordenamiento ascendente
final.sort()
# Imprimir resultado
print("El resultado en orden es ", final)

