class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x={}
        l=0
        maxl = 0
        for r,char in enumerate(s):
            if char in x and x[char]>=l:
                l = x[char]+1
            x[char] = r
            maxl = max(maxl, r-l+1)
        return maxl

        