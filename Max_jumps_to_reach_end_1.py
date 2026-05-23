class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        i=0
        j=1
        n=len(nums) 
        count = 0
        while j<n:
            if -target <= nums[j]-nums[i] <= target:
                count += 1
                i=j
                j+=1
            else :
                j+=1
        if i==n-1:
            return count
        else:
            return -1