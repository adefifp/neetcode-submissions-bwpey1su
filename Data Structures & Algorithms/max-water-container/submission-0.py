class Solution:
    def maxArea(self, heights: List[int]) -> int:
       ans = 0
       count = 0
       l = 0
       r = len(heights) - 1
       while l < r:
        count = min(heights[l], heights[r]) * (r - l)
        ans = max(count, ans)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
       return ans