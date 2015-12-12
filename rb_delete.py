# -*- coding: utf-8 -*-

def RB_delete_fixup(T,x):
    while x.color=="b" and T.root!=x:
        if x==x.parent.left:
            s=x.parent.right
            if s.color=="r":
                left_rotate(T,x.parent)
                x.parent.color="r"
                s.color="b"
                s=x.parent.right
            if s.left.color=="b" and s.right.color=="b":
                s.color="r"
                x=x.parent
            else:
                if s.right.color=="b":
                    right_rotate(T,s)
                    s.color="r"
                    s.left.color="b"
                    s=x.parent.right
                left_rotate(T,x.parent)
                s.color=x.parent.color
                x.parent.color="b"
                s.right.color="b"
                x=T.root

