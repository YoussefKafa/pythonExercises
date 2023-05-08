class Solution:
    def bestProfit(self, prices :list)-> int:
        maxProfit=0
        for i in range(len(prices) - 1):
            if i < len(prices)-1:
                if prices[i+1]>prices[i]:
                    maxProfit+=prices[i+1]-prices[i]
                    i=i+1
        return maxProfit
    def bestProfit(self, prices: list[int]) -> int:
            maxProfit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    maxProfit += prices[i] - prices[i-1]
            return maxProfit
if __name__=='__main__':
    prices=[7,6,4,3,1]
    sol=Solution()
    print(sol.bestProfit(prices))