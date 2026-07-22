class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa=[0]*26 
        ta=[0]*26
        for i in range(len(s)):
            sa[ord(s[i])-ord('a')]+=1
        for i in range(len(t)):
            ta[ord(t[i])-ord('a')]+=1
        return sa==ta