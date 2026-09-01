class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 ={}
        h2= {}

        for letter in s:
            h1[letter] = h1.get(letter,0)+1
        for letter in t:
            h2[letter] = h2.get(letter,0)+1
        return h2==h1
        # s = sorted(s)
        # t = sorted(t)
        # return s==t    