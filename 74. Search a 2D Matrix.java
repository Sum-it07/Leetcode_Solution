class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row=matrix.length;
        int col=matrix[0].length;
        boolean result=false;
        int m=0;
        int n=col-1;
        while(m<row && n>=0){
            if(matrix[m][n]==target){
                result=true;
                break;
            }
            if(matrix[m][n]<target){
                m++;
            }
            else{
                n--;
            }
        }
        return result;

    }
}
