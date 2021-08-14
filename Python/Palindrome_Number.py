class Solution:
    def isPalindrome(self, x: int) :
        y=str(x)
        z=y[: :-1]
        if(y==z):
            return True 
        return False
    
