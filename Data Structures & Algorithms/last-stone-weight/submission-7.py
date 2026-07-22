class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            h1 = heapq.heappop(stones)
            h2 = heapq.heappop(stones)
            if h2 - h1 > 0:
                heapq.heappush(stones, h1-h2)
        if stones:
            return -1*stones[0]
        else:
            return 0