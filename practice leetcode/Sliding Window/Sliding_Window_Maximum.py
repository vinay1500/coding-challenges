class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        l= 0
        result = []

        for r in range(k-1,len(nums)):
            maximum = max(nums[l:r+1])
            result.append(maximum)
            l += 1
        return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
myObj = Solution()
print(myObj.maxSlidingWindow(nums,k))