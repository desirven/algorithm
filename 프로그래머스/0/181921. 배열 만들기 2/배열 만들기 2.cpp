#include <string>
#include <vector>

using namespace std;

vector<int> solution(int l, int r) {
    vector<int> answer;
    for(int i=l; i<=r; i++){
        bool flag = true;
        for(char c : to_string(i)){            
            if (c != '0' && c != '5'){
                flag = false;
                break;
            }
        }
        if (flag)
            answer.push_back(i);
    }
    if (answer.empty())
        answer.push_back(-1);
    return answer;
}