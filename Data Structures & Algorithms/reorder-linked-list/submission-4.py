# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # het the head
        a = head 
        b= head
        if head and head.next:
            l = []
            while True:
                if not a:
                    break
                l.append(a)
                a= a.next
            p1 = 0
            p2 = len(l)-1
            while True:
                l[p1].next = l[p2]
                if p2 == p1+1 and len(l)%2 ==0:
                    break
                l[p2].next = l[p1+1]
                p1+=1           
                p2-=1
                if p2 < p1:
                    break
            if len(l)%2 ==0:
                l[p2].next = None
            else:
                l[int(len(l)/2+0.5)-1].next = None
       
        


        # merge them 


