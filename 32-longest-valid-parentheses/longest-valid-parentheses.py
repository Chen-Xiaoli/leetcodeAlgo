class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = list()
        maxLength = 0

        start = 0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                if not stack:
                    start = i+1
                else:
                    stack.pop()
                    if not stack:
                        maxLength = max(maxLength, i - start + 1)
                    else:
                        maxLength = max(maxLength, i - (stack[-1] + 1) + 1)
        return maxLength   
                
        