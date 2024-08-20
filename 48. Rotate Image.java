class Solution {
    public void reverse(int[] matrix){
        int n=matrix.length-1;
        int m=0;
        while(m<n){
            int temp=matrix[m];
            matrix[m]=matrix[n];
            matrix[n]=temp;
            m++;
            n--;
        }
    }

    public void rotate(int[][] matrix) {
        for(int i=0;i<matrix.length;i++)
        {
            for(int j=i;j<matrix.length;j++)
            {
                int temp=matrix[i][j];
                matrix[i][j]=matrix[j][i];
                matrix[j][i]=temp;
            }
        }
        for(int i=0;i<matrix.length;i++)
        {
            reverse(matrix[i]);

        }
    }
}
