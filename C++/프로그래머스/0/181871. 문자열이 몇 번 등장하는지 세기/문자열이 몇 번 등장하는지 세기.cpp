#include <string>
#include <vector>

using namespace std;

int solution(string myString, string pat) {
    int answer = 0;
    for (int i=0; i<myString.size()-pat.size()+1; i++)
        if (pat==myString.substr(i,pat.size())) answer += 1;
    return answer;
}