class Solution {
    public int countDigits(int num) {
        int count=0;
        int org =num;
        
        while(num>0){

            int dig= num%10;
            if (org%dig==0){
                count++;
            }
            num = num/10;
        }
        return count;
    }
}