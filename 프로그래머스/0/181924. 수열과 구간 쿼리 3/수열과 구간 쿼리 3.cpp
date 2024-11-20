#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    for (auto q:queries){
        int tmp = arr[q[0]];
        arr[q[0]] = arr[q[1]];
        arr[q[1]] = tmp;
    }
    return arr;
}