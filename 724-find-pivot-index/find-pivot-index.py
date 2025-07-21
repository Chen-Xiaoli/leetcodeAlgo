class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        preSum = [0] * (len(nums) + 1)

        for i, num in enumerate(nums):
            preSum[i+1] = preSum[i] + num
        
        print(preSum)
        
        for i in range(1, len(preSum)):
            print(preSum[-1] - preSum[i])
            if preSum[-1] - preSum[i] == preSum[i-1]:
                return i-1
        return -1


        