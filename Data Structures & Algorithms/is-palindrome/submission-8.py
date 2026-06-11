class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_ = s.replace(' ','')
        # s =s.lower()
        # str1 =''
        # for item in s:
        #     if item.isalnum():
        #         str1+=item
        # return str1 == str1[::-1]
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        