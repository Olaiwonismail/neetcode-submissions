class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_ = s.replace(' ','')
        s =s.lower()
        str1 =''
        for item in s:
            if item.isalnum():
                str1+=item
        return str1 == str1[::-1]
        