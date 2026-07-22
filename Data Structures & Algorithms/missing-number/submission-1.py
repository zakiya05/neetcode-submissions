class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        total = x*(x+1)
        total = int(total/2)
        for i in nums:
            total -= i
        return total