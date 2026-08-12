class Solution(object):
    def findNumbers(self, nums):
        cnt=0
        for val in nums:
            count=0
            while val>0:
                val= val//10
                count+=1
            if count%2==0:
                cnt+=1
        return cnt
        