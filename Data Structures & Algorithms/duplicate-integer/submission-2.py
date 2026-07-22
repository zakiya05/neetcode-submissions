class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s={}
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s[nums[i]]=i
        return False