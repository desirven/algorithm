#include <string>
#include <vector>

using namespace std;

int solution(int a, int d, vector<bool> included) {
    int answer = 0;
    for (auto b : included){
        answer += a*b;
        a += d;
    }
    return answer;
}