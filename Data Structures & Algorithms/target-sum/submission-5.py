class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def dfs(cursum, index):
            if index == len(nums):
                return 1 if cursum == target else 0
            if (index,cursum) in dp:
                return dp[(index,cursum)]

            dp[(index,cursum)] =  (dfs(cursum+nums[index], index+1)+ dfs(cursum - nums[index], index+1))
            return dp[(index,cursum)]
        
        
        return dfs(0,0)