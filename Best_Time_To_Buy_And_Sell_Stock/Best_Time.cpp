#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // buy when stock price is low, sell when it is high based on given prices
        // b =1, s=6 in this case
        // buy at lowest, sell at highest. min first then max.
        int min = prices[0];
        int profit = 0;
        for(int i=0; i<prices.size(); i++){
            if(prices[i] < min){ // check if new price is lower
                min = prices[i]; // if lower, update
            }
            profit = max(profit, prices[i]-min);  //compare
        }

        return profit;
    }
};

int main() {
    vector<int> prices = {7, 1, 5, 3, 6, 4}; // Example input
    Solution sol;
    int result = sol.maxProfit(prices);
    cout << "Maximum Profit: " << result << endl;
    return 0;
}