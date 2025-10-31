class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        l, r = [0]*len(height), [0] * len(height)
        l[0] = height[0]
        r[len(height)-1] = height[-1]
        for i in range(1,len(height)):
             l[i] = max(l[i-1],height[i])
        for i in range(len(height) - 2,-1,-1):
             r[i] = max(r[i+1],height[i])
        print(l,r)

        for i in range(1,len(height) - 1):
                #l = max(height[:i])
                #r = max(height[i+1 : ],)
                #print(i,l,r)

                trapped_water = min(l[i],r[i]) - height[i]
                print(trapped_water)
                print(l[i],r[i])
                if trapped_water > 0:
                     water = water + trapped_water
        return water
#height = [4,2,0,3,2,5]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
myObj = Solution()
print(myObj.trap(height))