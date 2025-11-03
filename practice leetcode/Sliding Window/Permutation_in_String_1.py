# brainstormig for solving it in O(n) time

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r, matches = 1, len(s1)+1, 26
        countS1 = Counter(s1)
        countS2 = Counter(s2[0:2])
        print(countS1)
        print(countS2)
        print(len(countS1&countS2))
        matches = matches - len(countS1&countS2)
        #for i in range(r):
        #    print(i,countS1[i],countS2[i])
        #    if countS1[i] == countS2[i]:
        #        matches += 1
        print(matches)


        while r <= len(s2):
            countS2[s2[l]] = countS2.get(l,0) - 1
            countS2[s2[r]] = countS2.get(r,0) + 1
            print(countS2[s2[l-1]],countS2[s2[r]])
            if countS2[s2[l-1]].value() == countS1.get(l-1,0):
                matches += 1
            if countS2[s2[r]].value() == countS1.get(r,0):
                matches += 1

            if matches == 26:
                return True
        return False
s1 = "abc"
s2 = "baxyzabc"
myObj = Solution()
print(myObj.checkInclusion(s1,s2))