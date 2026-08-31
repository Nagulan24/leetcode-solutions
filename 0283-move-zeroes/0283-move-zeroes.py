class Solution(object):
    def moveZeroes(self, nums):
        temp =0
        i=0
        while i<len(nums)-1:
            if nums[i]==0:

                fnd=False
                
                temp =nums[i]
                for j in range(i,len(nums)-1):
                    nums[j]=nums[j+1]
                nums[len(nums)-1]= temp

                for k in range(i+1,len(nums)):
                    if nums[k]!=0:
                        fnd= True
                        break
                
                if not fnd:
                    break


            else:
                i+=1
        return nums