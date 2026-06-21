class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lgth = len(prices)
        l = 0
        r = 1
        ans = 0
        while r < lgth:
            if prices[l] < prices[r]:
                if ans< prices[r]-prices[l]:
                    ans = prices[r] - prices[l]
                r+=1
            else:
                l+=1
                if l==r:
                    r+=1
        return ans





            

        