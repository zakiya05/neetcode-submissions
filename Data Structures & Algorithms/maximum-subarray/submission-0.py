class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubarray = nums[0]
        cursum=0
        for n in nums:
            if cursum <0:
                cursum=0
            cursum+=n
            maxSubarray = max(maxSubarray,cursum)
        return maxSubarray
