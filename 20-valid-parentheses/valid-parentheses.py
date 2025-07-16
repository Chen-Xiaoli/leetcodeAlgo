class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if item == '(' or item == '[' or item == '{':
                stack.append(item)
            elif item == ')':
                if len(stack) and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif item == ']':
                if len(stack) and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif item == '}':
                if len(stack) and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if len(stack):
            return False
        return True
                

        