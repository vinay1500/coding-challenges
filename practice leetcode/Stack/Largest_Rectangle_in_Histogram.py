#Largest_Rectangle_in_Histogram.py
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_Area = 0
        stack = []

        for i, h in enumerate(heights):
            #if stack or stack[-1][1] < h:
            #    stack.append([i,h])
            start_index = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                max_Area = max(max_Area, width*height)
                start_index = index
            stack.append([start_index,h])
        for i, h in stack:
            width = len(heights) - i
            max_Area = max(max_Area,width*h)
        return max_Area

heights = [2,1,5,6,2,3]    
myObj = Solution()
print(myObj.largestRectangleArea(heights))
