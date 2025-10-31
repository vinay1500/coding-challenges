class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low, high = 0, 1
        maxProfit = 0

        while high < (len(prices)):
            if prices[low] < prices[high]:
                profit = prices[high] - prices[low]
                maxProfit = max(maxProfit, profit)
            else:
                low = high
            high += 1
        return maxProfit
#prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]
myObj =Solution()
print(myObj.maxProfit(prices))