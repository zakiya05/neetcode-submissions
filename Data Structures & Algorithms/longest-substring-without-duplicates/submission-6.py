class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        mp={}
        for r in range(len(s)):
            if s[r] in mp:
                l = max(l,mp[s[r]])
            mp[s[r]] = r +1
            res = max(res, r - l +1)
        return res