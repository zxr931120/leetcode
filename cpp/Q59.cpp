#include <iostream>
#include <vector>

using namespace std;

enum direction {
    Up, Down, Left, Right
};

vector<vector<int>> generateMatrix(int);

void generate(vector<vector<int>> &, int, int, int, direction);

int main() {
    int n = 4;
    vector<vector<int>> matrix;
    matrix = generateMatrix(n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}

vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> matrix(n, vector<int>(n, 0));

    if (n == 0) {
        return matrix;
    }

//    for (int i = 0; i < n; i++) {
//        for (int j = 0; j < n; j++) {
//            matrix[i].push_back(0);
//        }
//    }

    generate(matrix, 1, 0, 0, Right);

    return matrix;
}

void generate(vector<vector<int>> &matrix, int input, int x, int y, direction dir) {
    matrix[x][y] = input;
    switch (dir) {
        case Right:
            if (y + 1 < matrix.size()) {
                if (matrix[x][y + 1] == 0) {
                    return generate(matrix, input + 1, x, y + 1, dir);
                }
            }
            //turn down.
            if (x + 1 < matrix.size()) {
                if (matrix[x + 1][y] == 0) {
                    return generate(matrix, input + 1, x + 1, y, Down);
                }
            }
            break;

        case Down:
            if (x + 1 < matrix.size()) {
                if (matrix[x + 1][y] == 0) {
                    return generate(matrix, input + 1, x + 1, y, dir);
                }
            }
            //turn left.
            if (y - 1 >= 0) {
                if (matrix[x][y - 1] == 0) {
                    return generate(matrix, input + 1, x, y - 1, Left);
                }
            }
            break;

        case Left:
            if (y - 1 >= 0) {
                if (matrix[x][y - 1] == 0) {
                    return generate(matrix, input + 1, x, y - 1, dir);
                }
            }
            //turn up.
            if (x - 1 >= 0) {
                if (matrix[x - 1][y] == 0) {
                    return generate(matrix, input + 1, x - 1, y, Up);
                }
            }
            break;

        case Up:
            if (x - 1 >= 0) {
                if (matrix[x - 1][y] == 0) {
                    return generate(matrix, input + 1, x - 1, y, dir);
                }
            }
            //turn right.
            if (y + 1 < matrix.size()) {
                if (matrix[x][y + 1] == 0) {
                    return generate(matrix, input + 1, x, y + 1, Right);
                }
            }
            break;
        default:
            break;
    }
}
