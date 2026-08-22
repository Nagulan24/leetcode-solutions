class Solution(object):
    def runningSum(self, nums):
        sum= nums[0]
        arr=[sum]
        for i in range(1,len(nums)):
            
            sum+= nums[i]
            arr.append(sum)
        return arr