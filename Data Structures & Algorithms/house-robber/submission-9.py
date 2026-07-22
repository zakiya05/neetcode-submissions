class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        x = 0
        y = 0
        for i in range( len(nums)):
            temp = max(x+nums[i] , y)
            x = y
            y = temp


        return y