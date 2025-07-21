class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)

        length = 0
        odd = 0
        even = 0

        for key, value in cnt.items():
            if value%2 == 0:
                odd += value/2
            else:
                if value > 1:
                    odd += math.floor(value/2)
                even += 1
        
        if even:
            length = int(odd * 2 + 1)
        else:
            length = int(odd * 2)

        return length 
        