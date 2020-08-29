package leetcode

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

//二叉树的前序遍历
//手动维护一个栈
func preorderTraversal(root *TreeNode) []int {
	if root == nil{
		return []int{}
	}
	stack,res := []*TreeNode{},[]int{}
	stack = append(stack,root)
	for len(stack) != 0{
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if node != nil{
			res = append(res,node.Val)
		}
		if node.Right != nil{
			stack = append(stack,node.Right)
		}
		if node.Left != nil{
			stack = append(stack,node.Left)
		}
	}
	return res
}
