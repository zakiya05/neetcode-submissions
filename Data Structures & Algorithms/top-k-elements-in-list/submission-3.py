class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        nums_heap=[]
        for val,freq in freq_map.items():
            heapq.heappush(nums_heap,(freq,val))
            if len(nums_heap)>k:
                heapq.heappop(nums_heap)
        return [val for freq,val in nums_heap]