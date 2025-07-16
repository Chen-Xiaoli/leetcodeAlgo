class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []

        for token in tokens:
           try:
            result.append(int(token))
           except:
            num1 = result.pop()
            num2 = result.pop()
            result.append(self.evaluate(num1, num2, token))
        
        return result.pop()
    def evaluate(self, num1, num2, op):
        if op == '+':
            return num2 + num1
        if op == '-':
            return num2 - num1
        if op == '*':
            return num2 * num1
        if op == '/':
            return int(num2/num1)
    

        