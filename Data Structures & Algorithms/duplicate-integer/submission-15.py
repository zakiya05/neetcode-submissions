class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for x in nums:
            if x in h:
                return True
            h.add(x)
        return False