class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        nums = sorted(nums)
        seen = set()
        for n in range(0,len(nums)):

            left = 0
            right = len(nums)-1
            while left+1 < right:
                if right == n:
                    break
                if left == n:
                    break
                l = [nums[left] , nums[right] , nums[n]]
                s  = nums[left]+ nums[right]+ nums[n]

                if s >0:
                    right-=1
                    
                elif s < 0:
                    left += 1
                     
                else: 
                    z =  (nums[left], nums[right] , nums[n])
                    if z not in seen:
                        ans.append(l)
                        seen.add(z)
                    
                    left+=1
                    right-=1
 
        return ans
                