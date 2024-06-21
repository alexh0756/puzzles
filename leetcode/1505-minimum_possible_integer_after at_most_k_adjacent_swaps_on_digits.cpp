#include <iostream>
#include <vector>
#include <string>
using namespace std;


class Solution {
public:
    string minInteger(string num, int k) {
        int start=num.size()-1;
        vector<int> vec_num(num.size());

        int min_i = 0;
        for (int i=0; i<num.size(); i++){
            vec_num[i] = num[i] - '0';
            if (vec_num[i] < vec_num[min_i] && i<=start+k) {min_i=i;} // need to initialise the start better for loop
        }

        while (start<vec_num.size()-1 && k>0){
            int loc = min_i;
            k = k - min_i + start;
            while (start!=loc){
                int tmp = vec_num[loc];
                vec_num[loc] = vec_num[loc-1];
                vec_num[loc-1] = tmp;
                loc--;
            }
            for (int n: vec_num) {cout << n << " ";} cout << endl;
            start++;
            min_i = start;
            int end = vec_num.size();
            if (start+k<end){end=start+k+1;}
            for (int i=start;i<end;i++) {
                if (vec_num[i]<vec_num[min_i]){min_i=i;}
            }
        }
        string output = "";
        for (int n: vec_num){
            output = output + to_string(n);
        }
        cout << output << endl << endl;
        return output;
    }
};


int main() {

    vector<string> num = {
        "3895246579",
        "9438957234785635408",
        "4321",
        "4321",
        "100",
        "36789"
    };
    vector<int> k = {
        4,
        23,
        8,
        4,
        1,
        1000
    };

    Solution s;
    for (int i=0; i<num.size(); i++) {
        s.minInteger(num[i], k[i]);
    }

    return 0;
}