class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        maxw = 0
        while l<r:
            if heights[l] > heights[r]:
                maxw = max((r-l)*heights[r], maxw)
                r-=1
            else:
                maxw = max((r-l)*heights[l], maxw)
                l+=1
        return maxw
