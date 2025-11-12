import math
from numpy import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
       # n = max(piles)
       # r = []
       # for i in range(1,n+1):
       #     r.append(i)
        min_k = max(piles)

        l, r = 1, max(piles)
        while l <= r:
            v = 0
            k = (l + r) // 2
            for p in piles:
                v += math.ceil(p/k)
            
            if v <= h:
                min_k = min(min_k, k)
                r = k - 1

            else:
                l = k + 1
        return min_k




piles = [3,6,7,11]
h = 8
myObj = Solution()
print(myObj.minEatingSpeed(piles,h))