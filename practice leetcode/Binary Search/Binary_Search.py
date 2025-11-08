class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = int((l + r) / 2)

            if nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
            else:
                return middle
            #elif nums[middle] == target:
            #    return middle
        return -1
nums = [-1,0,3,5,9,12]
#nums = [-1,0,3,5,9,12]
target = 2
myObj = Solution()
print(myObj.search(nums,target))