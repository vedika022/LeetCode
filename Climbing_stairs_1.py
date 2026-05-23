class Solution:
    def climbStairs(self, n: int) -> int:
        count=0      # 0 steps
        
        if n>0:      # 1+1+1.... (n times) all
            count+=1
        if n%2==0:      # 2+2+2...(n/2 times) even numbers
            count+=1
        else :        # all odd numbers 
            count += int(n/2+0.5)      
        return count