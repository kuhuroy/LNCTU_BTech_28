#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {

        int windowSum = 0;

        // First window
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }

        int maxSum = windowSum;

        // Sliding window
        for (int i = k; i < nums.size(); i++) {
            windowSum += nums[i];
            windowSum -= nums[i - k];

            maxSum = max(maxSum, windowSum);
        }

        return (double)maxSum / k;
    }
};

int main() {

    Solution s;

    vector<int> nums = {1, 12, -5, -6, 50, 3};
    int k = 4;

    cout << s.findMaxAverage(nums, k);

    return 0;
}