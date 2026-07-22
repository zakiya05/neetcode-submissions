class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x=[]
        for i in range(len(points)):
            l = -1*(points[i][0]**2 + points[i][1]**2)
            heapq.heappush(x,(l,i))
            if len(x)>k:
                heapq.heappop(x)
        return [points[i] for l,i in x ]