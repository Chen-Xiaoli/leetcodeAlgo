class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        dic = {}
        preSum = 0
        maxInterval = 0

        for i in range(len(hours)):

            preSum += (1 if hours[i] > 8 else -1)

            if preSum > 0:
                maxInterval = i + 1
            else:
                if preSum not in dic:
                    dic[preSum] = i
                if preSum -1 in dic:
                    j = dic.get(preSum -1)

                    interval = i - j

                    maxInterval = max(maxInterval, interval)
        return maxInterval



        
       

            
            


                
            


