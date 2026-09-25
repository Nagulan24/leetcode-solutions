class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        
        int count =0;
        int lar=0;
        int last;
        
        for (int i =0 ;i<nums.length;i++){
            if (nums[i]==1){
                count++;
            }
            else{
                if (lar<=count){
                    lar= count;
                    count=0;
                }
                else{
                    count=0;
                }
            }

        }
        last=count;
        if (lar>last){
            return lar;
        }
       else{
        return last;
       }
    
        
    }
}