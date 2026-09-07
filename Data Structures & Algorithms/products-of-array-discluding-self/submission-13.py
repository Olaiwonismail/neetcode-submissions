class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # solving wth 0(n) space
        ans = [1]* len(nums)
        
        # first pass
        p = 1
        l = len(nums)-1
        for n in range(0,l):
            p *= nums[n]
            ans[n+1] = p
        
        # second pass
        p =1
        for n in range(l,0,-1):
            p*= nums[n]
            ans[n-1] *= p
        return ans 


        
        # left = [1] * len(nums)
        # right = [1] * len(nums)

        # # left pass
        # p =1
        # for n in range(0,len(nums)-1):
        #     p *= nums[n]
        #     left[n+1] = p

        # # right pass
        # p =1 
        # for n in range(len(nums)-1,0,-1):
        #     p *= nums[n]
        #     right[n-1] = p

        # ans = []
        # for n  in range(0,len(nums)):
        #     ans.append(left[n]*right[n])
        # return ans



        