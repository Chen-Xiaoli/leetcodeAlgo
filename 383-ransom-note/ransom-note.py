class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dic = {}

        for ch in ransomNote:
    
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        
        for ch in magazine:
            if ch in dic:
                dic[ch] -= 1
        for key, value in dic.items():
            if value >= 1:
                return False
        return True

        