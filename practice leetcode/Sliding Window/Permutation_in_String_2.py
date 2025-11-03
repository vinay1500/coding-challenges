class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countS1, countS2 = [0] * 26, [0] * 26
        l, matches = 0, 0

        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
        for i in range(len(s1)):
            countS2[ord(s2[i]) - ord('a')] += 1
        #print(countS1)
        #print(countS2)
        #count = len(list(set(countS1) & set(countS2)))
        #print(count)
        #matches = matches - count
        #print(matches)

        for i in range(26):
            if countS1[i] == countS2[i]:
                matches += 1

        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            countS2[index] += 1
            if countS1[index] == countS2[index]:
                matches += 1
            elif countS1[index] + 1 == countS2[index]:
                matches -= 1
            

            index = ord(s2[l]) - ord('a')
            countS2[index] -= 1
            if countS1[index] == countS2[index]:
                matches += 1
            elif countS1[index] - 1 == countS2[index]:
                matches -= 1
            l += 1
        return matches == 26



           


s1 = "ab"
s2 = "eidboaoo"
myObj = Solution()
print(myObj.checkInclusion(s1,s2))