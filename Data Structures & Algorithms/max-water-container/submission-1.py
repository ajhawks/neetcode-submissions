class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        v = max(0, (r-l) * min(heights[l], heights[r]))
        while r > l:
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
            v = max(v, (r-l) * min(heights[l], heights[r]))
        return v
