class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index, buy = min(enumerate(prices), key=lambda x: x[1])
        sell=max(prices[index:])
        return sell-buy