class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # BRUTE FORCE SOLN

        # maxArea = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j - i)
        #         if (area > maxArea):
        #             maxArea = area
        
        # return maxArea

        i = 0
        j = len(heights) - 1
        maxArea = 0
        while j > 0 and i < len(heights) - 1:
            # print(i, j)
            maxArea = max(min(heights[i], heights[j]) * abs(j-i), maxArea)
            # j_loss = heights[j] - heights[j-1]
            # i_loss = heights[i] - heights[i+1]
            # if j_loss == i_loss:
            #     if heights[j] < heights[i]:
            #         j -= 1
            #     else:
            #         i += 1
            # elif j_loss > i_loss:
            #     i += 1
            # else:
            #     j -= 1

            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
        


        return maxArea


