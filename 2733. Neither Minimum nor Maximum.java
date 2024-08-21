import java.util.Arrays;
class Solution {
    public int findNonMinOrMax(int[] nums) {
        Arrays.sort(nums);
        int a=nums[0];
        int b=nums[nums.length-1];
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=a && nums[i]!=b){
                return nums[i];
            }
        }
        return -1;
    }
}
