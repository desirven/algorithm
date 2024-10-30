class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, total_profit = 0, 0
        buy = prices[0]
        prices.append(-1)
        for day in range(len(prices)-1):
            if prices[day] > buy:
                profit = max(profit, prices[day]-buy)
            else:
                buy = prices[day]

            if prices[day] > prices[day+1]:
                total_profit += profit
                profit, buy = 0, prices[day+1]
        return total_profit