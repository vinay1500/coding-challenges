from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxLength = 0, 0
        count = {}

        for r in range(len(s)):
            length = r - l + 1
            count[s[r]] = count.get(s[r], 0) + 1
            if length - max(count.values()) <= k:
                maxLength = max(maxLength, length)
            else:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
        return maxLength





        #    length = r - l + 1
#
        #    if s[l] == s[r]:
        #        continue
        #        #length +=1
        #    elif s[l] != s[r] and i <= k:
        #        #length += 1
        #        i += 1
        #    elif i == k:
        #        l += 1
        #    maxLength = max(maxLength, length)
        

s = "ABABBBA"
k = 2
myObj = Solution()
print(myObj.characterReplacement(s,k)) 