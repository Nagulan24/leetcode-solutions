class Solution {

    public void rev(int first, int last,int[] arr) {
        
        

        while(first<last){
            int temp = arr[first];
            arr[first]=arr[last];
            arr[last]= temp;

            first++;
            last--;
        }
        
    }
    
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k%nums.length;

        rev(0,n-k-1,nums);
        rev(n-k,nums.length-1,nums);
        rev(0,nums.length-1,nums);
    }
}
