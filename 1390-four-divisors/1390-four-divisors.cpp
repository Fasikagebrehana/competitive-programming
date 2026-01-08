class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {
        int sum = 0;

        for (int num : nums) {
            int divisorCount = 0;
            int divisorSum = 0;

            for (int i = 1; i <= sqrt(num); i++) {
                if (num % i == 0) {
                    divisorCount++;
                    divisorSum += i;
                    if (num / i != i) {
                        divisorCount++;
                        divisorSum += num / i;
                    }
                }
                if (divisorCount > 4) {
                    break;
                }
            }

            if (divisorCount == 4) {
                sum += divisorSum;
            }
        }

        return sum;
    }
};
