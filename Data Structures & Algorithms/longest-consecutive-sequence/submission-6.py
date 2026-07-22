class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        for i in range(len(nums)):
            s.add(nums[i])
        max_len=0
        for i in range(len(nums)):
            if nums[i]-1 not in s:
                x=1
                while nums[i]+x in s:
                    x+=1
                max_len=max(max_len, x)
        return max_len
                    