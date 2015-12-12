# -*- coding: utf-8 -*-

def merge(left,right):
    i=0
    j=0
    result=[]
    while i<len(left) and j<len(right):
       if left[i]>right[j]:
           result.append(left[i])
           i+=1
       else:
           result.append(right[j])
           j+=1
    result+=left[i:]
    result+=right[j:]
    print result
    return result


def merge_sort(A):
    if len(A)<=1:
        return A
    else:
        right=merge_sort(A[len(A)/2:])
        left=merge_sort(A[:len(A)/2])
        return merge(left,right)

A=[49,38,65,97,76,13,27,49]
merge_sort(A)

