class Solution:
    def maxArea(self, heights: List[int]) -> int:
        len_heights = len(heights)
        start = 0
        end = len_heights - 1
        max_area = 0

        while(start < end):
            curr_area = (end - start)*min(heights[start], heights[end])
            if(max_area < curr_area):
                max_area = curr_area
            if(heights[start] <= heights[end]):
                start = start + 1
            else:
                end = end - 1
        
        return max_area