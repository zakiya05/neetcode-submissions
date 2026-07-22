class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        nums.sort()
        gm, lm=0,0
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                lm+=1
            elif nums[i] == nums[i-1]:
                continue
            else:
                gm = max(gm,lm)
                lm=0
            
        return max(gm,lm)+1
