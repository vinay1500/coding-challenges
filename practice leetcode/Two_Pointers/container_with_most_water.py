class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)

            if height[l] < height[r]:
                l +=1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return res


height = [1,1]
#height = [1,8,6,2,5,4,8,3,7]
myObj = Solution()
print(myObj.maxArea(height))