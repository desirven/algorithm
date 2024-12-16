#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(string myString) {
    vector<string> answer;
    string tmp = "";
    for (char c:myString){
        if (c=='x'){
            if (tmp != "") answer.emplace_back(tmp);
            tmp = "";
        } else tmp += c;
    }
    if (tmp != "") answer.emplace_back(tmp);
    std::sort(answer.begin(), answer.end());
    return answer;
}