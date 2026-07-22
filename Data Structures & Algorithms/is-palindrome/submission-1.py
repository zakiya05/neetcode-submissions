class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(c.lower() for c in s if c.isalnum())
        l,r=0,len(res)-1
        while l<r:
            if res[l] == res[r]:
                l+=1
                r-=1
                continue
            else:
                return False
        return True
            
