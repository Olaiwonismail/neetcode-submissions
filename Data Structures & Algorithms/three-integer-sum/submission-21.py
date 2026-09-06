class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        nums = sorted(nums)
        for n in range(1,len(nums)):

            left = 0
            right = len(nums)-1
            while left+1 < right:
                if right == n:
                    right-=1
                if left == n:
                    left+=1
                l = sorted([nums[left] , nums[right] , nums[n]])
                s  = nums[left]+ nums[right]+ nums[n]

                if s >0:
                    right-=1
                    
                elif s < 0:
                    left += 1
                     
                else:
                    if l not in ans:
                        ans.append(l)
                    left+=1
                    right-=1
                    
      
        return ans
                