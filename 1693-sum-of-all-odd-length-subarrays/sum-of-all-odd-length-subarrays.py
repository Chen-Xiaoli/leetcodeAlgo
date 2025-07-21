class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # ans = 0

        # preSum = [0] * (len(arr) + 1)

        # for i in range(len(arr)):
        #     preSum[i+1] = preSum[i] + arr[i]
        
        # for i in range(len(arr)):
        #     for j in range(1, len(arr)+1, 2):
        #         if i+j-1 < len(arr):
        #             ans += preSum[i + j] - preSum[i]
                    
        # return ans

        n = len(arr)
        ans = 0
        for i, num in enumerate(arr):
            total = ((i + 1) * (n - i) + 1) // 2
            ans += num * total
        return ans


     




        