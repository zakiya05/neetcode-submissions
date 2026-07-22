class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj={i:[] for i in range(n)}
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        visit=set()
        def dfs(e,p):
            if e in visit:
                return False
            visit.add(e)
            for ne in adj[e]:
                if ne==p:
                    continue
                else:
                    if not dfs(ne,e):
                        return False
            return True
        return dfs(0,-1) and len(visit) == n