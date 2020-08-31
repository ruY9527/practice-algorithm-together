package com.ws.leetcode;

import com.alibaba.fastjson.JSON;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * @author ：wangsun
 * @date ：Created in 2020/8/31 19:23
 * @project : leetcode
 * @package : com.ws.leetcode
 * @description： 两数相加
 */
public class NumberPlus {

    /**
     * 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
     * <p>
     * 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
     *
     * @param l1
     * @param l2
     * @return
     */
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode newListNode = null;
        int i = l1.val+l2.val;
        if (i<=9){
            newListNode = new ListNode(i);
            if (l1.next!=null&&l2.next!=null) {
                newListNode.next = addTwoNumbers(l1.next, l2.next);
            }else if (l1.next!=null){
                newListNode.next = l1.next;
            }else if (l2.next!=null){
                newListNode.next = l2.next;
            }
        }else{
            i = i-10;
            newListNode = new ListNode(i);
            if (l1.next!=null&&l2.next!=null) {
                newListNode.next = addTwoNumbers(addTwoNumbers(new ListNode(1),l1.next), l2.next);
            }else if (l1.next!=null){
                newListNode.next = addTwoNumbers(new ListNode(1),l1.next);
            }else if (l2.next!=null){
                newListNode.next =addTwoNumbers(new ListNode(1),l2.next);
            }else{
                newListNode.next = new ListNode(1);
            }
        }
        return newListNode;
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(1);
        ListNode next = new ListNode(6);
        ListNode againNext = new ListNode(3);
        //l1.next = next;
        //l1.next.next = againNext;
        ListNode l2 = new ListNode(4);
        ListNode l2Next = new ListNode(5);
        ListNode l2AgainNext = new ListNode(5);
        //l2.next = l2Next;
        //l2.next.next = l2AgainNext;
        ListNode listNode = addTwoNumber(l1, l2);
        printListNode(listNode);
    }

    public static void printListNode(ListNode l1){
        System.out.println("int is "+ l1.val);
        if (l1.next!=null){
            printListNode(l1.next);
        }
    }

    public static ListNode addTwoNumber(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int carry = 0;
        while (p != null || q != null) {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        }
        if (carry > 0) {
            curr.next = new ListNode(carry);
        }
        return dummyHead.next;
    }



}

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}
