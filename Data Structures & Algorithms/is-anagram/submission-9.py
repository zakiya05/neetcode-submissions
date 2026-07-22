class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*26
        b = [0]*26
        for c in s:
            a[ord(c)-ord('a')]+=1
        for c in t:
            b[ord(c)-ord('a')]+=1
        return a ==b