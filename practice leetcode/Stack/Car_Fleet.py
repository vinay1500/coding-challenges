class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        array = []

        for p, s in zip(position,speed):
            array.append([p,s])

        stack = []
        #print(array)

        array = sorted(array, reverse=True)
        #print(array)
        for p,s in array:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
myObj = Solution()
print(myObj.carFleet(target,position,speed)) 