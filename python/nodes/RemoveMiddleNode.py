# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/30 0:47
@Auth ： GavinYang
@File ：RemoveMiddleNode.py
@IDE ：PyCharm
@Motto： 多反思是否还有更好的实现方式
leetCode: https://leetcode-cn.com/problems/delete-middle-node-lcci/
"""

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

'''
    把node的下一位覆盖给node.
    a->b->c->d->e->f  修改为  a->b->d->e->f
    如果需要删除的是c的话,那么也就是传入进来的node是c,然后将c替换成为下一个的值和指向都替换成下一个即可.
'''
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
