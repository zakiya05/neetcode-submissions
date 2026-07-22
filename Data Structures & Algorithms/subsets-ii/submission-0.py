class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(i, cur):
            if i==len(nums):
                res.add(tuple(cur))
                return 
            cur.append(nums[i])
            dfs(i+1,cur)
            cur.pop()
            dfs(i+1,cur)
        nums.sort()
        dfs(0,[])
        return [list(p) for p in res]