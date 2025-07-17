class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []

        digit = 0

        res = ''

        for ch in s:
            if '0' <= ch <='9':
                num = int(ch)
                digit = digit * 10 + num
            elif 'a' <= ch <= 'z':
                res += ch
            elif ch == '[':
                numStack.append(digit)
                strStack.append(res)

                digit = 0
                res = ''
            elif ch == ']':
                count = numStack.pop()
                outString = strStack.pop()
                
                for j in range(0, count):
                    outString += res
                res = outString
        return res


        