# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 11:56:46 2021

@author: didachos24
"""

import numpy as np
from math import sqrt

# Este programa genera una matriz cuadrada al azar del tamaño dado por el usuario
# y busca los elementos que son cuadrados perfectos, los va contando y almacena en una
# lista para retornarlos al final

# Esta rutina genera la matriz al azar del tamaño dado por el usuario
def crear_matriz():
    
    # Pregunta el tamaño de la matriz cuadrada al usuario
    n = int(input("Ingresa número para generar matriz: "))
    # Se genera la matriz con número al azar del 1 al 99 con método de numpy
    matriz = np.random.randint(1,99,size=(n,n))
    return matriz

def solucion():
    
    # Se llama a la función que genera la matriz
    matriz = crear_matriz()
    # Imprime la matriz para control de los elementos
    print(matriz)
    
    # Contador que acumula los elementos cuadrados perfectos en la matriz
    n_cuadrados_perfectos = 0
    # Lista que almacenará los elementos cuadrados perfectos en la matriz
    cuadrados_perfectos = []
    
    # Rutina que recorre la matriz para verificar condicion
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            
            # Condicional de comparación que verifica si el elemento que se analiza 
            # es cuadrado perfecto
            if int(sqrt(matriz[i,j]))**2 == matriz[i,j] :
                # Se suma uno en el contador de los elementos que cumplen condición
                n_cuadrados_perfectos += 1
                # Se agrega el elemento que cumple condición a la lista final
                cuadrados_perfectos.append(matriz[i,j])
    
    # Si no hay cuadrados perfectos en la matriz imprime mensaje dejando saber que 
    # no se puede esperar resultado y arrojará un error
    if len(cuadrados_perfectos) == 0:
        return print("\n \n====> No hay cuadrados perfectos en la matriz \n====> Esperar error \n \n")
    else:
        return n_cuadrados_perfectos, cuadrados_perfectos

# Llamado de la función solución
resultado = solucion()

# Imprime los resultados
print(resultado[0], resultado[1])