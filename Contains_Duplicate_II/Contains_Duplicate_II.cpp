#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> numSet; // Hash set to store unique numbers, key is number and value is the position last encountered

        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i]; 
            if (numSet.find(num) != numSet.end() && abs(i-numSet[num])<= k) { // if num exist and i - position of num <= k
                
                return true;
            }
            
            numSet[num] = i; // insert or update position
        }
        
        return false; // no duplicates found
    }
};

int main() {
    vector<int> nums = {1,2,3,1,2,3};  
    int k = 3;
    
    Solution sol;
    bool result = sol.containsNearbyDuplicate(nums, k);
    cout << (result ? "true" : "false") << endl;  
    
    return 0;
}