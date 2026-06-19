class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # cap = 0
        # l, r = 0, len(heights)-1
        # while l < r:
        #     width = r - l
        #     height = min(heights[l],heights[r])
        #     cap = max(width*height,cap)
        #     if heights[l] < heights[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return cap

        max_cap = 0
        l, r = 0, len(heights) -1 
        
        while l < r:
            max_cap = max(max_cap, (r-l) * min(heights[l],heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return max_cap