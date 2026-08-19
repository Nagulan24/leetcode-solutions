class Solution(object):
    def countDigits(self, num):
        n=0
        count=0
        orginal=num
        while num>0:
            n =num%10
            if orginal%n==0:
                count+=1
            num = num//10
        return count

        