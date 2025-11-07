class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, index = stack.pop()
                answer[index] = (i - index)
            stack.append([t,i])
        return answer

temperatures = [73,74,75,71,69,72,76,73]
myObj = Solution()
print(myObj.dailyTemperatures(temperatures))