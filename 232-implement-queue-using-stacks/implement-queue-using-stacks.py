class MyQueue:

    def __init__(self):

        self.stack = []
        self.stackOut = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        try:
            return self.stack.pop(0)
        except:
            raise IndexError('quque empty')
        
            
    def peek(self) -> int:
         try:
            return self.stack[0]
         except:
            raise IndexError('quque empty')

    def empty(self) -> bool:
        if len(self.stack):
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()