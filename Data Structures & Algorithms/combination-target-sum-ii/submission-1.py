class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(total, i, cur):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i>=len(nums):
                return 
            cur.append(nums[i])
            dfs(total+nums[i],i+1,cur)
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(total,i+1,cur)
        dfs(0,0,[])
        return res


        