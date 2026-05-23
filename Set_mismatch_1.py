class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        for i in range(len(nums)-1):
            
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
                

            elif nums[i] == nums[i+1] - 1 :
                continue   
            
            else:
                ans.append( 1 + nums[i] )

        if len(ans) == 1:
            if ans[0]==len(nums):
                ans.append(ans[0]-1)
            else:
                ans.append(len(nums))

        return ans