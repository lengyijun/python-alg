# -*- coding: utf-8 -*-

def bubble_sort(A):
    for i in range(len(A)-1,0,-1):
       for j in range(0,i):
           if A[j]>A[j+1]:
               A[j],A[j+1]=A[j+1],A[j]
           #     temp=A[j]
           #     A[j]=A[j+1]
           #     A[j+1]=temp
           # j=j+1
    print(A)

def insert_sort(A):
    ss=[A[0]]
    for item in A:
        pivot=0
        while ss[pivot]<item:
            pivot+=1
        temp=ss[pivot:]#利用PYTHON的特性
        ss[pivot]=item
        ss.extend(temp)
    print(A)


A=[49,38,65,97,76,13,27,50]
bubble_sort(A)