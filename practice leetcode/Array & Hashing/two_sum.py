class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) < 2:
            return
        nums = sorted(nums)
        l = len(nums) -1
        i=0
        while(l+1 > 1):
            if nums[i]+nums[l] < target:
                i +=1
            elif nums[i]+nums[l] > target:
                l -=1
            else:
                return [i,l]
            l-=1
nums = [2,7,11,15]
target = 9
myObj = Solution()
print(myObj.twoSum(nums,target))
        