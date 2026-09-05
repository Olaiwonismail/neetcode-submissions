class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        prefix = []
        postfix = []
        answer = [1] * len(nums)
        p= 1
        for num in nums:
            p *=num
            prefix.append(p)
        p=1
        for num in reversed(nums):
            p *= num
            postfix.append(p)
        postfix.reverse()

        for n in range(len(nums)):
            if n == 0:
                answer[n] = postfix[n+1]
            elif n == len(nums)-1:
                answer[n] = prefix[n-1]
            else:
                answer[n] = prefix[n-1] * postfix[n+1]
        return answer


            









        # brute force
        # ans = []
        # for excluded_num_index in range(len(nums)):
        #     p = 1
        #     for num_index in range(len(nums)):
        #         if num_index != excluded_num_index:
        #             p *= nums[num_index]
                    
        #     ans.append(p)
        # return ans

        