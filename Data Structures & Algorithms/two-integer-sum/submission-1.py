class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m ={}
        
        for i,item in enumerate(nums):
            look = target-item
            if look in m:
                return [m.get(look),i]
            m[item] = i
            
        
        
        