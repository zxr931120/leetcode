# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if root is None:
            return True
        leftList = []
        rightList = []
        self.treeStructTraversalLeft(root, leftList)
        self.treeStructTraversalRight(root, rightList)
        if leftList == rightList:
            return True
        else:
            return False

    def treeStructTraversalLeft(self, treenode: 'TreeNode', olist):
        olist.append(treenode.val)
        if treenode.left is not None:
            self.treeStructTraversalLeft(treenode.left, olist)
        else:
            olist.append(None)

        if treenode.right is not None:
            self.treeStructTraversalLeft(treenode.right, olist)
        else:
            olist.append(None)
            return

    def treeStructTraversalRight(self, treenode: 'TreeNode', olist):
        olist.append(treenode.val)
        if treenode.right is not None:
            self.treeStructTraversalRight(treenode.right, olist)
        else:
            olist.append(None)

        if treenode.left is not None:
            self.treeStructTraversalRight(treenode.left, olist)
        else:
            olist.append(None)
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
olist = []
sol.treeStructTraversalLeft(tnode, olist)
rolist = []
sol.treeStructTraversalRight(tnode, rolist)
print('left output list:', olist)
print('right output list:', rolist)

print(sol.isSymmetric(tnode))
