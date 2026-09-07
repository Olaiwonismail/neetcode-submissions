class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        l = set(nums)
        if len(l)<2:
            return len(l)
        ans = 0
        counter = 1

        for num in l:
            if num-1 not in l:
                counter = 1
                start = num
                while start+1 in l:
                        counter+= 1
                        start+=1
                    
            if ans < counter:
                ans = counter
                      
        return ans
                        


        # ans = 0
        # counter = 1
        # if not nums:
        #     return 0
        # l = list(set(nums))
        # l = sorted(l)
        # for n in range(len(l)-1):
        #     if l[n+1] - l[n] == 1:
        #         counter+=1
            
        #     else:
        #         if ans < counter:
        #             ans = counter
        #         counter = 1
        # if ans < counter:
        #         ans = counter
        # return ans

        
        