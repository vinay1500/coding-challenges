class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = set(nums)
        print(n)
        if len(n) != len(nums):
            return True
        return False
    
s = Solution()
t = Solution()
print(s.containsDuplicate([1,2,3,1]))
print(t.containsDuplicate([1,2,3,4]))
print(t.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))


#################################
print(f" Second Solution ")
class Solution1:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = set()
        for i in nums:
            if i in n:
                return True
            else:
                n.add(i)
        return False

s = Solution1()
t = Solution1()
print(s.containsDuplicate([1,2,3,1]))
print(t.containsDuplicate([1,2,3,4]))
print(t.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
