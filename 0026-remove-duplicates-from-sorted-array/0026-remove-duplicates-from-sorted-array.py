class Solution(object):
    def removeDuplicates(self, nums):
        count=0
        i=0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i+=1
                count+=1
        return i+1 
        