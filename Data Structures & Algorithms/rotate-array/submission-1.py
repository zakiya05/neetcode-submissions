class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        def reverse(l,r):
            while l<r:
                print("l,r ",l, r,"\n")
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
        k%=(n+1)     
        reverse(0,n)
        reverse(0,k-1)
        reverse(k,n)
        
        