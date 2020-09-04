"""
    二叉树所有的路径
    给定一个二叉树，返回所有从根节点到叶子节点的路径。
    输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

"""
    :type root: TreeNode
    :rtype: List[str]
"""
def binaryTreePaths(roots):
    
    def construct_paths(root,path):
        # 如果 root 是 None 的情况,那么就相当于这层递归是已经结束了的
        if root:
            path += str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            else:
                path += '>'
                construct_paths(root.left,path)
                construct_paths(root.right,path)    
    paths = []
    construct_paths(roots,paths)
    return paths