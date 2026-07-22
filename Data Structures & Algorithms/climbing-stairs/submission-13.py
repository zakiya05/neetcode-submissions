class Solution:
    def climbStairs(self, n: int) -> int:
        ''' 
        so we are given an n and we start from step 0 , 
        we can take 1 step or 2 steps from where we are
        here we need to return the number of distint steps 
        at each step we have option of taking 1 or 2 

        lets start with example 
        so we have 
        n= 1 1 way 
         1
        n = 2 2ways
        1+1
        2
        n= 3 3 ways
        1+1+1
        1+2
        2+1
        
        n= 4  5 
        1+1+1+1+1
        1+1+2
        1+2+1
        2+1+1
        2+2

        n = 5 8
        1+1+1+1+1
        1+1+1+2
        2+1+1+1
        1+2+1+1
        1+1+2+1
        1+2+2
        2+1+2
        2+2+1
         
        '''
        if n<=2:
            return n
        dp=[0]*(n+1)
        dp[1]= 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]

