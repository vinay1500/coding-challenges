import heapq
class Solution:
    def topkFrequent(self,nums: list[int], k: int) -> list[int]:
        minHeap = []
        counter = {}
        result = []

        for n in nums:
            counter[n] = counter.get(n,0) + 1
        
        print(counter)

        for key,val in counter.items():
            heapq.heappush(minHeap,(-val,key))
        print(minHeap)
        while len(result) < k:
            result.append(heapq.heappop(minHeap)[1])
        print(result)




nums = [1,1,1,2,2,3]
k = 2
myObj = Solution()

myObj.topkFrequent(nums,k)