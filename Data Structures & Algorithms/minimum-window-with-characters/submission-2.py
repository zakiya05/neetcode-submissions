class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT={}
        for c in t:
            countT[c]=1+countT.get(c,0)
        window={}
        l,res,reslen=0,[-1,-1],float("infinity")
        l,have,need=0,0,len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c]=1+window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have+=1
            while have == need:
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                if (r-l+1)<=reslen:
                    reslen=r-l+1
                    res=[l,r]
                    
                l+=1
        l,r = res
        return s[l:r+1] if reslen!=float("infinity") else ""
