class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x={}
        for i in range(len(nums)):
            x[target - nums[i]] = i
        for i in range(len(nums)):
            
            if nums[i] in x and x[nums[i]]!=i:
                return [i,x[nums[i]]]
        return [] 
