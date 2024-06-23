#include <iostream>
#include <vector>
#include <string>
using namespace std;


// class Solution {
// public:
//     int numberOfSubarrays(vector<int>& nums, int k) {
        
//         int i=0, j=0;
//         int odds = nums[0] % 2 == 1;
//         int count=0;

//         while (i<nums.size()-k+1 && j<nums.size()) {
//             if (odds==k) {
//                 for (int a=i; a<=j; a++){
//                     cout << nums[a] << " ";
//                 } cout << endl;

//                 int prev=0, next=1;
//                 while (nums[i+prev] % 2 == 0) {prev++;}
//                 while (j+next<nums.size() && nums[j+next] % 2 == 0) {next++;}
//                 count += (prev+1) * (next);
                
//                 while (i<nums.size() && nums[i] % 2 == 0) {i++;}
//                 odds--;
//                 i++;
//             }
//             while (j<nums.size() && odds < k) {
//                 j++;
//                 if (nums.size()==j){continue;}
//                 odds += nums[j] % 2;
//             }
//         }

//         cout << "count: " << count << endl;
        
//         return count;
//     }
// };


class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> count(n + 1, 0);
        count[0] = 1;
        int ans = 0, t = 0;
        
        for (int v : nums) {
            t += v & 1;
            if (t - k >= 0) {
                ans += count[t - k];
            }
            count[t]++;
        }
        
        return ans;
    }
};


int main() {

    vector< vector <int> > nums = {
        // {1,1,1,1,1},
        // {1,1,2,1,1,2,1,1},
        // {1,1,2,1,1},
        // {2,4,6},
        {2,2,2,1,2,2,1,2,2,2}
    };
    vector<int> k = {
        // 1,
        // 3,
        // 3,
        // 1,
        2
    };

    Solution s;
    for (int i=0; i<nums.size(); i++) {
        s.numberOfSubarrays(nums[i], k[i]);
    }

    return 0;
}