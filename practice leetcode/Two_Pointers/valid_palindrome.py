class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ""
        for c in s:
            if c.isalnum():
                clean_string +=c.lower()
        length = len(clean_string)

        for i in range(int(length//2)):
            if clean_string[i] != clean_string[length -1 -i]:
                return False
        return True
             
myObj = Solution()
print(myObj.isPalindrome("Was it a car or a cat I saw?"))