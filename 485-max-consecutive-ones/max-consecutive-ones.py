class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = 0
        lastZero = -1
        for i, num in enumerate(nums):
            if num == 0:
                lastZero = i
            else:
                maxLen = max(maxLen, i - lastZero)
        return maxLen
        