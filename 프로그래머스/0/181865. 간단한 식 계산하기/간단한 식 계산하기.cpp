#include <string>
#include <vector>

using namespace std;

int solution(string binomial) {
    int answer = 0;
    char op;
    
    int s = binomial.find(' ');
    int num1 = stoi(binomial.substr(0, s));
    op = binomial[s+1]; 
    int num2 = stoi(binomial.substr(s+3));
    
    if(op=='*')return num1*num2;
    else if(op=='+')return num1+num2;
    else return num1-num2;
    return answer;
}