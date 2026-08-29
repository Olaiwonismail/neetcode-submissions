# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we have a linked list and a hash map and an index
        m = {}
       
        index =-1
        counter = None
        current = head
       
        while True:

            
            if not current:
                break
            if current in m:
                
                index = m[current]
                return True
            else:
                if not counter:
                    counter=0
               
                m[current] = counter
                counter+=1
                if not current.next:
                    index = -1
                    return False
                else:
                    current= current.next
        index = -1
        return False


        # if we find a value we get the index

        # if index is -1 we return false
        