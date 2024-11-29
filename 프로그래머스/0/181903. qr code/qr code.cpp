#include <string>
#include <vector>

using namespace std;

string solution(int q, int r, string code) {
    string answer = "";
    while (r < code.size()){
        answer += code[r];
        r += q;
    }
    return answer;
}