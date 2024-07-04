class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<int> r;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==target)
            r.push_back(i);
        }
        return r;
    }
};