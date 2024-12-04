#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    for (int num:arr){
        for (int i=num; i>0; i--)
            answer.emplace_back(num);
    }
    return answer;
}