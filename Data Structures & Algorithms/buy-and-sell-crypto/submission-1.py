class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the beginning of the window
        x = 0
        # the end of the window 
        y=1
        mx=0
        l = len(prices)
        while y < l:
            if prices[y] - prices[x] < 0:
                x = y
                y+=1
            else:
                if prices[y] - prices[x] > mx :
                    mx = prices[y] - prices[x]
                y+=1
        return mx
                    

                
                





            

        