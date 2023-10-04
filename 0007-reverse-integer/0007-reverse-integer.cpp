class Solution {
public:
    double reverse(int x) {
        
        int num = abs(x);
        double rev = 0;
        while (num != 0) {
            double n = num % 10;
            rev = rev * 10 + n;
            num = num / 10;
        }
        if (x < 0) {
            rev = -rev;
        }
         if (rev > INT_MAX || rev < INT_MIN) {
            return 0;
        }
        return rev;
    }
    
};