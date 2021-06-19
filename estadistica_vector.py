# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 23:13:30 2021

@author: didac
"""

test = [15,14,13,12,11,10,9,8,7,6,5]

def estadisticas(a):
    suma = 0
    moda = []
    for i in range (len(a)):
        suma += a[i]
        
estadisticas(test)