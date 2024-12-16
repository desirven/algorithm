#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    int n=1;
    int init_len=arr.size();
    while (n<init_len){
        n *= 2;
    }
    for (int i=0; i<n-init_len; i++) arr.emplace_back(0);    
    return arr;
}