class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fq = Counter(nums)

        h=[]
        for key , val in fq.items():
            if len(h) <k:
                heapq.heappush(h, (val,key))
            else:
                heapq.heappushpop(h,(val,key))
        return [i[1] for i in h]