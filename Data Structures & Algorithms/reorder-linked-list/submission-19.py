# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # splt the linked list into 2
        fast = head
        slow = head
        if not head.next:
            return
        if not head.next.next:
            return
        if not head.next.next.next:
            f =head.next
            z = head.next.next
            head.next = z
            z.next = f
            f.next = None
            return

        while True:
            if not fast:
                break
            if not fast.next:
                break
            slow = slow.next
            fast = fast.next.next
            
        second_list = slow.next
        slow.next = None   
    
        # reverse the second
        if second_list.next:
            one = second_list
            two = second_list.next
            next_ =  second_list.next.next
            one.next = None
            while True:
                two.next = one
                one  = two
                two = next_
                if not next_:
                    break
                next_ = next_.next
            second_list = one
            
        
        first_list = head
        
        # merge em
        f2 =None
        f1 =None
        if first_list.next:
            f1 = first_list.next
        if second_list:
            f2 = second_list
        
        extra1 = None
        extra2 = None

        head.next = f2
        while True:
            # merge the two list 
            if not f1:
                f2 = None
                break
            if not f2:
                f1 = None
                break
            extra2 = f2.next
            extra1 = f1.next
            f2.next = f1
            f2 = extra2
            if extra2:
                f1.next = extra2
            else:
                break
            f1 =extra1
            

            

            


        # set the last one as null
