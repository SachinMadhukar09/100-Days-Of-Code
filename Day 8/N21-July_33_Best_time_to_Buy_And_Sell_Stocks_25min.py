# Link Leetcode  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#      GFG    https://practice.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1

# 21-July 06:50AM-07:15AM 25min Not Completed


# 121. Best Time to Buy and Sell Stock
# Easy

# 9613

# 395

# Add to List

# Share
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


def maxProfit(prices):
        c=0
        d=0
        for i in range(len(prices)-2):
            for j in range(i,len(prices)-2):
                if(prices[i]<prices[j]):
                    c=prices[i]
                else:
                    return 0
            for j in range(i,len(prices)-2):
                if(prices[j+1]>prices[j+2]):
                    d=prices[j+1]
                    # break
        return (d-c)

prices=[7,6,4,3,1]
print(maxProfit(prices))
    