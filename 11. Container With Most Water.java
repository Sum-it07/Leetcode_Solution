class Solution {
    public int maxArea(int[] height) {
        int left=0;
        int right=height.length-1;
        int maxarea=0;
        while(left<right)
        {
            int area;
            int width=right-left;
            int newh=0;
            if(height[left]<height[right])
            {
                newh=height[left];
            }
            else{
                newh=height[right];

            }
            area=newh*width;
            if (height[left]<height[right])
            {
                left++;
            }
            else{
                right--;
            }
            if(maxarea<area)
            {
                maxarea=area;
            }
        }
        return maxarea;
    }
}
