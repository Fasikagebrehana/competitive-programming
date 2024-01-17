class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        vector<int> ans;
        int i=0;
        bool r=true;
        sort(arr.begin(),arr.end());
        while(i<arr.size()){
            int c=1;
            for(int j=i+1;j<arr.size();j++){
                if(arr[i]==arr[j])
                c++;
            }
        ans.push_back(c);
        i=i+c;
    }
    sort(ans.begin(),ans.end());
    for(int i=0;i<ans.size()-1;i++){
            if(ans[i]==ans[i+1])
            r=false;
        }
    
    return r;
    }
};