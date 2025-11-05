from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        l, r = 0, 0
        length = len(s)
        substring = ""
        countT = Counter(t)
        #countS = Counter(s)
        print(countT)
        #print(countS)
        while r < len(s):
            print(f"in while loop {r},{l}")
            countS = {}
            r1 = r
            print(f"countS {countS}")
            while r1 < len(s):
                print(f"in second while loop l={l},r = {r1}")
                if s[r1] in countT.keys():
                    print(f"in first if condition s[r] = {s[r1]}, r = {r1}")
                    countS[s[r1]] = countS.get(s[r1],0) + 1
                if countS != countT:
                    print(f"in second if condition r = {r1},countS = {countS} , countT = {countT}")
                    r1 += 1
                else:
                    length = min(length, r1-l+1)
                    substring = s[l:r1+1]
                    print(f"in else condition length= {length} substring = {substring}")
                    break
            
            l += 1
            r += 1
        print(substring)

        return substring

s = "ADOBECODEBANC"
t = "ABC"
myObj = Solution()
print(myObj.minWindow(s,t))

#if countT != Counter(s[l:r]):
#                print(f"in first if condition{r},{l},{s[l:r]},")
#                r += 1
#            else:
#                print(f"in else condition,{r},{l},r-l{r-l},length {length}")
#                length = min(length, r - l)
#                substring = s[l:r]