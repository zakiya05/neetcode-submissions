class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m =len(s), len(t)
        if n!=m:
            return False
        l1=[0]*26
        l2 = [0]*26
        for i in range(n):
            l1[ord(s[i]) - ord('a')]+=1
            l2[ord(t[i]) - ord('a')]+=1
        return l1 == l2

