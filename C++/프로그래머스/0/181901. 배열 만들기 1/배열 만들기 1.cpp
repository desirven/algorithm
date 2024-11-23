#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int k) {
    vector<int> answer;
    int num = k;
    while (num <= n){
        answer.push_back(num);
        num += k;
    }
    return answer;
}