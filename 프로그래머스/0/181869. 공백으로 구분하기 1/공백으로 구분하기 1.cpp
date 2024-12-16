#include <string>
#include <vector>

using namespace std;

vector<string> solution(string my_string) {
    vector<string> answer;
    string tmp="";
    for (auto c:my_string){
        if (c==' ') {
            answer.emplace_back(tmp);
            tmp = "";
        }
        else tmp += c;
    }
    answer.emplace_back(tmp);
    return answer;
}