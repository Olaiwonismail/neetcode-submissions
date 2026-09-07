class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        # left pass
        p =1
        for n in range(0,len(nums)-1):
            p *= nums[n]
            left[n+1] = p

        # right pass
        p =1 
        for n in range(len(nums)-1,0,-1):
            p *= nums[n]
            right[n-1] = p

        ans = []
        for n  in range(0,len(nums)):
            ans.append(left[n]*right[n])
        return ans



        