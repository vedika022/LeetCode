class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        #affordable_choco=[x for x in prices if x < money]
        spent = money
        k=False
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]+prices[j] <= spent: 
                    spent = prices[i]+prices[j]
                    k=True

        if k is False:
            return money
        else:
            return money-spent
    
    
s=Solution()
print(s.buyChoco([1,2,2,3,3],3))
print(s.buyChoco([1,1,21,3,5,5,10],10))
print(s.buyChoco([1,2,3],3))
print(s.buyChoco([1,2,2,3,1],7))