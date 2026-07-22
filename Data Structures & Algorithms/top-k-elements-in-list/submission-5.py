class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countr = Counter(nums)
        minH=[]
        for val,freq in countr.items():
            heapq.heappush(minH,(freq,val))
            if len(minH)>k:
                heapq.heappop(minH)
        return [val for freq,val in minH]
