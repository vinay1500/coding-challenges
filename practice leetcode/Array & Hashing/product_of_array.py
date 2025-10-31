class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = [1] * n
        j = 0

        for i,num in enumerate(nums):
            print(i,num)
            if j != i:
                arr.append(num*arr[i])
                print(arr)
            else:
                arr.append(num)
            j +=1
        return arr

 
nums = [1,2,3,4]
myObj = Solution()
print(myObj.productExceptSelf(nums))