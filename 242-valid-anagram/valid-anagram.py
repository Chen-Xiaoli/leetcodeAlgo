class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}

        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1

        dic1 = {}

        for ch in t:
            if ch not in dic1:
                dic1[ch] = 1
            else:
                dic1[ch] += 1
        
        for key, value in dic.items():
            if key in dic1 and value == dic1[key]:
                continue
            else:
                return False
        return True
