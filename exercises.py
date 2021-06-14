lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = [15,14,13,12,11,10,9,8,7,6,5]

lista1.reverse()

def mismos(a, b):
    resultado = []
    for i in range (len(a)):
        for j in range (len(b)):
            #print("ciclo ", i, ",", j)
            if a[i] == b[j]:
                #print("i: ", i, " j: ", j)
                resultado.append(lista1[i])
                print(resultado)
    return resultado

final = mismos(lista1, lista2)
final.sort()
print("El resultado en orden es ", final)