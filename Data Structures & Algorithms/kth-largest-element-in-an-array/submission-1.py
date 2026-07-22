class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x=[]
        for i in range(len(nums)):
            heapq.heappush(x,nums[i])
            if len(x)>k:
                heapq.heappop(x)
        return x[0]