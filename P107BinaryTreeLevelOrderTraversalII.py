# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    BFlist = []
    index = 0
    allIndex = 0
    heightWIndex = []

    def allClear(self):
        self.BFlist = []
        self.index = 0
        self.allIndex = 0
        self.heightWIndex = 0

    def levelOrderBottom(self, root: 'TreeNode'):
        self.allClear()
        if root is None:
            return []
        self.BFlist.append(root)
        self.heightWIndex.append(0)
        self.BreadthFirstTraversal(self.BFlist[self.index])
        BFListval = [self.BFlist[i].val for i in range(0, self.allIndex + 1)]

        oList = []

        sIndex = 0
        for i in range(self.heightWIndex[self.allIndex] + 1):
            lInSameHeight = []
            while True:
                if self.heightWIndex[sIndex] == i:
                    lInSameHeight.append(BFListval[sIndex])
                    sIndex += 1
                    if sIndex > self.allIndex:
                        break
                else:
                    break
            oList.append(lInSameHeight)

        print('all index: ', self.allIndex)
        return oList[::-1]

    def BreadthFirstTraversal(self, treenode: 'TreeNode'):
        if treenode is None:
            self.index += 1
            self.BreadthFirstTraversal(self.BFlist[self.index])
            print(self.index)
            return
        if treenode.left is not None:
            self.BFlist.append(treenode.left)
            self.heightWIndex.append(self.heightWIndex[self.index] + 1)
            self.allIndex += 1

        if treenode.right is not None:
            self.BFlist.append(treenode.right)
            self.heightWIndex.append(self.heightWIndex[self.index] + 1)
            self.allIndex += 1

        self.index += 1
        print(self.index)
        if self.index > self.allIndex:
            return
        self.BreadthFirstTraversal(self.BFlist[self.index])
        return


tnode = TreeNode(5)
tnode1 = TreeNode(1)
tnode2 = TreeNode(2)
tnode3 = TreeNode(3)
tnode4 = TreeNode(4)
tnode5 = TreeNode(6)

tnode.left = tnode1
tnode.right = tnode2
tnode1.left = tnode3
tnode2.right = tnode4
tnode3.right = tnode5

sol = Solution()

sol = Solution()
print(sol.levelOrderBottom(tnode))
