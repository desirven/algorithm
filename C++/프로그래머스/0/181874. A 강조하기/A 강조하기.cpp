#include <string>
#include <vector>

using namespace std;

string solution(string myString) {
    for (int i=0; i<myString.size(); i++){
        if (myString[i]=='a') myString[i] = 'A';
        else if ('A'<myString[i] && myString[i]<='Z') myString[i] = tolower(myString[i]);
    }
        
    return myString;
}