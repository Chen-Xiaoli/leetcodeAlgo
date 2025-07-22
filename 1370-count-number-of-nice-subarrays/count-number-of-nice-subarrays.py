class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        ans = 0

        preSum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            preSum[i+1] = preSum[i] + (nums[i] % 2)
        
        count = [0] * (len(preSum))

        for i in range(len(preSum)):
            if preSum[i] - k >= 0:
                ans += count[preSum[i] - k]
            
            count[preSum[i]] += 1
        print(preSum)
        print(count)
        return ans



