class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[]
        def dfs(s, opened, closed):
            if opened == closed == n:
                res.append(s)
                return
           
            if closed < opened:
                if opened < n:
                    dfs(s+"(" , opened+1, closed)
                dfs(s+")",opened , closed+1)
            else:
                dfs(s+"(",opened+1, closed)

        dfs("",0,0)
        return res
            

