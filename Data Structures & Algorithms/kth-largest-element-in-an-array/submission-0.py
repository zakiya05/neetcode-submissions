class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mp =[]
        for i in range(len(nums)):
            heapq.heappush(mp,nums[i])
            if len(mp) > k:
                heapq.heappop(mp)
        return mp[0]        