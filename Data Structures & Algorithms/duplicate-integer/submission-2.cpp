#include <unordered_map>
#include <vector>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> count_dict;
        for (int i = 0; i < nums.size(); i++) {
            if (count_dict.find(nums[i]) == count_dict.end()) {
                count_dict[nums[i]] = 1;
            } else {
                count_dict[nums[i]] += 1;
                if (count_dict[nums[i]] > 1) {
                    return true;
                }
            }
        }
        return false;
    }
};