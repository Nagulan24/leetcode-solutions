import java.util.Arrays;
class Solution {
    public int missingNumber(int[] nums) {
        int tot=nums.length;
        int value =0;
        for(int i=0;i<nums.length;i++){
            tot+=i;
            value+=nums[i];

    }
       return tot-value; 
    }
}