# -*- coding: utf-8 -*-
from heapq import *
def krustal(vertex,edges):
    dict={}
    for ver in vertexs:
        dict[ver]=set(ver)

    # print(edges)
    heapify(edges)
    # print(edges)

    result=[]
    while edges:
        # 注意pop的方式
        w,v1,v2,=heappop(edges)
        if v1 not in dict[v2]:
            result.append((v1,v2,w))
            dict[v1]=dict[v1].union(dict[v2])
            for ver in dict[v1]:
                dict[ver]=dict[v1]
            if len(dict[v1])==len(vertexs):
                break
    return result



vertexs = list("ABCDEFG")
edges = [ (7,"A", "B", ),
          (5,"A", "D", ),
          (8,"B", "C", ),
          (9,"B", "D", ),
          (7,"B", "E", ),
          (5,"C", "E", ),
          (15,"D", "E", ),
          (6,"D", "F", ),
          (8,"E", "F", ),
          (9,"E", "G", ),
          (11,"F", "G", )]
# krustal(vertexs,edges)
print(krustal(vertexs,edges))
