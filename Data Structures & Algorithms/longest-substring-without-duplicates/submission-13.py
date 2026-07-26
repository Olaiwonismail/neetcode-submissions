class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = 0
        y = 1
        mx= 1
        l=[]
        w = len(s)
        if w < 2:
            return w
        
        while y < w:
            l = s[x:y]
            
            if s[y] not in l:
                y+=1 
                if mx < y-x:
                    mx = y-x
            else:
                x+=1
                y=x+1
            
        return mx