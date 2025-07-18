class MyCircularDeque:

    def __init__(self, k: int):

        self.capacity = k + 1
        self.arr = [0] * self.capacity

        self.front = 0
        self.rear = 0
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = value
        return True

        

    def insertLast(self, value: int) -> bool:
         if self.isFull():
            return False
         self.arr[self.rear] = value
         self.rear = (self.rear + 1) % self.capacity
         return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True
        

    def getFront(self) -> int:

        if self.isEmpty():
            return -1
        return self.arr[self.front]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]
        

    def isEmpty(self) -> bool:
        return self.front == self.rear
        

    def isFull(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()