class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            h[target - nums[i]]=i
        
        for i in range(len(nums)):
            if nums[i] in h and h[nums[i]]!=i:
                return [i, h[nums[i]]]
        return 0