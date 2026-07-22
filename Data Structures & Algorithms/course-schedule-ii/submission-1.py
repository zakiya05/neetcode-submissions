class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq={i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preq[course].append(pre)
        visit = set()
        cycle = set()
        output=[]
        def dfs(cor):
            if cor in cycle:
                return False
            if cor in visit:
                return True
            cycle.add(cor)
            for pre in preq[cor]:
                if not dfs(pre):
                    return False
            visit.add(cor)
            output.append(cor)
            cycle.remove(cor)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
        

