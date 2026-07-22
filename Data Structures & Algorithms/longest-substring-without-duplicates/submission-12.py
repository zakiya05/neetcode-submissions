class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i,j=0,0
        x={}
        while j<len(s):
            if s[j] in x and x[s[j]]>=i:
                i=x[s[j]]+1
            else:
                res = max(res,j-i+1)
            
            x[s[j]]= j 
            j+=1

        return res
                

