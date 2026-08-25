# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        items= []
        if head == None:
            return head
        if head:
            items.append(head.val)
            current = head.next
            while current:
                items.append(current.val)
                current = current.next
        
        x = ListNode(items[-1])
        items.pop()
        current = x
        while len(items)>0:
            current.next = ListNode(items[-1])
            items.pop()
            current = current.next
        return x
            
            