class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1 or n==2:
            return n
        if n<1:
            return 0
        return self.climbStairs(n-1)+ self.climbStairs(n-2)
       
        