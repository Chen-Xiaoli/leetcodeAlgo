class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0

        for item in s:
            if item == '(':
                depth += 1
            elif item == ')':
                if max_depth <= depth:
                    max_depth = depth
                depth -= 1
        return max_depth

