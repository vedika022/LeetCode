class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a=''
        for i in range(len(t)):
                if t[i] in s:
                    a+=t[i]
        return s in a

        