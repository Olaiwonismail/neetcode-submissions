# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # we use a tracker for the  2 lists
        tracker1 = list1
        tracker2 = list2
        if not tracker1:
            return tracker2
        if not tracker2:
            return tracker1
        if tracker1.val < tracker2.val:
            node = ListNode(tracker1.val)
            
            tracker1 = tracker1.next
        else:
            node = ListNode(tracker2.val)
            tracker2 = tracker2.next
        head = node
        # using the lesser one we start the linked list
        while True:
            if not (tracker2 and tracker1):
                if not tracker2:
                    node.next = tracker1
                else:
                    node.next = tracker2
                break
            
            if tracker1.val < tracker2.val:
                node.next= tracker1
                node= node.next
                
                
                tracker1 = tracker1.next
            else: 
                node.next= tracker2
                node= node.next
                # if tracker2.next:  
                tracker2 = tracker2.next
            
            
        return head
            
            
        