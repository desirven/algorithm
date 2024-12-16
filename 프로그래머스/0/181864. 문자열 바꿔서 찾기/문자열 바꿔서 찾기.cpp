#include <string>
#include <vector>

using namespace std;

int solution(string myString, string pat) {
    for (int i; i<pat.size(); i++)
        pat[i] = (pat[i]=='B') ? 'A':'B';
    if (myString.find(pat)==string::npos) return 0;
    return 1;
}