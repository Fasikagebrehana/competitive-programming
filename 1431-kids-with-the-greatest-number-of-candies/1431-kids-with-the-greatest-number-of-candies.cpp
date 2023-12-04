class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;
        int m=*max_element(candies.begin(), candies.end());
        for(int i=0;i<candies.size();i++){
            int s=candies[i]+ extraCandies;
            if(s>=m){
                result.push_back(true);
            }
            else{
                result.push_back(false);
            }
        }
        return result;
    }
};