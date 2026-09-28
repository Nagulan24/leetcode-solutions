import java.util.Arrays;
class Solution {
    public int missingNumber(int[] nums) {
        int val =nums.length;
        Arrays.sort(nums);
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=i){
                 val=i;
                 break;
                
            }

        }
        return val;
    }
}