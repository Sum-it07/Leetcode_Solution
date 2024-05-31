double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int size=nums1Size+nums2Size;
    int arr[size];
    int i,count=0;
    for(i=0;i<nums1Size;i++)
    {
        arr[count]=nums1[i];
        count+=1;

    }
    for(i=0;i<nums2Size;i++)
    {
        arr[count]=nums2[i];
        count+=1;

    }
    for (i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    float res;
    if(size%2==1)
    {
        
        res=arr[size/2];
        return res;
    }
    else
    {
        res=(arr[size/2]+arr[(size/2)-1])/2.0;
        return res;
    }

}
