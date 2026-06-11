class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # index =0
        l= 0
        nums=sorted(nums)
        leng = len(nums)
        r=leng-1
        solution = {}
        for index in range(0,leng):
            l= 0
            r=leng-1
            while l<r:
                if l == index:
                    l+=1
                    continue
                if r == index:
                    r-=1
                    continue
                sum_ = nums[l] + nums[index] + nums[r]
                
                if sum_ == 0:
                    ans = tuple(sorted([nums[l],nums[index],nums[r]]))
                    
                    if ans not in solution:
                        solution[ans] = ans
                    l+=1
                    r-=1
                    
                if sum_ < 0:
                    l+=1  
                if sum_ > 0: 
                    r-=1
                   
        return [list(list_item) for list_item in solution.keys()]



        