class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m =0
        low = prices[0]
        for i in prices:
            m = max(m, i- low)
            if i <low:
                low = i
        return m