class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)

        length = 0

        for key, value in cnt.items():
            if value%2 == 0:
                length += value
            else:
                length += value - 1
                cnt[key] = 1
        
        return length + 1 if 1 in cnt.values() else length
        