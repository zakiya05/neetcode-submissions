class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ml = float("inf")
        profit = 0
        for p in prices:
            print(p,profit,ml)
            if ml > p:
                ml = p
            lp = p - ml
            profit = max(profit,lp)

        return profit 