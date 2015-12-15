# -*- coding: utf-8 -*-
# https://github.com/qiwsir/algorithm/blob/master/prim_algorithm.md
from collections import defaultdict
from heapq import *

def prim( vertexs, edges ):
    adjacent_vertex=defaultdict(list)
    for v1,v2,length in edges:
        adjacent_vertex[v1].append((length,v2,v1))
        adjacent_vertex[v2].append((length,v1,v2))
    mst=[]

    # set表示一个集合
    chosed=set(vertexs[0])
    adjacent_vertex_edge=adjacent_vertex[vertexs[0]]
    heapify(adjacent_vertex_edge)
    while adjacent_vertex_edge:
        length,v1,v2=adjacent_vertex_edge.pop()
        if v1 not in chosed:
            chosed.add(v1)
            mst.append((length,v1,v2))
            for nexe_vertex in adjacent_vertex[v1]:
                heappush(adjacent_vertex_edge,nexe_vertex)
    return mst




# 把一个字符串转化为一个列表,很有用处
vertexs = list("ABCDEFG")
edges = [ ("A", "B", 7), ("A", "D", 5),
          ("B", "C", 8), ("B", "D", 9),
          ("B", "E", 7), ("C", "E", 5),
          ("D", "E", 15), ("D", "F", 6),
          ("E", "F", 8), ("E", "G", 9),
          ("F", "G", 11)]
print(prim(vertexs,edges))

