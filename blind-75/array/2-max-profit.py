class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
    
    def maxProfit_amey(self, prices):
        lowest = 0
        highestDiff = 0
        for i in range(len(prices)):
            if prices[i] - prices[lowest] > highestDiff:
                highestDiff = prices[i] - prices[lowest]
            if prices[i] < prices[lowest]:
                lowest = i
        return highestDiff
    

def main():
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit_amey(prices))

main()