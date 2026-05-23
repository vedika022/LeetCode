class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a=''
        j=0
        for i in range(len(t)):
                if j<len(s) and t[i] == s[j]:
                    a+=t[i]
                    j+=1
        return  a==s

        