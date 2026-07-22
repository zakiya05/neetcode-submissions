class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        m = len(nums)//2
        return nums[m]