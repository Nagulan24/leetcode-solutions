class Solution(object):
    def isPalindrome(self, x):
       rev=0
       org=x
       x=abs(x)
       while x != 0:
        ld=x % 10
        rev = (rev*10)+ld
        x= x // 10
  
       if org==rev:
        return True
       else:
        return False 
                