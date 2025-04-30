class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        

        d ={}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in d:
                return[d[complement],i]
            d[n] = i
        
        #print(d)
# in the below way we have to check the index of each as if we 
# insert all value in the hashmap then it will take the index of the 
# nums twice so we have to check if its not the same and they are two
# different elemnets...
        #for i in d:
            #print(i,d[i])
        #    if target-i in d:
        #        return print(d[i],d[target-i])

       # for i in range(len(nums)):
       #     if nums[i]+nums[-(i+1)]


s = Solution()
print(s.twoSum([2,7,11,15],9))
print(s.twoSum([3,2,4],6))
print(s.twoSum([3,3],6))