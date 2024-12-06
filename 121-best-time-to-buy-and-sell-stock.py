import array
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

# attempt 1
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
        
#         #sliding window technique, check every item after the index you are checking for. 
#         # This way you can check days 2345 for day 1. and days 345 for day 2 etc.
        
#         arr = array.array('i', prices)
#         highestProfitPossible = 0

#         for index, buyPrice in enumerate(arr):
#             if (arr[-1] == buyPrice):
#                 break
#             for possible in range(arr[index], len(arr)):
#                 # if the possible sell price is less than the buy price, and is larger than a previous profit
#                 if (arr[possible] - buyPrice > highestProfitPossible):
#                     highestProfitPossible = arr[possible] - buyPrice
#                     print('highest is now ', highestProfitPossible)
#         return highestProfitPossible
    
#attempt 2
# can do in o(n) just need to use two pointer
#leave left pointer at the lowest number you have seen
# variables = buy price, sell price, max profit
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        buyPriceIndex = 0
        sellPriceIndex = 0
        maxP = 0

        for stock in prices:
            if (prices[buyPriceIndex] < prices[sellPriceIndex]):
                profit = prices[sellPriceIndex] - prices[buyPriceIndex]
                # chooses the maximum between these two variables which changes max profit accordingly
                maxP = max(maxP, profit)
            else:
                #since there is a number lower than your current buy price, change the buy price to that one instead
                buyPriceIndex = sellPriceIndex

            sellPriceIndex += 1
                
        return maxP

sol = Solution()

test = [2, 4, 1]

test2 = [7,1,5,3,6,4]

test3 = [5,4,3,2,1]

# print(sol.maxProfit(test))

print(sol.maxProfit(test2))

print(sol.maxProfit(test3))