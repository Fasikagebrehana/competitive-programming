class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        char result = letters[0];
        for(int i=0;i < letters.size();i++){
            if(target < letters[i]){
                result = letters[i];
                break;
            }
        }
      return result;  
    }
};