class Solution {
    public int findKthLargest(int[] nums, int k) {
        return quickselect(nums,0,nums.length-1,nums.length-k);

    }
        public int quickselect(int[] arr,int l,int r,int k){
            if(l==r){
                return arr[l];
            }
            int pivot_index=(l+r)/2;
            int pivot=arr[pivot_index];
            // arr[pivot_index]=arr[r];
            // arr[r]=pivot;
            swap(arr,pivot_index,r);

            int index=l;
            for(int i=l;i<r;i++)
            {
                if(arr[i]<pivot){
                    // int temp=arr[i];
                    // arr[i]=arr[index];
                    // arr[index]=temp;
                    swap(arr,i,index);
                    index++;
                }

            }
            // int temp=arr[index];
            // arr[index]=arr[r];
            // arr[r]=temp;
            swap(arr,index,r);

            if(index==k)
            {
                return arr[index];
            }
            else if(index<k){
                return quickselect(arr,index+1,r,k);
            }
            else{
                return quickselect(arr,l,index-1,k);
            }

        }
        public void swap(int[] arr, int i, int j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }


}
