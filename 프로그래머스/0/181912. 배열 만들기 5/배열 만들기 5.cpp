#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> intStrs, int k, int s, int l) {
    vector<int> answer;
    for (auto intStr:intStrs){
        int subInt = stoi(intStr.substr(s, l));
        if (subInt > k)
            answer.push_back(subInt);
    }
    return answer;
}