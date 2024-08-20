class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        boolean result=false;
        for(int rot=0;rot<4;rot++){
            boolean check=true;
            for(int m=0;m<mat.length;m++)
            {
                for(int n=0;n<mat[0].length;n++){
                    if(mat[m][n]!=target[m][n])
                    {
                        check= false;
                        break;
                    }
                }
                if(check==false){
                    break;
                }
            }
            if(check==true){
                result=true;
                break;
            }
            for(int i=0;i<mat.length;i++)
            {
                for(int j=i+1;j<mat[0].length;j++)
                {
                    int temp=mat[i][j];
                    mat[i][j]=mat[j][i];
                    mat[j][i]=temp;
                }
            }
            for(int i=0;i<mat.length;i++)
            {
                int low=0;
                int high=mat.length-1;
                while(low<high)
                {
                    int temp=mat[i][high];
                    mat[i][high]=mat[i][low];
                    mat[i][low]=temp;
                    low++;
                    high--;

                }
            }
        }
        return result;
    }
}
