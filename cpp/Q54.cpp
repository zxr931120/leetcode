#include <iostream>
#include <vector>

using namespace std;

enum direction {
    Up, Down, Left, Right
};

vector<int> spiralOrder(vector<vector<int>> &);

void findNext(vector<vector<int>> &, vector<int> &, int, int, int, direction);

int main() {
    std::cout << "Hello, World!" << std::endl;
    vector<vector<int>> matrix{};
    vector<int> out;
    out = spiralOrder(matrix);

    cout << "out is: ";
    for (int x : out)
        cout << x << " ";

    cout << endl;
    return 0;
}

vector<int> spiralOrder(vector<vector<int>> &matrix) {
    int signal = 0;
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            signal += matrix[i][j];
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    cout << "signal is: " << signal << endl;

    vector<int> output;

    if (matrix.size() == 0) {
        return output;
    }

    findNext(matrix, output, 0, 0, signal, Right);

    return output;
}

void findNext(vector<vector<int>> &matrix, vector<int> &output, int x, int y, int signal, direction dir) {
    output.push_back(matrix[x][y]);
    matrix[x][y] = signal;

    if (dir == Right) {
        if (y + 1 < matrix[x].size()) {
            if (matrix[x][y + 1] != signal) {
                findNext(matrix, output, x, y + 1, signal, dir);
                return;
            }
        }

        //case cannot move right, turn down.
        if (x + 1 < matrix.size()) {
            if (matrix[x + 1][y] != signal) {
                findNext(matrix, output, x + 1, y, signal, Down);
                return;
            }
        }

        return;
    }

    if (dir == Down) {
        if (x + 1 < matrix.size()) {
            if (matrix[x + 1][y] != signal) {
                findNext(matrix, output, x + 1, y, signal, dir);
                return;
            }
        }

        //case cannot move down, turn left.
        if (y - 1 >= 0) {
            if (matrix[x][y - 1] != signal) {
                findNext(matrix, output, x, y - 1, signal, Left);
                return;
            }
        }

        return;
    }

    if (dir == Left) {
        if (y - 1 >= 0) {
            if (matrix[x][y - 1] != signal) {
                findNext(matrix, output, x, y - 1, signal, dir);
                return;
            }
        }

        //case cannot move left, turn up.
        if (x - 1 >= 0) {
            if (matrix[x - 1][y] != signal) {
                findNext(matrix, output, x - 1, y, signal, Up);
                return;
            }
        }
        return;
    }

    if (dir == Up) {
        if (x - 1 >= 0) {
            if (matrix[x - 1][y] != signal) {
                findNext(matrix, output, x - 1, y, signal, dir);
                return;
            }
        }

        //cannot move up, turn right.
        if (y + 1 < matrix[x].size()) {
            if (matrix[x][y + 1] != signal) {
                findNext(matrix, output, x, y + 1, signal, Right);
                return;
            }
        }
        return;
    }
    cout << "some thing strange." << endl;
    return;
}
