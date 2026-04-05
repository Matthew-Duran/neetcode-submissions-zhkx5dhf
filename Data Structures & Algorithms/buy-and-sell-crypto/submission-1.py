class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_now = prices[0]

        for p in prices:
            min_now = min(p, min_now)
            max_profit = max(max_profit, p - min_now)
            p += 1
        return max_profit



        