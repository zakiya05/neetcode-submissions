class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        rightp=[1]*n
        for i in range(n-2,-1,-1):
            rightp[i]=rightp[i+1]*nums[i+1]
        lp=1
        res=[1]*n
        for i in range(n):
            if i:
                lp = lp*nums[i-1]
            res[i]= lp*rightp[i]
        return res
        