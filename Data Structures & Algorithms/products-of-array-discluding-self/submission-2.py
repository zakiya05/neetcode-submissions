class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        rProd=[1]*l
        for r in range(l-2,-1,-1):
            rProd[r] = rProd[r+1]*nums[r+1]
        res=[1]*l
        lp=1
        for i in range(l):
            if i:
                lp=lp*nums[i-1]
            res[i] = lp*rProd[i]
        return res
             