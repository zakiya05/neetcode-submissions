class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[0]*26
        b=[0]*26
        for n in s:
            a[ord(n) - ord('a')]+=1
        for x in t:
            b[ord(x)-ord('a')]+=1
        return a==b