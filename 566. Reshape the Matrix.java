class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int[][] arr=new int[r][c];
        int[] arr1=new int[r*c];
        if((r*c)!=mat.length*mat[0].length)
        {
            return mat;
        }
        int index=0;
        int m=0,n=0;
        for (int i=0;i<mat.length;i++)
        {
            for(int j=0;j<mat[0].length;j++)
            {
                arr[m][n]=mat[i][j];
                n++;
                if(n==c)
                {
                    n=0;
                    m++;
                }
                // arr1[index++]=mat[i][j];
            }
        }
        // index=0;
        // for(int i=0;i<r;i++)
        // {
        //     for(int j=0;j<c;j++)
        //     {
        //         arr[i][j]=arr1[index++];
        //     }
        // }
        return arr;
    }
}
