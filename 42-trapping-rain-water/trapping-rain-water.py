class Solution:
    def trap(self, height: List[int]) -> int:
        stack = list()

        result = 0

        n = len(height)

        for i, h in enumerate(height):
            if not stack:
                stack.append(i)

            elif height[i] <= height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:
                    bottom = stack[-1]
                    stack.pop()
                    if stack:
                        h = min(height[stack[-1]], height[i]) - height[bottom]
                        w = i - stack[-1] - 1
                        result += w * h
            stack.append(i)
        return result


        
        