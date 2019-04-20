#include <iostream>
#include <vector>

using namespace std;

double findMedianSortedArrays(vector<int> &m, vector<int> &);

vector<int> mergeArrays(vector<int> &, vector<int> &);

int main() {
    vector<int> a{1, 2, 3, 4, 8};
    vector<int> b{2, 4, 8};

    vector<int> res;


    double median = findMedianSortedArrays(a, b);
    cout << median;

    return 0;
}

double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
    //O(m+n)
    vector<int> res;
    res = mergeArrays(nums1, nums2);


    if (res.size() % 2 == 0) {
        double a = res[res.size() / 2];
        double b = res[res.size() / 2 - 1];
        return (a + b) / 2;
    }

    double a = res[(res.size() - 1) / 2];
    return a;
}

vector<int> mergeArrays(vector<int> &nums1, vector<int> &nums2) {
    if (nums1.empty()) {
        return mergeArrays(nums2, nums1);
    }

    vector<int> res = nums1;
    int ridx = 0;
    int outrange = 0;
    bool out = false;
    for (int i = 0; i < nums2.size(); i++) {
        while (nums2[i] > res[ridx]) {
            ridx++;
            if (ridx >= res.size()) {
                out = true;
                break;
            }
        }
        if (ridx >= res.size()) {
            outrange = i;
            break;
        }

        res.insert(res.begin() + ridx, nums2[i]);
    }

    if (out) {
        for (int i = outrange; i < nums2.size(); i++) {
            res.push_back(nums2[i]);
        }
    }


    return res;
}


