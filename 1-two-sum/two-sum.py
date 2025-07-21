class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        map = dict()

        for i, num in enumerate(nums):

            anotherNum = target - nums[i]

            if anotherNum in map:
                return [map[anotherNum], i]
            else:
                map[nums[i]] = i
        return []