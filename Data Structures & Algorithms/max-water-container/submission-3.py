class Solution:
    def maxArea(self, heights: List[int]) -> int:
       
        l =0
        r = len(heights)-1
        area = 0

        while l<r:
            new_area = min(heights[l],heights[r])*(r-l)
            if area < new_area:
                area = new_area
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
            
        return area

        