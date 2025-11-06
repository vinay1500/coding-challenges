class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       brackets = { ")":"(","}":"{","]":"["}
       #counter = 0

       for c in s:
           print(stack)
           if c in brackets:
            if stack and stack[-1] == brackets[c]:
               stack.pop()
               #counter -= 1
            else:
               return False
           else:
               stack.append(c)
               #counter += 1
       return True if not stack else False

s = "()"
myObj = Solution()
print(myObj.isValid(s))