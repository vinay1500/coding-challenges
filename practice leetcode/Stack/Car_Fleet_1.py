class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        fleet = 0
        max_time = 0.0

        for p, s in sorted(zip(position, speed), reverse= True):
            t = (target - p) / s
            if t > max_time:
                fleet += 1
                max_time = t
        return fleet

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
myObj = Solution()
print(myObj.carFleet(target,position,speed)) 