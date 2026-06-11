class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0     
        s =s.lower()
        list1= [item for item in s if item.isalnum()]
        r=len(list1)-1
        while l<r:
            if list1[l]==list1[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        