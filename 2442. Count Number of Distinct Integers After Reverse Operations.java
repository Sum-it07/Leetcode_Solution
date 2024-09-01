import java.util.Arrays;
class Solution {
    public int countDistinctIntegers(int[] nums) {
        int[] arr1=new int[nums.length];
        for(int i=0;i<nums.length;i++)
        {
            int temp=nums[i];
            int rev=0;
            while(temp!=0)
            {
                int temp1=temp%10;
                rev=rev*10+temp1;
                temp/=10;
            }
            arr1[i]=rev;
        } 
        int[] arr=new int[nums.length+arr1.length];
        ArrayList<Integer> list=new ArrayList<>();
        for(int i=0;i<nums.length;i++)
        {
            list.add(nums[i]);
        }
        for(int i=0;i<arr1.length;i++)
        {
            list.add(arr1[i]);
        }
        Collections.sort(list);
        int count = 1;
        for (int i = 1; i < list.size(); i++) {
            if (!list.get(count - 1).equals(list.get(i))) { 
                list.set(count, list.get(i));
                count++;
            }
        }


        return count;
    }
}
