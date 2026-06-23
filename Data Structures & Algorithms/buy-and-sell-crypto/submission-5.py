class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = buy+1
        max_profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]: #buy or hold
                max_profit = max((prices[sell] - prices[buy]),max_profit)
            else: #sell
                buy = sell
            sell += 1
        return max_profit

    # # DP:
    #     max_profit = 0
    #     min_buy = prices[0]
    #     for sell in prices:
    #         max_profit = max(max_profit,sell - min_buy)
    #         min_buy = min(sell,min_buy)
    #     return max_profit
    
