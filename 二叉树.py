# -*- coding: utf-8 -*-
__author__ = 'jaundice'
# 二叉树的遍及
# http://www.cnblogs.com/yupeng/p/3414451.html

class TreeNode(object):
    def __init__(self,data=0,left=0,right=0):
        self.data=data
        self.left=left
        self.right=right

class BTree(object):
    def __init__(self,root=0):
        self.root=root

    def is_empty(self):
        if self.root is 0: #             todo is 是什么东西？？
            return True
        else:
            return False

    # 这是不推荐的递归算法
    def preOrder(self,treenode):
        if treenode is 0:
            return
        print treenode.data
        self.preOrder(treenode.left)
        self.preOrder(treenode.right)

    # 前序，非递归
    def preOrder_change(self,treenode):
       if treenode.data==0:
           return
       else:
           ss=[]
           ss.append(treenode)
           while len(ss)!=0:
               print ss[-1].data
               temp=ss[-1]
               ss.pop(-1)
               if temp.right!=0:
                   ss.append(temp.right)
               if temp.left!=0:
                   ss.append(temp.left)

    # 中序，非递归
    def midOrder(self,treenode):

        if treenode.data==0:
            return
        else:
            ss=[]
            ss.append(treenode)
            while len(ss)!=0:
                temp=ss[-1]
                dict[temp]=dict[temp]+1
                if dict[temp]==2:
                    print temp.data
                    ss.pop(-1)
                    if temp.right!=0:
                        ss.append(temp.right)
                else:
                    if temp.left!=0:
                        ss.append(temp.left)

    # 后序，非递归
    def postOrder(self,treecode):
        if treecode.data==0:
            return
        else:
            ss=[]
            ss.append(treecode)
            while len(ss)!=0:
                temp=ss[-1]
                dict[temp]=dict[temp]+1
                if dict[temp]==3:
                    ss.pop(-1)
                    print(temp.data)
                if dict[temp]==2:
                    if temp.right!=0:
                        ss.append(temp.right)
                if dict[temp]==1:
                    if temp.left!=0:
                        ss.append(temp.left)


n1 = TreeNode(data=1)
n2 = TreeNode(2,n1,0)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5,n3,n4)
n6 = TreeNode(6,n2,n5)
n7 = TreeNode(7,n6,0)
n8 = TreeNode(8)
root = TreeNode('root',n7,n8)

dict={}
dict[n1]=0
dict[n2]=0
dict[n3]=0
dict[n4]=0
dict[n5]=0
dict[n6]=0
dict[n7]=0
dict[n8]=0
dict[root]=0
# print dict

bt=BTree(root)
# print "preorfer"
# print bt.preOrder(bt.root)
# print bt.preOrder_change(bt.root)
# print bt.midOrder(bt.root)
print bt.postOrder(bt.root)
