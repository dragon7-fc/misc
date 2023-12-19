825. Friends Of Appropriate Ages

Some people will make friend requests. The list of their ages is given and `ages[i]` is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

* `age[B] <= 0.5 * age[A] + 7`
* `age[B] > age[A]`
* `age[B] > 100 && age[A] < 100`

Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

**Example 1:**
```
Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
```

**Example 2:**
```
Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
```

**Example 3:**
```
Input: [20,30,100,110,120]
Output: 
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
``` 

**Notes:**

* `1 <= ages.length <= 20000`.
* `1 <= ages[i] <= 120`.

# Solution
---
## Approach #1: Counting [Accepted]
**Intuition**

Instead of processing all 20000 people, we can process pairs of `(age, count)` representing how many people are that age. Since there are only 120 possible ages, this is a much faster loop.

**Algorithm**

For each pair `(ageA, countA), (ageB, countB)`, if the conditions are satisfied with respect to age, then `countA * countB` pairs of people made friend requests.

If `ageA == ageB`, then we overcounted: we should have `countA * (countA - 1)` pairs of people making friend requests instead, as you cannot friend request yourself.

```python
class Solution(object):
    def numFriendRequests(self, ages):
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(\mathcal{A}^2 + N)$ where $N$ is the number of people, and $\mathcal{A}$ is the number of ages.

* Space Complexity: $O(\mathcal{A})$, the space used to store count.

# Submissions
---
**Solution: (Counting)**
```
Runtime: 452 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA

        return ans
```

**Solution 1: (Counting)**
```
Runtime: 74 ms
Memory Usage: 37.3 MB
```
```c++
class Solution {
public:
    int numFriendRequests(vector<int>& ages) {
        int n=ages.size(), ages_count[121]={0};
        for(int i=0;i<n;++i) ages_count[ages[i]]++;
        
        int friend_request=0;
        for(int i=1;i<=120;i++){
            for(int j=1;j<=120;++j){
                if(i<=0.5*double(j)+7 ||  i>j || (i>100 && j<100)) continue;
                if(i==j) friend_request+=(ages_count[i]-1)*(ages_count[i]);
                else friend_request+=(ages_count[i])*(ages_count[j]);
            }
        }
        
        return friend_request;
    }
};
```

**Solution 2: (Binary Search)**
```
Runtime: 47 ms
Memory: 37.6 MB
```
```c++
class Solution {
public:
    int numFriendRequests(vector<int>& ages) {
        sort(ages.begin(), ages.end());
        int ans = 0;
        auto it = upper_bound(ages.begin(), ages.end(), 14);
        while (it != ages.end())
        {
            auto it2 = upper_bound(ages.begin(), ages.end(), *it);
            
            ans += (it2-it)*max((int)(prev(it2) - upper_bound(ages.begin(), ages.end(), 0.5*(*it) +7)), 0);
            
            it = it2;
        }
        return ans;
    }
};
```

**Solution 3: (Counting)**
```
Runtime: 39 ms
Memory: 37.9 MB
```
```c++
class Solution {
    bool request(int a, int b) {
        return !(b <= 0.5 * a + 7 || b > a || (b > 100 && a < 100));
    }
public:
    int numFriendRequests(vector<int>& ages) {
        unordered_map<int, int> count;
        for (int &age : ages)
            count[age]++;
        int res = 0;
        for (auto &a : count)
            for (auto &b : count)
                if (request(a.first, b.first))
                    res += a.second * (b.second - (a.first == b.first ? 1 : 0));
        return res;
    }
};
```
