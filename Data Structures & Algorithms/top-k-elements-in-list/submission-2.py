class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freqHeap=[]
        for val,freq in c.items():
            heapq.heappush(freqHeap,(freq,val))
            if len(freqHeap)>k:
                heapq.heappop(freqHeap)
        return [val for freq, val in freqHeap]