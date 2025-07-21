class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dic = {}

        for i, ch in enumerate(s):
            if ch not in dic:
                dic[ch] = i
            else:
                dic[ch] = -1
        
        for key, value in dic.items():
            if value != -1:
                return  value
        return -1
        
