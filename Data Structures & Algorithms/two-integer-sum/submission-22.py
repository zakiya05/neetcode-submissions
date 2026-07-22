class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[target - nums[i]] = i
        for i in range(len(nums)):
            if d.get(nums[i],-1) != -1 and d[nums[i]]!=i:
                return [i, d[nums[i]]]
        return []
        