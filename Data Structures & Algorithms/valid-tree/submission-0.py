class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj ={i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit=set()
        def dfs(node,parent):
            if node in visit:
                return False

            visit.add(node)
            for ni in adj[node]:
                if ni == parent:
                    continue
                else:
                    if not dfs(ni,node):
                        return False
            return True
        return dfs(0,-1) and len(visit)==n

        