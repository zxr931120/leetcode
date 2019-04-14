class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        ll = head
        #print(ll.next)

        while ll.next is not None:
            #print(ll.val)
            if ll.next.val == ll.val:
                if ll.next.next is not None:
                    #iv = ll.next
                    ll.next = ll.next.next
                    #del iv
                else:
                    ll.next = None

            else:
                ll = ll.next
        return head

llist = ListNode(2)
llist.next = ListNode(2)
llist.next.next = ListNode(2)
llist.next.next.next = ListNode(3)
llist.next.next.next.next = ListNode(3)
llist.next.next.next.next.next = None

sol = Solution()
newHead = sol.deleteDuplicates(llist)

while newHead.next is not None:
    print(newHead.val)
    newHead = newHead.next

print(newHead.val)
