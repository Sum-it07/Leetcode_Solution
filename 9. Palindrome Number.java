class Solution {
    public boolean isPalindrome(int x) {
        boolean result = true;
        if(x<10 && x>0){
            return result;
        }
        if(x<0){
            return false;
        }
        int realValue=x;
        int palin=0;
        while(x!=0)
        {
            int temp=x%10;
            palin=palin*10+temp;
            x/=10;
        }
        if(realValue!=palin){
            result=false;
        }
        return result;

    }
}
