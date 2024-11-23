#include <string>
#include <vector>

using namespace std;

vector<int> solution(string my_string) {
    vector<int> answer;
    answer.assign(52, 0);
    
    for (char c:my_string){
        if (c >= 'A' && c <= 'Z')
            answer[c-'A'] += 1;
        else
            answer[c-'a'+26] += 1;
    }
        
    return answer;
}