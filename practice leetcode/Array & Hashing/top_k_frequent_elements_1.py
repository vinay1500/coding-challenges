import heapq
class Solution:
    def topkFrequent(self,nums: list[int], k: int) -> list[int]:
        counter = {}
        freq = [[] for i in range(len(nums) +1)]
        result = []

        for n in nums:
            counter[n] = counter.get(n,0) + 1
        
        print(counter)

        for key,val in counter.items():
            freq[val].append(key)
        
        print(freq)

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result



nums = [1,1,1,2,2,3]
k = 2
myObj = Solution()

myObj.topkFrequent(nums,k)