# -*- coding: utf-8 -*-
__author__ = 'jaundice'
from copy import *

def create_node(n):
    return [node(key) for key in n]

class node(object):
    def __init__(self,key):
        self.key=key
        self.parent=None
        self.left=None
        self.right=None
    def in_left(self):
        return self==self.parent.left

def create_tree(nodes):
    quene=nodes[:]
    # quene=deepcopy(nodes) #此处还不可以用深拷贝
    while len(quene)>1:
        quene.sort(key=lambda item:item.key)
        node_left=quene.pop(0)
        node_right=quene.pop(0)
        node_father=node(node_left.key+node_right.key)
        node_father.left=node_left
        node_father.right=node_right
        node_left.parent=node_father
        node_right.parent=node_father
        quene.append(node_father)
    return quene[0]

def huffman_code(root):
    codes=["" for i in range(len(chars_freqs))]
    for i in range(len(chars_freqs)):
        node_temp=nodes[i]
        while node_temp!=root:
            if node_temp.in_left():
                codes[i]="0"+codes[i]
            else:
                codes[i]="1"+codes[i]
            node_temp=node_temp.parent
    return codes

if __name__ == '__main__':
    chars_freqs = [('C', 12), ('G', 2), ('E', 3), ('K', 3), ('B', 4),
                   ('F', 4), ('I', 4), ('J', 4), ('D', 5), ('H', 6),
                   ('N', 6), ('L', 7), ('M', 9), ('A', 10)]
    nodes=create_node(item[1] for item in chars_freqs)
    root=create_tree(nodes)
    codes=huffman_code(root)
    for item in zip(chars_freqs,codes):
        print item
