class Solution:
    def maxArea(self, heights: List[int]) -> int:
       
        ans =0
        for l in range(0,len(heights)-1):
            for r in range(1,len(heights)):
                if heights[l] >= heights[r]:
                    if ans < (heights[r]*(r-l)):
                        ans = heights[r]*(r-l)
                if heights[l] < heights[r]:
                    if ans < (heights[l]*(r-l)):
                        ans = heights[l]*(r-l)
            
        return ans

        