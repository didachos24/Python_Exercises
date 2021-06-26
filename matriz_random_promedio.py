# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 10:21:38 2021

@author: didac
"""

import numpy as np

def promedio_matriz(A):
    fil = A.shape[0] #filas
    col = A.shape[1] #columnas
    suma = 0
    for i in range (fil):
        for j in range (col):
            suma += A[i,j]
    promedio = suma / (fil * col)
    return promedio
            
def cuantos_superiores_promedio(A):
    promedio = promedio_matriz(A)
    cuantos = 0
    for i in range (A.shape[0]):
        for j in range (A.shape[1]):
            if A[i,j] > promedio:
                cuantos += 1
    return cuantos

def cuales_superiores_promedio(A):
    promedio = promedio_matriz(A)
    cuales = []
    for i in range (A.shape[0]):
        for j in range (A.shape[1]):
            if A[i,j] > promedio:
                cuales.append(A[i,j])
    return cuales

def donde_superiores_promedio(A):
    promedio = promedio_matriz(A)
    posiciones = []
    for i in range (A.shape[0]):
        for j in range (A.shape[1]):
            if A[i,j] > promedio:
                posiciones.append((i,j))
    return posiciones

def solucion():
    m = int(input("Ingresar el número de filas: "))
    n = int(input("Ingresar el número de columnas: "))
    mat = np.random.randint(1, 99, size=(m,n))
    num_superiores = cuantos_superiores_promedio(mat)
    print("Matriz: ")
    print(mat)
    print("Promedio: ")
    print(promedio_matriz(mat))
    print("los elementos son: ")
    print(cuantos_superiores_promedio(mat))
    print("Los elementos superiores son: ")
    print(cuales_superiores_promedio(mat))
    print("las pocisiones son: ")
    print(donde_superiores_promedio(mat) )
    
solucion()