class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two ptrs:
        i = 0
        j = len(heights) -1 
        maxa = 0
        while i < j:
            print(i, j)
            area = (j - i) * min(heights[i], heights[j])
            if area > maxa:
                maxa = area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
        return maxa