class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subSet = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in subSet:
                subSet.remove(s[l])
                l += 1
            subSet.add(s[r])
            maxLength = max(maxLength, r-l+1)
        return maxLength
    
    
    #    length = 0
    #    maxSubstring = ""
    #    l, r = 0, 0
#
    #    while r < len(s):
#
    #        substring = ""
    #        subSet = set()
#
    #        while s[r] in subSet:
    #                subSet.remove(s[l])
    #                l += 1
#
    #        #if s[l] != s[r]:
    #        subSet.add(s[r])
    #        substring += s[r]
    #        maxSubstring = max(maxSubstring, substring)
    #            
    #        r += 1
    #    return maxSubstring


s = "abcabcbb"            
myObj = Solution()
print(myObj.lengthOfLongestSubstring(s))