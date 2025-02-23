class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0  # Buy pointer
        h = 1  # Sell pointer

        while h < len(prices):
            # If current price is lower than the buy price, update the buy pointer
            if prices[h] < prices[l]:
                l = h  # New potential buy point

            # Calculate the potential profit
            profit = prices[h] - prices[l]

            # Update max_profit if we find a better profit
            if profit > max_profit:
                max_profit = profit

            h += 1

        return max_profit