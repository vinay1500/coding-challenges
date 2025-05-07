from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       l = { ")" : "(", "]" : "[", "}" : "{" }
       for i in s:
            
            if i in l:
                print("in first if")
                if stack and stack[-1] == l[i]:
                    print("in second if")
                    stack.pop()
                else:
                    print("in first else")
                    return False
            else:
                print("in second else")
                stack.append(i)
       print(f"value of i: {i},value of stack: {stack},")
       return True if not stack else False

s = Solution()
print(s.isValid("([{}])"))
print(s.isValid("[(])"))


       
'''
 print(len(s))
        if len(s)%2 != 0 :
            print("first if")
            return False
        print(len(s)/2)
        
        for i in range(int(len(s)/2)):
            if s[i] != s[-(i+1)]:
                print(s[i], s[-(i+1)])
                return False

        #print("###############")
        






        #queue = deque()

        for i in range(len(s)):
            print(f"value of i: {i}, value of s[i]: {s[i]}, value of stack:{stack}")
            if s[i] not in l:
                print("in the first if")
                stack.append(s[i])
            else:
                if stack.pop() != l[s]:
                    print(f"in the second if, value of {l[s]}")
                    #print(stack,l[s[i]])
                    return False
                else:
                    print("in the first else")
                    stack.pop()
        return True
'''

'''


            print(i)
            if s[i] in l:
                print(s[i]+"in if")
                queue.pop()
            else:
                print(s[i]+"in else")
                queue.append(s[i])



        return True
    '''