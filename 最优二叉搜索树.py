# -*- coding: utf-8 -*-
import copy

def OPTIMAL_BST():
    p=[0,0.15,0.1,0.05,0.1,0.2]
    q=[0.05,0.1,0.05,0.05,0.05,0.1]

    w=[[0 for i in range(len(q)+1)]for j in range(len(q)+1)]
    for i in  range(len(q)):
        w[i+1][i]=q[i]
    e=copy.deepcopy(w)

    for i in range(1,len(q)+1):
        for j in range(i,len(q)):
            w[i][j]=w[i][j-1]+p[j]+q[j]

    for i in range(1,len(q)):
        e[i][i]=e[i][i-1]+e[i+1][i]+w[i][i]

    for k in range (3,len(q)+1):
        for j in range (1,)

    print(w)
    print(e)

OPTIMAL_BST()
