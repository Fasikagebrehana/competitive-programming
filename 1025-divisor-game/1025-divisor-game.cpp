class Solution {
public:
    bool divisorGame(int n) {
        if((n-1)%2 != 0){
            return true;
        }
        else
            return false;
    }
};