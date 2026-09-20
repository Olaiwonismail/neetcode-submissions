class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        n = sorted(nums)
        for i in range(len(n)):
            
            end = len(n)-1
            start = i+1
            
            
            while start < end:
                
                
                if n[end]+n[start]+n[i] == 0:
                    l = sorted([n[end],n[start],n[i]])
                    if l not in ans:
                        ans.append(l)
                    start += 1
                    end -= 1

                else:
                    if n[end]+n[start]+n[i] < 0:
                        start += 1
                        
                    if n[end]+n[start]+n[i] > 0:
                        end -= 1
                # if start == i and start < len(n)-1:
                #     start+=1
                # if end ==i and end > 0:
                #     end-=1

        return ans

                

                
        