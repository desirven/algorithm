#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int a, int b, int c) {
    int answer = 0;
    if (a==b and a==c) answer = 27*pow(a,6);
    else if (a!=b and a!=c and b!=c) answer = a+b+c;
    else answer = (a+b+c)*(a*a+b*b+c*c);
    return answer;
}