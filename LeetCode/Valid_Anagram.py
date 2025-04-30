class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}

        for i in range(len(s)):
            d1[s[i]] = 1 + d1.setdefault(s[i],0)
            d2[t[i]] = 1 + d2.setdefault(t[i],0)
        print(d1)
        print(d2)
        for i in d1:
            #print(i,d1[i],d2[i])
            if d1[i] != d2.get(i,0):
                #print(d1[i],d2[i])
                return False
        return True

a = Solution()
b = Solution()
x= a.isAnagram("anagram","nagaram")
y= b.isAnagram("rat","car")
print(x)
print(y)