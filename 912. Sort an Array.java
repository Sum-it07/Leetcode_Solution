class Solution {
    public static void conqurer(int[] nums,int si,int mid,int ei){
        int[] merge=new int[ei-si+1];
        int id1=si;
        int id2=mid+1;
        int x=0;
        while(id1<=mid && id2<=ei ){
            if(nums[id1]<nums[id2]){
                merge[x]=nums[id1];
                x++;
                id1++;
            }
            else{
                merge[x]=nums[id2];
                x++;
                id2++;
            }
        }
        while(id1<=mid){
                merge[x]=nums[id1];
                x++;
                id1++;
        }
        while(id2<=ei){
                merge[x]=nums[id2];
                x++;
                id2++;
        }
        int j=si;
        for(int i=0;i<merge.length;i++){
            nums[j]=merge[i];
            j++;
        }

    }
    public static void divide(int[] nums,int si,int ei)
    {
        if(si>=ei)
        {
            return;
        }
        int mid=si+(ei-si)/2;
        divide(nums,si,mid);
        divide(nums,mid+1,ei);
        conqurer(nums,si,mid,ei);
    }
    public int[] sortArray(int[] nums) {
        int n=nums.length;
        divide(nums,0,n-1);
        return nums;
        
    }
}
