class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count = 0

        # pre = 0

        # mp = collections.defaultdict(int)

        # mp[0] = 1

        # for i in range(len(nums)):
        #     pre += nums[i]

        #     count += mp[pre-k]
        #     mp[pre] += 1
        
        # return count

        preSum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            preSum[i+1] = preSum[i] + nums[i]
        
        dic = {}

        ans = 0

        for i in range(len(preSum)):
           
            if preSum[i] - k in dic:
                ans += dic[preSum[i] - k]
            else:
                dic[preSum[i] - k] = 0
            
            if preSum[i] in dic:
                dic[preSum[i]] += 1
            else:
                 dic[preSum[i]] = 1
          
        return ans

            





        