class NumArray:

    def __init__(self, nums: List[int]):
        self.stack = nums
        

    def sumRange(self, left: int, right: int) -> int:
        temp = self.stack[left:right+1]

        res = 0

        for num in temp:
            res += num
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)