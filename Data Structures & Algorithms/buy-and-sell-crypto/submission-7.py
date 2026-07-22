class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp= 0
        lmin = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<lmin:
                lmin = prices[i]
            maxp = max(maxp, prices[i]- lmin)
        return maxp