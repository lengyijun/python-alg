# -*- coding: utf-8 -*-
# 在相同值上有点问题，别的都挺好
# 花了几分钟写的
def quick_sort(A,start,end):
    origin_end=end
    origin_start=start
    if end<=start:
        return
    else:
        pivot=A[start]
        while end>start:
            while end>start and A[end]>=pivot:
                end=end-1
            temp=A[end]
            while end>start and A[start]<=pivot:
                start=start+1
#             exchange

            A[end]=A[start]
            A[start]=temp
    print start
    print end
    quick_sort(A,origin_start,start-1)
    quick_sort(A,start+1,origin_end)
    print A

# A=[10,2,16,5,3,6,7,100]
A=[49,38,65,97,76,13,27,49]
quick_sort(A,0,len(A)-1)

