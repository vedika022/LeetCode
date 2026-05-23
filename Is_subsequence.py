class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a=""
        for i in t:
            if i in s:
                a+=i
        if a==s:
            return True
        else:
            return False 
            
        