from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r, matches = 0, len(s1), 0
        countS1 = Counter(s1)
        countS2 = Counter(s2)
        print(countS1)
        print(countS2)


        while r <= len(s2):
            if countS1 != Counter(s2[l:r]):
                l += 1
                r += 1
            else:
                return True
        return False
s1 = "ab"
s2 = "eidbaooo"
myObj = Solution()
print(myObj.checkInclusion(s1,s2))