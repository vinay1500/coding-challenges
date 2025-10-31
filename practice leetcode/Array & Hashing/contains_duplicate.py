List = [1,1,1,3,3,4,3,2,4,2]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        
        for n in nums:
            if n in mySet:
                return True
            mySet.add(n)
        return False
    


sol = Solution()
sol.containsDuplicate(List)