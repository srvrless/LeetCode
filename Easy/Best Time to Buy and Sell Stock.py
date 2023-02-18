from typing import List

prices = [2, 4, 1]


def maxProfit(prices: List[int]) -> int:
    for i, y in enumerate(prices):
        if prices[i] < prices[i + 1]:
            mins = y
    # mins = min(prices)
    indx = prices.index(mins)
    return max(prices[indx:]) - mins


print(maxProfit(prices))
