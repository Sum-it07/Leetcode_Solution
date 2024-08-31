class Solution {
    public int hammingDistance(int x, int y) {
        int pos=x^y;
        int count=0;
        while(pos>0)
        {
            count+=(pos&1);
            pos=pos>>1;
        }
        return count;
    }
}
