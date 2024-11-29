#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> two_idx;
    for (int i=0; i<arr.size(); i++)
        if (arr[i] == 2) two_idx.emplace_back(i);
    
    if (two_idx.empty()) return {-1};
    else
        return vector<int>(arr.begin() + two_idx.front(), arr.begin() + two_idx.back() + 1);
}