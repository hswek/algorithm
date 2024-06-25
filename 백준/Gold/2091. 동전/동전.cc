#include <iostream>
#include <cstring>
using namespace std;

int x, a, b, c, d;
int ss = 0;
int r[4] = {0, 0, 0, 0};
int cache[10100];

void recursive(int num_a, int num_b, int num_c, int num_d, int s) {
    if (s == x) {
        if (num_a + num_b + num_c + num_d > ss) {
            ss = num_a + num_b + num_c + num_d;
            r[0] = num_a; r[1] = num_b; r[2] = num_c; r[3] = num_d;
        }
        return;
    }
    if (s > x) {
        return;
    }
    if (cache[num_a + 5 * num_b + 10 * num_c + 25 * num_d] >= num_a + num_b + num_c + num_d) {
        return;
    }
    cache[num_a + 5 * num_b + 10 * num_c + 25 * num_d] = num_a + num_b + num_c + num_d;
    if (num_a + 5 <= a && s + 5 <= x) {
        recursive(num_a + 5, num_b, num_c, num_d, s + 5);
    }
    if (num_b != b && s + 5 <= x) {
        recursive(num_a, num_b + 1, num_c, num_d, s + 5);
    }
    if (num_c != c && s + 10 <= x) {
        recursive(num_a, num_b, num_c + 1, num_d, s + 10);
    }
    if (num_d != d && s + 25 <= x) {
        recursive(num_a, num_b, num_c, num_d + 1, s + 25);
    }
}

int main() {
    cin >> x >> a >> b >> c >> d;
    memset(cache, -1, sizeof(cache));
    if (x % 5 > a) {
        cout << "0 0 0 0" << endl;
    } else {
        int tmp = x % 5;
        recursive(tmp, 0, 0, 0, tmp);
        for (int i = 0; i < 4; i++) {
            cout << r[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
