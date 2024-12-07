#include <string>
#include <vector>
#include <numeric>

using namespace std;

int solution(vector<int> arr1, vector<int> arr2) {
    if (arr1.size() > arr2.size()) return 1;
    else if (arr1.size() < arr2.size()) return -1;
    else {
        int arr1_sum = std::accumulate(std::begin(arr1), std::end(arr1), 0, std::plus<int>());
        int arr2_sum = std::accumulate(std::begin(arr2), std::end(arr2), 0, std::plus<int>());
        if (arr1_sum > arr2_sum) return 1;
        else if (arr1_sum < arr2_sum) return -1;
        else return 0;
    }
}