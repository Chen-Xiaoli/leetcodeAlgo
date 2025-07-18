class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        # length = len(prices)

        
        # for i in range(length):
        #     for j in range(i+1, length):
        #         if prices[j] <= prices[i]:
        #             prices[i] = prices[i] -  prices[j]
        #             break
        # return prices

        n = len(prices)
        ans = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            p = prices[i]

            while stack and stack[-1] > p:
                stack.pop()
            
            if stack:
                ans[i] = p - stack[-1]
            else:
                ans[i] = p
            
            stack.append(p)
        return ans

