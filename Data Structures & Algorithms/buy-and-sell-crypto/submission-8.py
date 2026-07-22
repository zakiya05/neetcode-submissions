class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp =0 
        for i in range(len(prices)):
            if prices[i]<minp:
                minp = prices[i]
            maxp= max(maxp, prices[i]- minp)
        return maxp