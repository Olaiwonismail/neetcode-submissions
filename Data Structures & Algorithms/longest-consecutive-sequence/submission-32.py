class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        pl = 1
        ans = 1
        numbs = set(nums)
        for item in numbs:
            if item+1 in numbs and item-1 not in numbs:
                while (item+1) in numbs:
                    pl +=1
                    item+=1
                if ans< pl:
                    ans = pl
                pl =1
                   

        if ans< pl:
            ans = pl
        return ans
                    
                
