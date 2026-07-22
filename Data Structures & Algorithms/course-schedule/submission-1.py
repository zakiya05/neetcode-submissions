class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses<=0:
            return True
        preq_map={i:[] for i in range(numCourses)}

        for cor,preq in prerequisites:
            preq_map[cor].append(preq)
        visit=set()
        def dfs(cor):
            if cor in visit:
                return False
            if preq_map[cor]==[]:
                return True
            visit.add(cor)
            for p in preq_map[cor]:
                if not dfs(p):
                    return False
            visit.remove(cor)
            preq_map[cor]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True