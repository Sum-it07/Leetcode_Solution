import java.util.Arrays;
class Solution {
    public int maximizeSum(int[] nums, int k) {
        // int max = Arrays.stream(nums).max().orElseThrow();
        int max=nums[0];
        for(int i=0;i<nums.length;i++)
        {
            if(max<nums[i])
            {
                max=nums[i];
            }
        }
        int temp=max;
        for(int i=1;i<k;i++)
        {
            temp++;
            max+=temp;
        }
        return max;
    }
}
