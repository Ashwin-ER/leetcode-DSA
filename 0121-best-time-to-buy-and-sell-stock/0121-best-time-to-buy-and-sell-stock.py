class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        minPurchase = prices[0]
        for i in range(1, len(prices)):		
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        return maxProfit