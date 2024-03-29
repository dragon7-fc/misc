2300. Successful Pairs of Spells and Potions

You are given two positive integer arrays `spells` and `potions`, of length `n` and `m` respectively, where `spells[i]` represents the strength of the `i`th spell and `potions[j]` represents the strength of the `j`th potion.

You are also given an integer `success`. A spell and potion pair is considered **successful** if the **product** of their strengths is **at least** `success`.

Return an integer array `pairs` of length `n` where `pairs[i]` is the number of **potions** that will form a successful pair with the `i`th spell.

 

**Example 1:**
```
Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
```

**Example 2:**
```
Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
```

**Constraints:**

* `N == SPELLS.LENGTH`
* `M == POTIONS.LENGTH`
* `1 <= N, M <= 10^5`
* `1 <= SPELLS[I], POTIONS[I] <= 10^5`
* `1 <= SUCCESS <= 10^10`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 1470 ms
Memory Usage: 37.7 MB
```
```python
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        return [len(potions) - bisect_left(potions, (success + a - 1) // a) for a in spells]
```

**Solution 2: (Binary Search)**
```
Runtime: 455 ms
Memory Usage: 99.9 MB
```
```c++
class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        vector<int> res;
        for (int a: spells) {
            long need = (success + a - 1) / a;
            auto it = lower_bound(potions.begin(), potions.end(), need);
            res.push_back(potions.end() - it);
        }
        return res;
    }
};
```

**Solution 3: (Binary Search)**
```
Runtime: 173 ms
Memory: 97.6 MB
```
```c++
class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        int N = spells.size(), M = potions.size(), spell, left, right, mid;
        long long product;
        vector<int> ans(N);
        sort(potions.begin(), potions.end());
        for (int i = 0; i < N; i++) {
            spell = spells[i];
            left = 0;
            right = M - 1;
            while (left < right) {
                mid = left + (right - left) / 2;
                product = (long long)spell * (long long)potions[mid];
                if (product < success) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            ans[i] = M - left - ((long long)spell * (long long)potions[left] < success);
        }
        return ans;
    }
};
```
