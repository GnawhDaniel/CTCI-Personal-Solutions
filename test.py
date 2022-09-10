class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):

        def recurse(node, previous=None):
            if node is None:
                return previous
            a = recurse(node.next, node)
            node.next = previous
            return a
        
        return recurse(head)


head = ListNode(1)
placeholder = head
for i in range(2, 6):
    head.next = ListNode(i)
    head = head.next

a = Solution().reverseList(placeholder)

while a != None:
    print(a.val)
    a = a.next