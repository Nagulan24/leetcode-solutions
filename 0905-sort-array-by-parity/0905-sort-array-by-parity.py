class Solution(object):
    def sortArrayByParity(self, nums):
        first=0
        last=len(nums)-1
        while last>first:
            if nums[first]%2==0:
                first+=1
                
            elif nums[last]%2!=0:
                last-=1

            else :
                nums[last],nums[first] = nums[first],nums[last]
                last-=1
                first+=1
        return nums 
            
        