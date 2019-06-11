# -*- coding: utf-8 -*-
# Author:haiyuchiluomeng
class Node(object):
    def __init__(self,item):
        self.elem=item
        self.lson=None
        self.rson=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def add(self,item):#树里添加元素
        node=Node(item)
        if self.root is None:
            self.root=node
            return
        queue = [self.root]
        while queue:
            cur=queue.pop(0)
            if cur.lson is None:
                cur.lson=node
                return
            else:
                queue.append(cur.lson)
            if cur.rson is None:
                cur.rson=node
                return
            else:
                queue.append(cur.rson)
    def breadth_travel(self):
        #广度遍历
        if self.root is None:#树为空直接返回
            return
        queue=[self.root]#让队列存放第一个节点
        while queue:
            cur = queue.pop(0)#取出第一个节点
            print(cur.elem)#输出当前节点
            if cur.lson is not None:#如果左二子不为空则添加到队列中
                queue.append(cur.lson)
            if cur.rson is not None:#如果右儿子不为空则添加到队列中
                queue.append(cur.rson)
    def prevtravel(self,node):
        #先序遍历
        if node is None:
            return
        print(node.elem,end=' ')#输出根
        self.prevtravel(node.lson)#左儿子递归
        self.prevtravel(node.rson)#右儿子递归

    def intravel(self,node):
        #中序遍历
        if node is None:
            return
        self.intravel(node.lson)#左儿子递归
        print(node.elem, end=' ')  # 输出根
        self.intravel(node.rson)#右儿子递归
    def posttravel(self,node):
        #后序遍历
        if node is None:
            return
        self.posttravel(node.lson)#左儿子递归
        self.posttravel(node.rson)#右儿子递归
        print(node.elem, end=' ')  # 输出根

if __name__ =="__main__":
    tree=BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.prevtravel(tree.root)
    print(' ')
    tree.intravel(tree.root)
    print(' ')
    tree.posttravel(tree.root)

