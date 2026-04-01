class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        ans = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > ans:
                ans = profit
            if prices[r] < prices[l]:
                l = r
            r += 1
        return ans