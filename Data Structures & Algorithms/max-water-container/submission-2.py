class Solution:
    def maxArea(self, heights: List[int]) -> int:
       
        ans =0
        width = len(heights)
        for l in range(0,width-1):
            for r in range(1,width):
                if heights[l] >= heights[r]:
                    if ans < (heights[r]*(r-l)):
                        ans = heights[r]*(r-l)
                if heights[l] < heights[r]:
                    if ans < (heights[l]*(r-l)):
                        ans = heights[l]*(r-l)
            
        return ans

        