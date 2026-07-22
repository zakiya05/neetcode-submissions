class Solution:
    def climbStairs(self, n: int) -> int:
        s1, s2 = 1,2 
        if n<= 2:
            return n
        for i in range(3, n+1):
            temp = s1+s2
            s1 = s2
            s2 = temp
        return s2