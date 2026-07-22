class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0] or 0 
    
       
        x = nums[0]
        y = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = max(y, nums[i]+x)
            x = y 
            y = temp 

        return y

