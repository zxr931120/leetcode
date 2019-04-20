#include <iostream>
#include <vector>

using namespace std;

int maxSubArray(vector<int> &);

int main() {
    vector<int> a{-2, 1, 2, -4, 5, -1, 3};

    cout << maxSubArray(a) << endl;
    return 0;
}

int maxSubArray(vector<int> &nums) {
    int sum = 0;
    int max = 0;
    int hidx = 0;
    int sidx = 0;
    int eidx = 0;

    for (int i = 0; i < nums.size(); i++) {
        sum += nums[i];
        if (i == 0) {
            max = sum;
        }
        if (max < sum) {
            max = sum;
            sidx = hidx;
            eidx = i;
        }

        if (sum < 0) {
            sum = 0;
            hidx = i + 1;
        }
    }

    cout << "start and end: (" << sidx << ", " << eidx << ")" << endl;
    return max;
}
