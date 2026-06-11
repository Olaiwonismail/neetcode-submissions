class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_ = s.replace(' ','')
        
        str1 =''
        for item in s:
            if item.isalnum():
                str1+=item.lower()
        return str1 == str1[::-1]
        