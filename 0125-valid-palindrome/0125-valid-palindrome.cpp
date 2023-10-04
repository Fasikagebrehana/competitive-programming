class Solution {
public:
    bool isPalindrome(string s) {
        transform(s.begin(),s.end(),s.begin(), ::tolower);
        string result;
        bool r;
        for(char c : s){
            if(isalnum(c))
            result+=c;
        }
        
        string rev=result;
        reverse(rev.begin(),rev.end());
        if(result==rev){
                r= true;
            }
        else{
                r= false;
            }
        
        return r;
    }
};