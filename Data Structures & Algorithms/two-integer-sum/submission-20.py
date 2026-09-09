class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        l = len(nums)
        for n in range(l):
            diff = target - nums[n]
            if diff in m:
                return sorted([m[diff],n])
            m[nums[n]] = n

        
         
            
        
        
        