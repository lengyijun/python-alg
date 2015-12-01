# -*- coding: utf-8 -*-
__author__ = 'jaundice'

# 维持最大堆的性质
def max_heapify(A,i):
    largest=i
    if 2*i<len(A) and A[i]<A[2*i]:
       largest=2*i
    if 2*i+1<len(A) and A[largest]<A[2*i+1]:
        largest=2*i+1
    if largest!=i:
        temp=A[i]
        A[i]=A[largest]
        A[largest]=temp
        max_heapify(A,largest)

# 建立最大堆
def build_max_heap(A):
    for i in range (len(A)-1,0,-1):
        max_heapify(A,i)
    return A
    # print(A)

def heapsort(A):
    print A
    A=build_max_heap(A)
    print(A)
    ss=[]
    for i in range (len(A)-1,0,-1):
        temp=A[1]
        A[1]=A[-1]
        A[-1]=temp

        ss.append(A[-1])
        A.pop(-1)
        max_heapify(A,1)
    print ss


# 用于维持最大堆性质的测试
def test_max_heapify():
    A=[0,16,4,10,14,7,9,3,2,8,1]
    print(A)
    max_heapify(A,2)
    print(A)

# 建立最大堆的测试
def test_build_max_heap():
    A=[0,4,1,3,2,16,9,10,14,8,7]
    print A
    build_max_heap(A)

def test_heap_sort():
    A=[0,4,1,3,2,16,9,10,14,8,100,7]
    heapsort(A)

test_heap_sort()
