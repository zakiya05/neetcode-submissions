class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countr = Counter(nums)
        minHeap=[]
        for val,freq in countr.items():
            heapq.heappush(minHeap,(freq,val))
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        return [val for freq,val in minHeap]