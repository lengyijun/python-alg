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

def heap_increase_key(A,i,key):
    if key<=A[i]:
        print("key<=A[i]")
        return
    else:
        A[i]=key
        while i>1 and A[i/2]<key:
            A[i],A[i/2]=A[i/2],A[i]
            i=i/2
        return A

def max_heap_insert(A,key):
    A.append(float("-inf"))
    A=heap_increase_key(A,len(A)-1,key)
    return A

def build_max_heap_with_insert(A):
    B=[A[0]]
    for i in range(1,len(A)-1):
        max_heap_insert(B,A[i])
    return B

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

def test_heap_increase_key():
     A=[0,100, 16, 14, 10, 9, 8, 7, 4, 3, 2, 1]#A是排好序的数组
     print(heap_increase_key(A,11,1000))

def test_max_heap_insert():
    A=[0,100, 16, 14, 10, 9, 8, 7, 4, 3, 2, 1]#A是排好序的数组
    print(len(A))
    print(max_heap_insert(A,1000))
    print(len(A))

def test_build_man_heap_with_insert():
    A=[0,4,1,3,2,16,9,10,14,8,7]
    print(build_max_heap_with_insert(A))

# test_heap_sort()
# test_heap_increase_key()
# test_max_heap_insert()
test_build_man_heap_with_insert()