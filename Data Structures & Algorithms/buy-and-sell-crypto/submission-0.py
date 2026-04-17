class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0        # buy
        r = 1        # sell

        maxProfit = 0

        while r < len(prices):

            # profitable window
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)

            # bad window -> found cheaper buy day
            else:
                l = r

            r += 1

        return maxProfit