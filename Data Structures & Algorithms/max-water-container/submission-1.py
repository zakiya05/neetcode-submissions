class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater =0 
        l,r=0,len(heights)-1
        while l<r:
            lm = min(heights[r], heights[l])*(r-l)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            maxwater= max(lm,maxwater)
        return maxwater
