# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split into 2
        if not head or not head.next or not head.next.next:
            return
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_head = slow.next
        slow.next = None

        # reverse the second one
        prev ,current = None, second_head 
        while current: 
            new = current.next
            current.next = prev
            prev =current
            current = new     
            

        second_head = prev
        # merge them back

        first , second = head.next , second_head
        
        head.next = second

        while second:
            next_first = first.next
            next_second =second.next
            second.next = first
            if next_second:
                first.next = next_second
            
            second = next_second
            first = next_first
            


