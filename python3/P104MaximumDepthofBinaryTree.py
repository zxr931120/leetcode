# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    md = 0

    def maxDepth(self, root: 'TreeNode') -> 'int':
        if root is None:
            return self.md
        depth = 0
        self.DepthFirstTraversal(root, depth)
        return self.md + 1

    def DepthFirstTraversal(self, treenode: 'TreeNode', nowdepth):
        nd = nowdepth
        if nowdepth > self.md:
            self.md = nowdepth
        if treenode.left is not None:
            self.DepthFirstTraversal(treenode.left, nowdepth + 1)

        if treenode.right is not None:
            self.DepthFirstTraversal(treenode.right, nowdepth + 1)

        return


tnode = TreeNode(5)
tnode1 = TreeNode(2)
tnode2 = TreeNode(3)
tnode3 = TreeNode(2)
tnode4 = TreeNode(3)

tnode.left = tnode1
tnode1.left = tnode2
tnode.right = tnode3
tnode3.right = tnode4

sol = Solution()
print(sol.maxDepth(tnode))
