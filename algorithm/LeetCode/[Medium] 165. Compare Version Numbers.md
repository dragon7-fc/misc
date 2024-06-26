165. Compare Version Numbers

Compare two version numbers `version1` and `version2`.
If `version1 > version2 return 1`; `if version1 < version2 return -1`;otherwise return `0`.

You may assume that the version strings are non-empty and contain only digits and the `.` character.

The `.` character does not represent a decimal point and is used to separate number sequences.

For instance, `2.5` is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be `0`. For example, version number `3.4` has a revision number of `3` and 4 for its first and second level revision number. Its third and fourth level revision number are both `0`.

 

**Example 1:**
```
Input: version1 = "0.1", version2 = "1.1"
Output: -1
```

**Example 2:**
```
Input: version1 = "1.0.1", version2 = "1"
Output: 1
```

**Example 3:**
```
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
```

**Example 4:**
```
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”
```

**Example 5:**
```
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"
```

**Note:**

* Version strings are composed of numeric strings separated by dots `.` and this numeric strings may have leading zeroes.
* Version strings do not start or end with dots, and they will not be two consecutive dots.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Create two arrays by splitting on the '.'
        arr_1 , arr_2 = version1.split('.'), version2.split('.')
        # treate these arras like queues, dequing it each iteration, 
        # if the queue ran out, set it to zero since '1.0.0.0' == '1'
        while arr_1 or arr_2:
            val_1 = int(arr_1.pop(0)) if arr_1 else 0
            val_2 = int(arr_2.pop(0)) if arr_2 else 0
            # if at any point version 1 is greater than version 2, 
            if val_1 > val_2:
                return 1
            # if 2 is greater than 1 return -1
            if val_2 > val_1:
                return -1
        # if we make it to the end it was equal so return zero 
        return 0
```

**Solution 2: (Greedy)**
```
Runtime: 28 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in itertools.zip_longest(version1.split('.'), version2.split('.')):
            v1 = int(v1) if v1 else 0
            v2 = int(v2) if v2 else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
```

**Solution 3: (Greedy)**
```
Runtime: 0 ms
Memory Usage: 6.4 MB
```
‵``c++
class Solution {
public:
    int compareVersion(string version1, string version2) {
        vector<int> v1, v2;
        stringstream ss(version1);
        string str;
        while (getline(ss, str, '.')) {
            v1.push_back(stoi(str));
        }
        ss = stringstream(version2);
        str.erase();
        while (getline(ss, str, '.')) {
            v2.push_back(stoi(str));
        }
        int n1, n2;
        for (int i = 0; i < max(v1.size(), v2.size()); i++) {
            n1 = (i < v1.size() ? v1[i] : 0);
            n2 = (i < v2.size() ? v2[i] : 0);
            if (n1 < n2)
                return -1;
            else if (n1 > n2)
                return 1;
        }
        return 0;
    }
};
```

**Solution 4: (Greedy)**
```
Runtime: 0 ms
Memory: 7.48 MB
```
```c++
class Solution {
public:
    int compareVersion(string version1, string version2) {
        int i = 0, j = 0, n1 = version1.size(), n2 = version2.size(), a = 0, b = 0; 
        while (i < n1 || j < n2) {
            while (i < n1 && version1[i] != '.') {
                a = a*10 + (version1[i]-'0');
                i += 1;
            }
            while (j < n2 && version2[j] != '.') {
                b = b*10 + (version2[j]-'0');
                j += 1;
            }
            if (a > b) {
                return 1;
            } else if (a < b) {
                return -1;
            }
            i += 1;
            j += 1;
            a = 0;
            b = 0;
        }
        return 0; 
    }
};
```
