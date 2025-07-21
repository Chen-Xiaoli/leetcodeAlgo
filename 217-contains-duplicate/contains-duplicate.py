class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dic = {}

        # for i in range(len(nums)):
        #     if nums[i] in dic:
        #         return True 
        #     dic[nums[i]] = 0
        # return False

        pre = set()

        for num in nums:
            if num in pre:
                return True
            pre.add(num)
        return False

        