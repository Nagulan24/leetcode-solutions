class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int j=0;
        int count =0;
        int lar;
        int arr[]= new int[nums.length*2];
        for (int i =0 ;i<nums.length;i++){
            if (nums[i]==1){
                count++;

            }
            else{
                arr[j]= count;
                j++;
                count=0;
            }

        }
        arr[j]=count;
        lar = arr[0];
        for(int k=0; k<arr.length;k++){
             
            if (lar <arr[k]){
                lar = arr[k];

            }
        }
        return lar;
    }
}