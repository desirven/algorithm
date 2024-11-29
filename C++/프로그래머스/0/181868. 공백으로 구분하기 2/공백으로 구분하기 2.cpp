#include <string>
#include <vector>

using namespace std;

vector<string> solution(string my_string) {
    vector<string> answer;
    string tmp="";
    for (auto c:my_string){
        if (c==' ' && tmp!="") {
            answer.emplace_back(tmp);
            tmp = "";
        }
        else if (c==' ' && tmp=="") tmp = "";
        else tmp += c;
    }
    if (tmp!="") answer.emplace_back(tmp);
    return answer;
}