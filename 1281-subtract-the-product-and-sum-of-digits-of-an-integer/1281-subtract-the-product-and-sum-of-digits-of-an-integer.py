class Solution(object):
    def subtractProductAndSum(self, n):
        sum=0
        product=1
        while n>0:
            extract=n%10
            sum+=extract
            product *=extract
            n = n//10
        tot= product-sum
        return tot