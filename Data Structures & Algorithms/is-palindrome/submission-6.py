class Solution:
    def isPalindrome(self, s: str) -> bool:
        y=""
        z=""
        s= s.lower()
        for i in s:
            if i.isalnum():
                y = i+y
                z= z+i
            else:
                continue
        print(y)
        return y==z

