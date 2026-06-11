class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_ = s.replace(' ','')
        s =s.lower()
        list1= [item for item in s if item.isalnum()]
        return list1 == list1[::-1]
        