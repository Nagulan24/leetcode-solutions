class Solution(object):
    def rotate(self, nums, k):
        '''for i in range(k):
            temp=nums[len(nums)-1]
            for j in range((len(nums)-1),0,-1):
                nums[j]=nums[j-1]
            nums[0]=temp
        return nums'''

        if len(nums)<1:
            return nums


        n = len(nums)
        k%=n

        
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        return nums