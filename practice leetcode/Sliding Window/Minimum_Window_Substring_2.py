class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        l, result, length, countT, window = 0, [-1, -1], float("infinity"), {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        have, need = 0, len(countT)
        

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < length:
                    result = [l, r]
                    length = (r - l + 1)

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = result
        return s[l:r+1] if length != float("infinity") else ""
s = "ADOBECODEBANC"
t = "ABC"
myObj = Solution()
print(myObj.minWindow(s,t))