class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            h[target- nums[i]]=i
        for i in range(len(nums)):
            if h.get(nums[i],-1) != -1 and h[nums[i]]!=i:
                return [i,h[nums[i]]]
        return []

