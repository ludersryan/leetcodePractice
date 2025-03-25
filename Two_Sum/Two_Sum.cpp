#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> numMap; 

    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i]; // complement if target = 9 and nums[i] = 2, 9 -2=7, check if 7 exists
        if (numMap.find(complement) != numMap.end()) { // check
            return {numMap[complement], i}; 
        }
        numMap[nums[i]] = i; // store data in numMap
    }
    
    return {}; 
}
int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = twoSum(nums, target);
    cout << "Indices: [" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}