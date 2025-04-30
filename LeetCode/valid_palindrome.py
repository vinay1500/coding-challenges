class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        print(s)
        for i in range(int(len(s)/2)):
            print(i,s[i],s[-(i+1)])
            if s[i] != s[-(i+1)]:
                return False
        return True


s = Solution()
print(s.isPalindrome("Was it a car or a cat I saw?"))
print(s.isPalindrome("tab a cat"))