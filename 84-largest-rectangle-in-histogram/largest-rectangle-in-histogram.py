class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = list()
        res = 0

        newHeights = [0] * (len(heights) + 2)

        for i in range(1, len(heights) + 1):
            newHeights[i] = heights[i-1]
        
        for i in range(len(newHeights)):
            while stack and newHeights[i] < newHeights[stack[-1]]:

                cur = stack[-1]
                stack.pop()

                curHeight = newHeights[cur]
                leftIndex = stack[-1]
                rightIndex = i

                curWidth = rightIndex - leftIndex - 1
                res = max(res, curWidth * curHeight)
            
            stack.append(i)
        return res


                
                

        