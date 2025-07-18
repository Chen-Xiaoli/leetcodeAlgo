class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        length = len(prices)

        
        for i in range(length):
            for j in range(i+1, length):
                if prices[j] <= prices[i]:
                    prices[i] = prices[i] -  prices[j]
                    break
        return prices