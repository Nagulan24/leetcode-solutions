class Solution(object):
    def check(self, nums):
        copy=sorted(nums)
        k = len(nums)
        for i in range(k):
            temp = nums[len(nums)-1]
            for j in range(len(nums)-1,0,-1):
                nums[j]= nums[j-1]
            nums[0]= temp
            if nums == copy:
                return True
                break
        else:
            return False

        