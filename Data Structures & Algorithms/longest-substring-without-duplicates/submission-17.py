class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        maxLen=0
        l=0
        for i in range(len(s)):
            if s[i] in mp:
                l = max(l,mp[s[i]]+1)
            mp[s[i]] = i
            maxLen = max(maxLen, i-l+1)
        return maxLen

