#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    bool is_odd = n%2;
    int answer = 0;
    for (auto x=n; x>0; x-=2){
        if (is_odd)
            answer += x;
        else 
            answer += x*x;
    }
    return answer;
}