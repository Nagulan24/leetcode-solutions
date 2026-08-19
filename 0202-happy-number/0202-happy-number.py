class Solution(object):
    def isHappy(self, n):
        seen=set()
        while n!=1:
            
            if n in seen:
                return False
            seen.add(n)
            sum=0
            while n>0:
                dig=n%10
                sum+=(dig*dig)
                n=n//10
            n= sum
        return True
        
   

        