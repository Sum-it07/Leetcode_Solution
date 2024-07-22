class Solution {
    public int fib(int n) {
        int a=0;
        int b=0;
        int c=1;
        int ans=0;
        for(int i=0;i<n;i++)
        {
            ans=c;
            a=b;
            b=c;
            c=a+b;

        }
        return ans;
    }
}
