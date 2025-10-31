class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0
        water = 0
        l, r = 0, len(height) -1
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water += rightMax - height[r]
        return water

#height = [4,2,0,3,2,5]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
myObj = Solution()
print(myObj.trap(height))