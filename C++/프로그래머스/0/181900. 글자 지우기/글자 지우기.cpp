#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string, vector<int> indices) {
    string answer = "";
    for (const auto i:indices)
        my_string[i] = '_';
    for (const auto c:my_string)
        if (c != '_') answer += c;
    return answer;
}