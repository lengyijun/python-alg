# -*- coding: utf-8 -*-
__author__ = 'jaundice'
import  heapq

class node(object):
    def __init__(self):
        self.key=float("inf")
        self.parent=None

def init():
    s=node()
    t=node()
    x=node()
    z=node()
    y=node()
    edge=[(10,s,t),(1,t,x),(4,x,z),(6,z,x),(2,y,z),(5,s,y),(2,t,y),(3,y,t),(9,y,x),(7,z,s)]

    edge_map={}
    for length,v1,v2 in edge:
        edge_map[(v1,v2)]=length

    s.key=0
    vertex=[s,t,x,z,y]
    return edge,vertex,edge_map

# 得到相邻点的集合
def adj(edge):
    adj_map={}
    for length,v1,v2 in edge:
        adj_map[v1]=set()
    for length,v1,v2 in edge:
        adj_map[v1].add(v2)
    return adj_map

def relax(v1,v2,length):
    if v1.key+length<v2.key:
        v2.key=v1.key+length
        v2.parent=v1

if __name__ == '__main__':
    edge,vertex,edge_map=init()
    adj_map=adj(edge)


    S=set()
    vertex_copy=vertex[:]
    while len(vertex_copy)!=0:
        vertex_copy.sort(key=lambda x:x.key)
        temp=vertex_copy.pop(0)
        S.add(temp)

        for item in adj_map[temp]:
            relax(temp,item,edge_map[(temp,item)])

    for item in vertex:
        try:
            print(str(item.key)+"     "+str(item.parent.key))
        except:
            print("error")
