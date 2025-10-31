class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}

        for n in s:
            dict1[n] = dict1.get(n,0)+1
        
        for n in t:
            dict2[n] = dict2.get(n,0)+1
        
        return dict1 == dict2
    
s = "car"
t = "rat"

myObj = Solution()
print(myObj.isAnagram(s,t))