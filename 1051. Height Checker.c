int heightChecker(int* heights, int heightsSize) {
    int i,j,temp;
    int* original = (int*)malloc(heightsSize * sizeof(int));
    for (i = 0; i < heightsSize; i++) {
        original[i] = heights[i];
    }
    for(i=0;i<heightsSize-1;i++)
    {
        for(j=i+1;j<heightsSize;j++)
        {
            if(heights[i]>heights[j])
            {
                temp=heights[i];
                heights[i]=heights[j];
                heights[j]=temp;
            }
        }
    }
    int count=0;
    for(i=0;i<heightsSize;i++)
    {
        if(original[i]!=heights[i])
        {
            count++;
        }
    }
    return count;
}
