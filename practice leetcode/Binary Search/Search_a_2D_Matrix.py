class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        row = 0

        while row <= len(matrix) - 1:
            l, r = 0, len(matrix[row]) - 1

            if target < matrix[row][r]:
                middle = (l+r)//2
                if matrix[row][middle] > target:
                    r = middle -1
                elif matrix[row][middle] < target:
                    l = middle + 1
                else:
                    return True
            row += 1
        return False


#matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
#target = 13
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3    
myObj = Solution()
print(myObj.searchMatrix(matrix,target))
