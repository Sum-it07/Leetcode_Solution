bool isPalindrome(int x) {
    if(x<0)
    {
        return false;
    }
    int i;
    int y=0;
    long int pal=0;
    int temp=x;
    while(x!=0)
    {
        y=x%10;
        x=x/10;
        pal=pal*10+y;
    }
    if(temp==pal){
        return true;
    }
    else{
        return false;
    }
}
