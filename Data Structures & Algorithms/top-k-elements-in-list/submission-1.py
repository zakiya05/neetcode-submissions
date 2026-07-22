class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fq = Counter(nums)
        hq = []
        for num, freq in fq.items():
            heapq.heappush(hq, (freq,num))
            if len(hq) >k:
                heapq.heappop(hq)
        return [nums for freq, nums in hq]
