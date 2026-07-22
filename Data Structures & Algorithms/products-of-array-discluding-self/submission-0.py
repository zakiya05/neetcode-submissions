class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        l=[1]*n
        r=[1]*n
    
        for i in range(1,n):
            l[i]=nums[i-1]*l[i-1]
        for j in range(n-2,-1,-1):
            r[j] = r[j+1]*nums[j+1]
        
        for i in range(n):
            l[i] = l[i]*r[i]
        return l