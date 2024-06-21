#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;


class Solution {
public:
    int findSmallestInteger(vector<int>& nums, int value) {
        unordered_map<int, int> map;

        for (int num: nums){
            int val = num;
            val = val % value;
            while (val<0) {val+=value;}
            if (map.count(val)) {map[val]+=1;}
            else {map[val]=1;}
        }
        for (auto& element: map){
            cout << element.first << " " << element.second << "\n";
        }
        int min_val = 0; 
        for (int i=0; i<value; i++) {
            if (!map.count(i)) {return i;}
            if (map[i]<map[min_val]) {min_val=i;}
        }
        // if (min_val==0) {min_val=value;}
        return value * (map[min_val%value]) + min_val;
    }
};

int main() {

    vector< vector<int> > nums = {
        {1,-10,7,13,6,8},
        {3,0,3,2,4,2,1,1,0,4},
        {3,0,3,2,4,2,1,1,0,4,0,1},
        {3,0,3,2,4,2,1,1,0,4},
        {1,-10,7,13,6,8}
    };
    vector<int> value = {
        5,
        7
    };

    Solution s;
    for (int i=0; i<nums.size(); i++) {
        s.findSmallestInteger(nums[i], value[i]);
    }

    return 0;
}