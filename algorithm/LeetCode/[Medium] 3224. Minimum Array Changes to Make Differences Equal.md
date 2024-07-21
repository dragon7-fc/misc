3224. Minimum Array Changes to Make Differences Equal

You are given an integer array `nums` of size `n` where `n` is even, and an integer `k`.

You can perform some changes on the array, where in one change you can replace any element in the array with any integer in the range from `0` to `k`.

You need to perform some changes (possibly none) such that the final array satisfies the following condition:

* There exists an integer `X` such that `abs(a[i] - a[n - i - 1]) = X` for all (`0 <= i < n`).

Return the **minimum** number of changes required to satisfy the above condition.

 

**Example 1:**
```
Input: nums = [1,0,1,2,4,3], k = 4

Output: 2

Explanation:
We can perform the following changes:

Replace nums[1] by 2. The resulting array is nums = [1,2,1,2,4,3].
Replace nums[3] by 3. The resulting array is nums = [1,2,1,3,4,3].
The integer X will be 2.
```

**Example 2:**
```
Input: nums = [0,1,2,3,3,6,5,4], k = 6

Output: 2

Explanation:
We can perform the following operations:

Replace nums[3] by 0. The resulting array is nums = [0,1,2,0,3,6,5,4].
Replace nums[4] by 4. The resulting array is nums = [0,1,2,0,4,6,5,4].
The integer X will be 4.
```
 

**Constraints:**

* `2 <= n == nums.length <= 10^5`
* `n` is even.
* `0 <= nums[i] <= k <= 10^5`

# Submissions
---
**Solution 1: (Counter, Binary Search)**

__Intuition__
what can be possible values of X
it's 0 to k
Now we will check for all possible values what is the minimum.
For each pair for a X number of changes required may be
0 : If both are equal
1 : If changing one we can achieve the target
2 : If we need to change both.
Now let's focus on case 1 and case 2
suppose the pair is a,b and a < b
So in one change what can be max X???
What can we do in one move.
convert a->0 : in this case max X can be b
convert b->k : in this case max X can be k-a
so in one change we can have maximum X threshold = max(max(a, b), k - min(a, b))
If X> threshold we need 2 changes.

__Approach__
We have stored all this boundary value for which we need 2 changes for a particular pair.
Later using binary search we can found easily how many 2 changes operation required for a particular X value in a faster way.
We have also stored the initial difference in a freq vector.

__Complexity__
Time complexity: O(n+n∗logn(n)+k∗log(n))
Space complexity: O(k+n/2) //Freq vector [size : k]

```
Runtime: 175 ms
Memory: 102.68 MB
```
```c++
class Solution {
public:
    int minChanges(vector<int>& nums, int k) {
        vector<int> freq(k+1);
        vector<int> v;
        int n = nums.size();
        for (int i = 0; i < n / 2; i++){
            int dif = abs(nums[i] - nums[n - i - 1]);
            freq[dif]++;

            int a = nums[i], b = nums[n - i - 1];
            int threshold = max(max(a, b), k - min(a, b));
            v.push_back(threshold);
        }

        sort(v.begin(), v.end());

        int ans = n / 2;
        n /= 2;
        for (int i = 0; i < freq.size(); i++)
        {
            int rest = n - freq[i];
            int greater = lower_bound(v.begin(), v.end(), i) - v.begin();
            ans = min(ans, rest + greater);
        }
        return ans;
    }
};
```

**Solution 2: (Counter, Prefix sum)**
```
Runtime: 126 ms
Memory: 111.74 MB
```
```c++
class Solution {
public:
    int minChanges(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        int n = nums.size();
        vector<int> maxGap(k+1,0);
        for(int i=0;i<n/2;i++){
            int diff = abs(nums[i]-nums[n-i-1]);
            mp[diff]++;
            int gap1 = k-min(nums[i],nums[n-i-1]);
            int gap2 = max(nums[i],nums[n-i-1])-0;
            int gap = max(gap1,gap2);
            maxGap[gap]++;
        }
        for(int i=k-1;i>=0;i--){
            maxGap[i] = maxGap[i]+maxGap[i+1];
// If a differnce can be i+1 then it can also be i.
        }
        int ans = INT_MAX;
        for(auto &a: mp){
            if(maxGap[a.first]==n/2){
                int to_be_changed = n/2 - a.second;
                ans = min(ans,to_be_changed);
            }
            else{
                int one_element_change = maxGap[a.first]-a.second;
                int two_element_change = (n/2-maxGap[a.first])*2;
                int total = one_element_change+two_element_change;
                ans = min(ans,total);
            }
            
        }
        return ans;
    }
};
```
