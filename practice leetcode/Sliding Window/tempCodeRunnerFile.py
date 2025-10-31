class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxLength, i = 0, 0, 0
        count = {}
        

        for r in range(len(s)):
            length = r - l + 1
            count[s[r]] = count.get(s[r], 0) + 1
            if length - max(count.values()) <= k:
                maxLength = max(maxLength, length)
            else:
                count[s[l]] = count.get(s[l],0) - 1
                l += 1
        return maxLength

