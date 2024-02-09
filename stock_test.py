"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Input: prices = [7,1,5,3,6,4]
Output: 7

Input: prices = [7,6,4,3,1]
Output: 0

7,1,5,3,4,9

p = 0 + (5-1) + (4-3) + (9-4) = 10
b = 7 -> 1 -> 5 -> 3 -> 4 -> 9 if b > prices[i]
"""


def max_profit(prices):
    size = len(prices)

    if size < 2:
        return 0

    profit = 0
    buy = prices[0]

    for i in range(1, size):
        if prices[i] < buy: #buy condition
            buy = prices[i]
        else:
            profit += (prices[i] - buy)
            buy = prices[i]

    return profit


prices = [7, 1, 5, 3, 4, 9]

# i = 0 -> 1 -> 2 -> 3 -> 4 -> 5
#buy = 7 -> 1 -> 5 -> 3 -> 4 -> 9
#profit = 0 + (5 - 1) + (4 - 3) + (9 - 4) = 10

print(max_profit(prices))
