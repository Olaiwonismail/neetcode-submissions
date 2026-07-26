class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = 0
        y = 1
        max_length= 1
        substring=[]
        width = len(s)
        if width < 2:
            return width
        
        while y < width:
            substring = s[x:y]
            
            if s[y] not in substring:
                y+=1 
                if max_length < y-x:
                    max_length = y-x
            else:
                x+=1
                y=x+1
            
        return max_length