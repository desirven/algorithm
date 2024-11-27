#include <vector>

using namespace std;

int solution(vector<int> arr) {
    int count = 0;
    vector<int> prev;
    
    while (true) {
        prev = arr;
        for (int& num : arr) {
            if (num >= 50 && num % 2 == 0) {
                num /= 2;
            } else if (num < 50 && num % 2 == 1) {
                num = num * 2 + 1;
            }
        }
        
        count++;
        
        if (arr == prev) {
            return count-1;
        }
    }
}