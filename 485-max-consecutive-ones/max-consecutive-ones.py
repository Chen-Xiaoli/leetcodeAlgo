class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = 0
        count = 0

        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                maxLen = max(maxLen, count)
                count = 0
        maxLen = max(maxLen, count)
        return maxLen
        