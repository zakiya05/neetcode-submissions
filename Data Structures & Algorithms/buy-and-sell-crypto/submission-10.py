class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lmin = prices[0]
        res =-1
        for p in prices:
            res = max(res, p-lmin)
            if p <lmin:
                lmin = p
        return res