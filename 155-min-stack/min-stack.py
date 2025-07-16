class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self. min_stack:
           top = self.min_stack[-1]
           if val <= top:
            self.min_stack.append(val)
        else:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        if not self.is_empty():
            if self.min_stack[-1] == self.stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()
        else:
            raise IndexError('stack is empty')
        

    def top(self) -> int:
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError('stack is empty')
        

    def getMin(self) -> int:
        return self.min_stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()