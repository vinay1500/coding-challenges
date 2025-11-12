class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        result = float("infinity")

        while l <= r:

            if nums[l] < nums[r]:
                result = min(result,nums[l])
                break
            m = (l + r) // 2
            result = min(result, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return result
#nums = [3,4,5,1,2]
#nums = [4,5,6,7,0,1,2]
nums = [11,13,15,17]
myObj = Solution()
print(myObj.findMin(nums))