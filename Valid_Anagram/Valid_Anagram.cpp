#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
bool isAnagram(string s, string t) {
    // make 2 hash map, count freq of char and compare for result
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<char, int> countS;
        unordered_map<char, int> countT;
        for (int i = 0; i < s.length(); i++) {
            countS[s[i]]++;
            countT[t[i]]++;
        }
        return countS == countT;
    }
};


int main() {
    Solution solution;
    
    string s1 = "racecar", t1 = "carrace";
    cout << boolalpha << solution.isAnagram(s1, t1) << endl; 
    
    string s2 = "jar", t2 = "jam";
    cout << boolalpha << solution.isAnagram(s2, t2) << endl; 
    
    return 0;
}