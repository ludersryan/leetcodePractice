#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int pre = 1;
        int post = 1;
        int size = nums.size();
        vector<int> ans(size);
        for(int i = 0; i < nums.size(); i++){
           ans[i] = pre;
           pre = nums[i]*pre;
        }
        for(int i = nums.size() - 1; i >= 0; --i){
            ans[i] = ans[i] * post;
            post = post*nums[i];
        }
        return ans; 
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3, 4}; 
    vector<int> result = solution.productExceptSelf(nums);
    
    cout << "Output: [";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    
    return 0;
}
