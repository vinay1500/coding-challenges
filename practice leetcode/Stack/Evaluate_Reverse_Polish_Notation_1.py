import operator

from numpy import floor


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = ['+','-','*','/']

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                x = stack.pop()
                y = stack.pop()
                if i == '+':
                    result = y+x
                elif i == '-':
                    result = y - x
                elif i == '*':
                    result = y * x
                else:
                    result = int(y/x)         
                stack.append(result)
        return stack[0]

tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#tokens = ["2","1","+","3","*"]
myObj = Solution()
print(myObj.evalRPN(tokens))