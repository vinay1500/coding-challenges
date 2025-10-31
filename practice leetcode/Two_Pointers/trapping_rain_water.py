class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0

        for i in range(1,len(height) - 1):
                l = max(height[:i])
                r = max(height[i+1 : ],)
                #print(i,l,r)

                trapped_water = min(l,r) - height[i]
                if trapped_water > 0:
                     water = water + trapped_water
        return water
#height = [4,2,0,3,2,5]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
myObj = Solution()
print(myObj.trap(height))