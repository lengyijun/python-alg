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


# http://www.2liang.me/archives/257
def insert_sort_change(A):
    for i in range(1,len(A)):
        j=i-1
        key=A[i]
        while j>=0:
            if A[j]>key:
                A[j+1]=A[j]
                A[j]=key
            j-=1
    print A

def select_sort(A):
    ss=[]
    i=0
    while len(A)!=0 :
        min_num=min(A)
        ss.append(min_num)
        for i in range(0,len(A)):
            if A[i]==min_num:
               A.pop(i)
               break
    print(ss)

A=[49,38,65,97,76,13,27,50]
# bubble_sort(A)
insert_sort_change(A)
