class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        x1 = [0]*26
        x2 = [0]*26

        for c in s1:
            x1[ord(c)-ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            x2[ord(s2[r])-ord('a')] += 1

            if r - l + 1 > len(s1):
                x2[ord(s2[l])-ord('a')] -= 1
                l += 1

            if x1 == x2:
                return True

        return False