class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_w=set()
        upper_w=set()
        traversed =set()

        for i in word :
            
            if i.islower() :
                if i not in traversed :
                    lower_w.add(i)
                else :
                    upper_w.discard(i)
            
            else :
                ch = i.lower()
                
                if ch in lower_w :
                    upper_w.add(ch)
                    traversed.add(ch)
                    lower_w.discard(ch)
    
        return len(upper_w)
    
#