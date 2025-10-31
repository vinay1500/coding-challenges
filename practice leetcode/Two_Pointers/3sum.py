class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        print(nums)
        solution = []

        for n in range(len(nums)-1):

            
            if n > 0 and nums[n] == nums[n-1]:
                continue
            l, r = n+1, len(nums) - 1

            while l < r:
                

                if nums[l] + nums[r] + nums[n] < 0 :
                    l += 1
                elif nums[l] + nums[r] + nums[n] > 0 :
                    r -= 1
                else:
                    solution.append([nums[l],nums[r],nums[n]])
                    l +=1

                    while l < r and nums[l] == nums[l-1]:
                        l +=1 
            print(l,r,n)
        return solution



nums = [-1,0,1,2,-1,-4]
myObj =  Solution()
print(myObj.threeSum(nums))