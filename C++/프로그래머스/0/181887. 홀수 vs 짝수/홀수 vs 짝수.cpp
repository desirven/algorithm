#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int sum_odd = 0;
    int sum_even = 0;
    for (int i=0; i<num_list.size(); i += 2){
        sum_odd += num_list[i];
        sum_even += num_list[i+1];
    }
    return max(sum_odd, sum_even);
}