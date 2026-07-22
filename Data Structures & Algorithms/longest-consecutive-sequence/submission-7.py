class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp={}
        max_count=0
        for i in range(len(nums)):
            mp[nums[i]] = i
        for i in range(len(nums)):
            if mp.get(nums[i]-1, -1)>=0:
                continue 
            else:
                x = nums[i]
                count = 1
                while mp.get(x+1, -1)>-1:
                    count+=1
                    x+=1
                max_count = max(max_count, count)
        return max_count
                

