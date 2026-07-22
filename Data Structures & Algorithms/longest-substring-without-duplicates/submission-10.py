class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x={}
        i,j=0,0
        maxl=0
        while j<len(s):
            if x.get(s[j],-1) >=i:
                i= x[s[j]]+1
            
            x[s[j]] = j
            maxl = max(maxl,j-i+1)
            j+=1
        return maxl