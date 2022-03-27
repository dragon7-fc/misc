949. Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

**Example 1:**
```
Input: [1,2,3,4]
Output: "23:41"
```

**Example 2:**
```
Input: [5,5,5,5]
Output: ""
```

**Note:**

1. `A.length == 4`
1. `0 <= A[i] <= 9`

# Solution
---
## Approach 1: Brute Force
**Intuition**

Try all possible times, and remember the largest one.

**Algorithm (Java)**

Iterate over all permutations `(i, j, k, l)` of `(0, 1, 2, 3)`. For each permutation, we can try the time `A[i]A[j] : A[k]A[l]`.

This is a valid time if and only if the number of hours `10*A[i] + A[j]` is less than `24`; and the number of minutes `10*A[k] + A[l]` is less than `60`.

We will output the largest valid time.

**Algorithm (Python)**

For each possible ordering of the 4 digits, if it's a legal time and the time is greater than the one we have stored, update the answer.

```python
class Solution(object):
    def largestTimeFromDigits(self, A):
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""
```

**Complexity Analysis**

* Time Complexity: $O(1)$.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution: (Brute Force)**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""
```

**Solution 1: (Permutation via Backtracking)**
```
Runtime: 44 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        max_time = -1

        def build_time(permutation):
            nonlocal max_time

            h, i, j, k = permutation
            hour = h*10 + i
            minute = j*10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)

        def swap(array, i, j):
            if i != j:
                array[i], array[j] = array[j], array[i]

        def permutate(array, start):
            if start == len(array):
                build_time(array)
                return

            for index in range(start, len(array)):
                swap(array, index, start)
                # repeat the permutation with the original array mutated
                permutate(array, start+1)
                swap(array, index, start)

        permutate(A, 0)
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
```

**Solution 2: (Brute Force0**
```
Runtime: 4 ms
Memory Usage: 9.6 MB
```
```c++
class Solution {
public:
    string largestTimeFromDigits(vector<int>& arr) {
        string result;
        for(int i=0;i<=3;++i){
           for(int j=0;j<=3;++j){
                for(int k=0;k<=3;++k){
                    if(i==j or j==k or k==i)
                        continue;
                    string hh = to_string(arr[i]) + to_string(arr[j]);
                    string mm = to_string(arr[k]) + to_string(arr[6-i-j-k]);
                    
                    string temp = hh + ":" + mm;
                    
                    if(hh < "24" and mm < "60" and temp > result){
                        result = temp;
                    }
                }
            } 
        }
        
        return result;
    }
};
```
