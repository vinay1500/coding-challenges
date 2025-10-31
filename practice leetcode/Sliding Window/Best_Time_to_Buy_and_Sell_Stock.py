class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low, high = prices[0], 0
        maxProfit = 0

        for i in range(len(prices)):
            low = min(low, prices[i])
            high = prices[i]
            #print(f"high {high}")
            #print(f"low {low}")
            profit = high - low
            #print(f"profit {profit}")
            #if profit > 0:
                #high +=1
            maxProfit = max(maxProfit, profit)
        return maxProfit
#prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]
myObj =Solution()
print(myObj.maxProfit(prices))