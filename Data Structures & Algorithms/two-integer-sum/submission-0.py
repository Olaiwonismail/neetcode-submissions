class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m ={}
        counter =0
        for item in nums:
            look = target-item
            if look in m:
                return [m.get(look),counter]
            m[item] = counter
            counter+=1
        
        
        