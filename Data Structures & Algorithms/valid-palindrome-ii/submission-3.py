class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        def isPalindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return isPalindrome(i+1,j) or isPalindrome(i,j-1)

        return True