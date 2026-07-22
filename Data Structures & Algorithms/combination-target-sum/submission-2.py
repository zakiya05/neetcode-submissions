class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        def recursive(i, currentList, total):
            if target == total:
                res.append(currentList.copy())
                return
            if i>=len(nums) or total > target:
                return 
            currentList.append(nums[i])
            recursive(i, currentList, total+nums[i])
            currentList.pop()
            recursive(i+1, currentList, total)
        recursive(0,[],0)
        return res
