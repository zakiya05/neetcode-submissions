class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res =0
        f=0 
        l,r=0,0
        m={}
        while r<len(s):
            m[s[r]] = 1+ m.get(s[r],0)
            f = max(f,m[s[r]])
            while (r-l+1) - f >k:
                m[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
            r+=1
        return res