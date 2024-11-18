#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    string stra = to_string(a);
    string strb = to_string(b);
    stra += strb;
    int answer = stoi(stra);
    return answer>2*a*b ? answer : 2*a*b;
}