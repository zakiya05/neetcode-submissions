class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i,n in enumerate(nums):
            h[target-n] = i
        for i,n in enumerate(nums):
            if n in h and i!=h[n]:
                return [i,h[n]]
        return []

