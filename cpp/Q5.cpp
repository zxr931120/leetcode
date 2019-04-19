#include <iostream>
#include <string>
#include <vector>

using namespace std;

string longestPalindrome(string);

string bruteForce(string);

string dynamicProgramming(string);

vector<int> recurrence(int, int, string &);

bool judgementCut(string);

int main() {
    string a = "ll";
    string res = longestPalindrome(a);
    cout << res.length() << endl;
    cout << "res is: " << res << endl;
}

string bruteForce(string s) {
    if (s.length() == 0) {
        return "";
    }
    int msidx = 0;
    int maxSub = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s.length() - i < maxSub) {
            break;
        }
        for (int j = s.length() - 1; j >= i; j--) {
            if (j - i + 1 < maxSub) {
                break;
            }
            string Substr = s.substr(i, j - i + 1);
            if (judgementCut(Substr)) {
                if (Substr.length() > maxSub) {
                    msidx = i;
                    maxSub = Substr.length();
                }
            }
        }
    }

    return s.substr(msidx, maxSub);
}

string longestPalindrome(string s) {
    //return bruteForce(s);
    return dynamicProgramming(s);
}

string dynamicProgramming(string s) {
    vector<int> idxHolder;
    vector<int> tmp;
    int maxlen = 0;
    int tmplen;

    for (int i = 0; i < s.length(); i++) {
        tmp = recurrence(i, i, s);
        tmplen = tmp[1] - tmp[0] + 1;
        if (tmplen > maxlen) {
            maxlen = tmplen;
            idxHolder = tmp;
        }
        if (i + 1 < s.length()  && s[i] == s[i + 1]) {
            tmp = recurrence(i, i + 1, s);
            tmplen = tmp[1] - tmp[0] + 1;
            if (tmplen > maxlen) {
                maxlen = tmplen;
                idxHolder = tmp;
            }
        }
    }

    return s.substr(idxHolder[0], maxlen);
}

vector<int> recurrence(int i, int j, string &s) {
    if (i < 0 || j > s.length() - 1) {
        return vector<int>{i + 1, j - 1};
    }

    if (s[i] != s[j]) {
        return vector<int>{i + 1, j - 1};
    }

    return recurrence(i - 1, j + 1, s);
}

bool judgementCut(string s) {
    for (int i = 0; i < s.length() / 2; i++) {
        if (s[i] != s[s.length() - i - 1]) {
            return false;
        }
    }
    return true;
}
