class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        l,r= 0,0
        n = len(s)
        m={}
        while r<n:
            if s[r] in m:
                l = max(l,m[s[r]])
            m[s[r]]=r+ 1            
            res = max(res,r-l+1)
            r+=1
        return res