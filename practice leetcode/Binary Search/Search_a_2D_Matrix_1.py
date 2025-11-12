class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        lo, hi = 0, rows * cols - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            r, c = divmod(mid, cols)
            val = matrix[r][c]
            if val == target:
                return True
            if val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


#matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
#target = 13
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
myObj = Solution()
print(myObj.searchMatrix(matrix,target))
#searchMatrix(matrix,target)