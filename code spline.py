# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:32:12 2024

@author: pierr
"""
import numpy as np
x=[]
y=[]
n = 6
mat = np.zeros((n-1,n-1))
for i in range (n-1) :
    for j in range(n-1):
        if i==j :
            mat[i][j]=4
        elif i ==j+1 or j ==i+1:
            mat[i][j]=1
            
mat