C++

1) Brute Force [O(n^2)]
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        int size = nums.size();
        for(int i=0 ; i < size - 1 ;i++)
        {
            for(int j = i+1 ; j<size ; j++)
            {
                if(nums[i]+nums[j] == target)
                {
                    ret.push_back(i);
                    ret.push_back(j);
                    return ret;
                }   
            }
        }
        return ret;
    }
};

2) Hash Table [O(n)]
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        int size = nums.size();
        int diff;
        unordered_map<int,int>m;
        for (int i=0 ; i<size ; i++)
        {
            diff = target - nums[i];
            if(m.find(diff) != m.end() && m.find(diff) -> second != i )
            {
                ret.push_back(i);
                ret.push_back(m.find(diff) -> second);
                return ret;
            }
            m[nums[i]] = i;
        }
        return ret;
    }
};
