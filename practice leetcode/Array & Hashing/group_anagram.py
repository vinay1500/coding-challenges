from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-97] += 1
            res[tuple(count)].append(s)
        return res.values()


       
strs = ["eat","tea","tan","ate","nat","bat"]
myObj = Solution()
print(myObj.groupAnagrams(strs))
# dii = defaultdict[list]
#        for word in strs:
#            dii[word] = "".join(word)