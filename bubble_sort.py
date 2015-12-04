# -*- coding: utf-8 -*-

def bubble_sort(A):
    for i in range(len(A)-1,0,-1):
       for j in range(0,i):
           if A[j]>A[j+1]:
               temp=A[j]
               A[j]=A[j+1]
               A[j+1]=temp
           j=j+1
    print(A)

A=[49,38,65,97,76,13,27,50]
bubble_sort(A)