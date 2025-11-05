from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        l, r, have, result, length, countT = 0, 0, 0, "", len(s), Counter(t)
        need = len(countT)
        countS = {}

        for r in s:
            if have == need:
                if length < min(length,r-l):
                    length = r-l
                    result = s[l:r+1]
            elif s[r] in countT.keys():
                countS[s[r]] = countS.get(s[r],0) + 1
            else:
                continue

s = "ADOBECODEBANC"
t = "ABC"
myObj = Solution()
print(myObj.minWindow(s,t))