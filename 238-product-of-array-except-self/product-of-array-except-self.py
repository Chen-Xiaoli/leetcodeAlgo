class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [1] * len(nums)
      
        # left = [1] * len(nums)
        # right = [1] * len(nums)

        # for i in range(1, len(nums)):
        #     left[i] = left[i-1] * nums[i-1]

        # for i in range(len(nums)-2, -1, -1):
        #     right[i] = right[i+1] * nums[i+1]

        # for i in range(len(nums)):
        #     ans.append(left[i] * right[i]) 

        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]

        right = 1

        for i in range(len(nums)-1, -1, -1):

            ans[i] = ans[i] * right
            right *= nums[i]

        return ans
            







        