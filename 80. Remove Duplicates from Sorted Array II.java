class Solution {
    public int removeDuplicates(int[] nums) {
        int position=1;
        int count=1;
        for(int i=1;i<nums.length;i++)
        {
            if(nums[i]!=nums[i-1] )
            {
                nums[position]=nums[i];
                count=1;
                position++;
            }
            else
            {
                if(count==1)
                {
                    nums[position]=nums[i];
                    position++;
                }
                count++;
            }
        }
        return position;
    }
}
