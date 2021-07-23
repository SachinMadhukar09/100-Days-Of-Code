# link Leetcode-https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

# 23 july 04:33PM-04:53PM 20 min Complted by HELP 


def maxProfit(prices):
    tmin=prices[0]
    tmax=0
    for i in prices:
        if i < tmin:
            tmin=i
        elif i>tmin:
            d=i-tmin
            tmax=max(tmax,d)
    return tmax
prices=[7,1,5,3,6,4]
print(maxProfit(prices))

# Not Completed on GFG