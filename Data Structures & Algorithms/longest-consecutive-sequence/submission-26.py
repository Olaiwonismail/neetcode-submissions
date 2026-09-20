class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ns = list(set(nums))
        ns = sorted(ns)
        
        count = 1
        ans = 1
        for i in range(1,len(ns)):
            if ns[i] - ns[i-1] == 1:
                count+=1
            else:
                if count > ans:
                    ans = count
                count =1
        if count > ans:
            ans = count
        return ans

