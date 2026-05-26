class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ones = [0]
        for i in nums:
            if i == 1:
                count += 1
            #elif count == ones[-1]:
                #count = 0
            else:    
                ones.append(count)
                count = 0
            ones.append(count)
        return max(ones)

s=Solution()
print(s.findMaxConsecutiveOnes([0,0,0,0,0,1,0,00,0,0,00]))
print(s.findMaxConsecutiveOnes([0,0,1,1,1,0,1,1,0,0,0,0,1,1,1,1,1,1,1,0]))