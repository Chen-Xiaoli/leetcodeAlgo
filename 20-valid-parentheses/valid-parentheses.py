class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []

        for item in s:
            if item == '(' or item == '[' or item == '{':
                stack.append(item)
            else:
                if not stack:
                    return False
                top = stack[-1]   
                if (top == '(' and item == ')') or (top == '[' and item == ']') or (top == '{' and item == '}'):
                    stack.pop()
                else:
                    return False
        return not stack
                

        