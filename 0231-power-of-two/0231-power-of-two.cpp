class Solution {
public:
    bool isPowerOfTwo(int n) {
        bool r=false;
        while(n!=1&&(n%2)==0&&n!=0){
            n=n/2;
        }
        if(n==1){
            r=true;
        }
        return r;
    }
};