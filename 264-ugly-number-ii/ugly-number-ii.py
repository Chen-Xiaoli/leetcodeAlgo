class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]

        seen = {1}
        pq = [1]

        for i in range(n-1):

            curr = heapq.heappop(pq)

         

            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(pq, nxt)
                    
        return heapq.heappop(pq)

