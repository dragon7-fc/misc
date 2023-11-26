899. Orderly Queue

A string `S` of lowercase letters is given.  Then, we may make any number of moves.

In each move, we choose one of the first `K` letters (starting from the left), remove it, and place it at the end of the string.

Return the lexicographically smallest string we could have after any number of moves.

 

**Example 1:**
```
Input: S = "cba", K = 1
Output: "acb"
Explanation: 
In the first move, we move the 1st character ("c") to the end, obtaining the string "bac".
In the second move, we move the 1st character ("b") to the end, obtaining the final result "acb".
```

**Example 2:**
```
Input: S = "baaca", K = 3
Output: "aaabc"
Explanation: 
In the first move, we move the 1st character ("b") to the end, obtaining the string "aacab".
In the second move, we move the 3rd character ("c") to the end, obtaining the final result "aaabc".
```

**Note:**

* `1 <= K <= S.length <= 1000`
* `S` consists of lowercase letters only.

# Solution
---
## Approach 1: Mathematical
**Intuition**

Call the move that takes the Kth letter from the beginning and puts it on the end, a "K-kick" move.

Examining 1-kick moves, they let us consider the string as a "necklace" that may be rotated freely, where each bead of the necklace corresponds to a letter in the string. (Formally, this is the equivalence class under 1-kick moves.)

Examining 2-kick moves (in the context of treating the string as a necklace), they allow us to swap the positions of two adjacent beads. Thus, with 2-kick moves, every permutation of necklace is possible. (To actually construct the necklace, we bring the second smallest bead to be after the smallest, then the third smallest to be after the second smallest, and so on.)

The previous insight may be difficult to find. Another strategy is to write a brute force program to examine the result of 2-kick moves - then we might notice that 2-kick moves allow any permutation of the string.

Yet another strategy might be to explicitly construct new moves based on previous moves. If we perform a 2 kick move followed by many 1 kick moves, we can move a string like `"xyzzzzzz" -> "xzzzzzzy" -> "yxzzzzzz"`, proving we can swap the positions of any two adjacent letters.

**Algorithm**

If `K = 1`, only rotations of S are possible, and the answer is the smallest rotation.

If `K > 1`, any permutation of S is possible, and the answer is the letters of S written in lexicographic order.

```python
class Solution(object):
    def orderlyQueue(self, S, K):
        if K == 1:
            return min(S[i:] + S[:i] for i in range(len(S)))
        return "".join(sorted(S))
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of S.

* Space Complexity: $O(N^2)$.

# Submissions
---
**Solution: (Mathematical)**
```
Runtime: 36 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            return min(S[i:] + S[:i] for i in range(len(S)))
        return "".join(sorted(S))
```

**Solution 2: (sorting)**
```
Runtime: 5 ms
Memory: 8.8 MB
```
```c++
class Solution {
public:
    string orderlyQueue(string s, int k) {
        string ans;
        ans = s;
        if (k > 1) {
            sort(s.begin(), s.end());
            return (s);
        } else {
            string temp = s + s;
            for (int i = 0; i + s.length() <= temp.length(); i++) {
                ans = min(ans, temp.substr(i, s.length()));
            }
            return ans;
        }
    }
};
```
