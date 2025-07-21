class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        map1 = dict()
        value = dict()
        
        for i in range(len(s)):
            input1 = s[i]
            input2 = t[i]

            if input1 in map1 and map1[input1] != input2:
                return False
            elif input2 in value and value[input2] != input1:
                return False

            map1[input1] = input2
            value[input2] = input1

        return True
            
