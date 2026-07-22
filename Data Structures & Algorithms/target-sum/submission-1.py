class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(cursum, index):
            if index == len(nums):
                return cursum == target 
            return (dfs(cursum+nums[index], index+1)+ dfs(cursum - nums[index], index+1) )   
        
        return dfs(0,0)