class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowerchars = ''
        upperchars = ''
        count = 0
        word = set(word)
        for i in word :
            if i.islower() :
                if i in upperchars:
                    upperchars = upperchars.replace(i,'')
                    count += 1
                else :
                    lowerchars += i
            else :                  #i.isupper() : 
                if i.lower() in lowerchars:
                    lowerchars = lowerchars.replace(i.lower(),'')
                    count += 1
                else :
                    upperchars += i.lower()
        
        return count
    

#solved without any help from chatgpt*!!!!!!!!!!!!!!!!!!!!!
#only help taken was to name all string manipulation functions in python
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  
#   
            
s = Solution()
print(s.numberOfSpecialChars('AABab') )     