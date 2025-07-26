from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = list()
        result = 0
        n = len(height)

        for i, h in enumerate(height):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
                if stack:
                    h = min(height[stack[-1]], height[i]) - height[bottom]
                    w = i - stack[-1] - 1
                    result += w * h
            stack.append(i)
        return result


        
        