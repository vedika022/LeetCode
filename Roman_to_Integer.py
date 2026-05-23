class Solution:
    def romanToInt(self, s: str) -> int:
        total=0
        for i in range(len(s)):
                if s[i] == 'I' :
                    if i+1<len(s) and s[i+1]== 'V' :
                        total+=4
                    elif i+1<len(s) and s[i+1]== 'X' :
                        total+=9
                    else : total+=1  
                if s[i] == 'X' :
                    if i+1<len(s) and s[i+1]== 'L' :
                        total+=40
                    elif i+1<len(s) and s[i+1]== 'C' :
                        total+=90 
                    elif i-1 >= 0 and s[i-1]=='I':
                        pass
                    else : total+=10      
                if s[i] == 'C' :
                    if i+1<len(s) and s[i+1]== 'D' :
                        total+=400
                    elif i+1<len(s) and s[i+1]== 'M' :
                        total+=900
                    elif i-1 >= 0 and s[i-1]=='X':
                        pass
                    else : total+=100
                if s[i]=='V':
                    if i-1 >= 0 and s[i-1]=='I':
                        pass
                    else: total+=5
                if s[i]== 'L':
                    if i-1 >= 0 and s[i-1]=='X':
                        pass
                    else: total+=50
                if s[i]=='D':
                    if i-1 >= 0 and s[i-1]=='C':
                        pass
                    else: total+=500
                if s[i]=='M':
                    if i-1 >= 0 and s[i-1]=='C':
                        pass
                    else: total+=1000

        return total
            
                    
                
        