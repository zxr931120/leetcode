# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            if l2 is None:
                return None
            else:
                return l2

        if l2 is None:
            return l1

        outlistlen = self.getListLength(self, l1) + self.getListLength(self, l2)
        print(outlistlen)

        for i in range(outlistlen):
            if i == 0:
                if l1.val <= l2.val:
                    outlisthead = ListNode(l1.val)
                    l1 = l1.next
                else:
                    outlisthead = ListNode(l2.val)
                    l2 = l2.next

                if outlistlen > 1:
                    outlist = ListNode(0)
                    outlisthead.next = outlist
                else:
                    return outlisthead
                continue

            if l1 is None:
                outlist.val = l2.val
                l2 = l2.next
                if l2 is not None:
                    outlist.next = ListNode(0)
                    outlist = outlist.next

                continue

            if l2 is None:
                outlist.val = l1.val
                l1 = l1.next
                if l1 is not None:
                    outlist.next = ListNode(0)
                    outlist = outlist.next

                continue

            if l1.val <= l2.val:
                outlist.val = l1.val
                l1 = l1.next
            else:
                outlist.val = l2.val
                l2 = l2.next

            outlist.next = ListNode(0)
            outlist = outlist.next

        return outlisthead

    def getListLength(self, l):
        llen = 1
        while l.next is not None:
            llen += 1
            l = l.next

        return llen

    def printList(self, l):
        print('print list')
        print(l.val)
        while l.next is not None:
            print(l.next.val)
            l = l.next

#Accepted

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(2)
l2.next.next.next = ListNode(5)
l2.next.next.next.next = ListNode(7)

sol = Solution

outl = sol.mergeTwoLists(sol, l1, l2)
print(sol.getListLength(sol,outl))

sol.printList(sol,outl)
