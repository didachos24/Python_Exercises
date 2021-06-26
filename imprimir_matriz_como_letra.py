# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 22:16:44 2021

@author: didachos24
"""

import numpy as np

def crear_matriz():
    n = int(input("Ingrese el tamaño de la raiz cuadrada: "))
    matriz =  np.random.randint(1,9,size = (n,n))
    return matriz
    
class imprimir():
    
    def __init__(self, matriz, impresion):
        self.matriz = matriz
        self.impresion = impresion
        
    def letra_c(self):
        for i in range(n):
            for j in range(n):
                if i == 0:
                    print(self.matriz[i,j])
                elif i > 0 and i < n:
                    print(self.matiz[0,j])
                else:
                    print(self.matriz[n.j])