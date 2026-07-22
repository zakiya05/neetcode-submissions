class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        y={}
        for i in range(len(nums)):
            if nums[i] in y:
                return True
            y[nums[i]]=i
        return False
