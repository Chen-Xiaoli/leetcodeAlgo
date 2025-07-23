class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        dic = collections.defaultdict(list)

        maxDegree = 0
        minLen = 0
   

        for i, num in enumerate(nums):
            if num not in dic:
                count = 1
                start = i
                end = i
                dic[num] = [count, start, end]
            else:
                dic[num][0] += 1
                dic[num][2] = i
            

        for count, left, right in dic.values():
            if maxDegree < count:
                maxDegree = count
                minLen = right - left + 1
            elif maxDegree == count:
                if minLen > (right-left+1):
                    minLen = right-left+1
        return minLen

        