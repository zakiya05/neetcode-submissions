class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml =0
        d={}
        l,r=0,0
        while r<len(s):
            if s[r] in d:
                l = max(l,d[s[r]])
            d[s[r]] = r+1
            ml = max(ml, r-l+1)
            r+=1
        return ml