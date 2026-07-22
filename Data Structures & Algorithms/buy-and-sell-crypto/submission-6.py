class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP =0
        lmin = prices[0]
        for sell in prices:
            maxP = max(maxP, sell - lmin)
            lmin = min(lmin , sell)
        return maxP