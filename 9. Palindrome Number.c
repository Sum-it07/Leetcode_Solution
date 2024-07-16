bool isPalindrome(int x) {
    int temp=0,sum=0,org=x;
    if (x<0){
        return false;
    }
    while(x!=0){
        temp=x%10;
        if (sum > (INT_MAX - temp) / 10) {
            return false;
        }        
        sum=sum*10+temp;
        x/=10;
    }
    return org==sum;
}
