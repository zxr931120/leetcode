#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> spiralMatrixIII(int, int, int, int);

int distanceFromStartPoint(int, int, int, int);

int main() {
    vector<vector<int>> m;
    m = spiralMatrixIII(5, 6, 1, 4);

    return 0;
}

vector<vector<int>> spiralMatrixIII(int R, int C, int r0, int c0) {
    if (R == 0 || C == 0) {
        vector<vector<int>> nullreturn;
        return nullreturn;
    }

    vector<vector<int>> matrix(R, vector<int>(C, 0));
    //int signal = 0;
    int max = 0;

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {

            matrix[i][j] = distanceFromStartPoint(i, j, r0, c0);
            //signal += matrix[i][j];
            if (matrix[i][j] > max) {
                max = matrix[i][j];
            }

            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    vector<vector<int>> out(R * C, vector<int>(2, 0));
    vector<vector<int>> rawout(max + 1, vector<int>(2, -1));
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            rawout[matrix[i][j]][0] = i;
            rawout[matrix[i][j]][1] = j;
        }
    }

    int rawidx = 0;
    for (int i = 0; i < R * C; i++) {
        while (rawout[rawidx][0] == -1) {
            rawidx++;
        }
        out[i] = rawout[rawidx];
        cout << "(" << out[i][0] << "," << out[i][1] << ") ";
        if (i % C == C - 1) {
            cout << endl;
        }
        rawidx++;
    }

//    for (int i = 0; i < R * C; i++) {
//        int min = signal;
//        int min_j = 0;
//        int min_k = 0;
//        for (int j = 0; j < R; j++) {
//            for (int k = 0; k < C; k++) {
//                if (matrix[j][k] < min) {
//                    min = matrix[j][k];
//                    min_j = j;
//                    min_k = k;
//                }
//            }
//        }
//        out[i][0] = min_j;
//        out[i][1] = min_k;
//        cout << "(" << out[i][0] << "," << out[i][1] << ") ";
//        matrix[min_j][min_k] = signal;
//        if (i % C == C - 1) {
//            cout << endl;
//        }
//    }

    return out;

}

int distanceFromStartPoint(int r, int c, int r0, int c0) {
    int dis_c = abs(c - c0);
    int dis_r = abs(r - r0);
    int distance = max(dis_r, dis_c);
    int base = (2 * distance - 1) * (2 * distance - 1);

    int sp_c = c0 + distance;
    int sp_r = r0 - distance + 1;

    if (r == sp_r - 1 && c == sp_c) {
        return distance * 8 - 1 + base;
    }

    if (r == sp_r - 1) {
        return distance * 8 - 1 + base - (sp_c - c);
    }

    if (c == sp_c) {
        return r - sp_r + base;
    }


    return distance * 2 + (sp_c - c) + 2 * (distance - 1) + sp_r - r + base;
}