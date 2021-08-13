class Solution:
    def reverse(self, x: int) :                    
        z=''
        y=str(x)
        # here we are removing the minus sign from negetive number
        if(x<0):
            a=y[1:]
        else:
            a=y
        #A single digit numbe
        if(len(a)==1):
            return x
        #Reversing the string
        for i in a[ : :-1]:
            z=z+i
                
        if(z=='0'):
            return z
        
        if(x<0):
          #removing leading zeros 
            ans='-'+z.lstrip('0')
            ab=int(ans)
        else:
            ans= z.lstrip('0')
            ab=int(ans)
        #applying constraints         
        if -2 ** 31 <= ab <= 2 ** 31 - 1:
            return ab 
        return 0
            
        
