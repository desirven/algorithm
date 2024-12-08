#include <string>
#include <vector>

using namespace std;

int solution(vector<string> strArr) {
    int cnt[30] = {0, };
    int answer = 0;
    for (auto s:strArr){
        cnt[s.size()-1]++;
        answer = cnt[s.size()-1]>answer ? cnt[s.size()-1]:answer;
    }
    return answer;
}