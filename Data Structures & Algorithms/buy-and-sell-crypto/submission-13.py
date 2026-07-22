class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        maxProfit =0
        for p in prices:
            maxProfit = max(maxProfit, p -low)
            if p <low:
                low = p
        return maxProfit
