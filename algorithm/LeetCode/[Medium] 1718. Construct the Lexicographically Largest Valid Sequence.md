1718. Construct the Lexicographically Largest Valid Sequence

Given an integer `n`, find a sequence that satisfies all of the following:

* The integer `1` occurs once in the sequence.
* Each integer between `2` and `n` occurs twice in the sequence.
* For every integer `i` between `2` and `n`, the distance between the two occurrences of `i` is exactly `i`.
* The distance between two numbers on the sequence, `a[i]` and `a[j]`, is the absolute difference of their indices, `|j - i|`.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than `a` sequence `b` (of the same length) if in the first position where `a` and `b` differ, sequence `a` has a number greater than the corresponding number in `b`. For example, `[0,1,9,0]` is lexicographically larger than `[0,1,5,6]` because the first position they differ is at the third number, and `9` is greater than `5`.

 

**Example 1:**
```
Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
```

**Example 2:**
```
Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
```

**Constraints:**

* `1 <= n <= 20`

# Submissions
---
**Solution 1: (Greedy, more smaller current more larger result)**
```
Runtime: 92 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [0]*(2*n-1)     # the array we want to put numbers. 0 means no number has been put here
        i = 0                 # current index to put a number                
        vi = [False] * (n+1)  # check if we have used that number
        
        # backtracking
        def dfs(arr, i, vi):
            # if we already fill the array successfully, return True
            if i >= (2*n-1):
                return True

            # try each number from n to 1
            for x in range(n, 0, -1):
                # two cases:
                # x > 1, we check two places. Mind index out of bound here.
                # x = 1, we only check one place
                # arr[i] == 0 means index i is not occupied
                if (x > 1 and ((not (arr[i] == 0 and (i+x < 2*n-1) and arr[i+x] == 0)) or vi[x]))  \
                    or (x == 1 and (arr[i] != 0 or vi[x])):
                    continue

                # if it can be placed, then place it
                if x > 1:
                    arr[i] = x
                    arr[i+x] = x
                else:
                    arr[i] = x
                vi[x] = True

                # find the next available place
                nexti = i+1
                while nexti < 2*n-1 and arr[nexti]:
                    nexti += 1

                # place the next one
                if dfs(arr, nexti, vi):
                    # if it success, it is already the lexicographically largest one, we don't search anymore
                    return True

                # backtracking... restore the state
                if x > 1:
                    arr[i] = 0
                    arr[i+x] = 0
                else:
                    arr[i] = 0
                vi[x] = False

            # we could not find a solution, return False
            return False

        dfs(arr, i, vi)
        return arr
```

**Solution 2: (Backtracking, O(n!))**
```
Runtime: 0 ms, Beats 100.00%
Memory: 8.64 MB, Beats 36.80%
```
```c++
class Solution {
    // Recursive function to generate the desired sequence
    bool findLexicographicallyLargestSequence(int currentIndex,
                                              vector<int>& resultSequence,
                                              vector<bool>& isNumberUsed,
                                              int targetNumber) {
        // If we have filled all positions, return true indicating success
        if (currentIndex == resultSequence.size()) {
            return true;
        }

        // If the current position is already filled, move to the next index
        if (resultSequence[currentIndex] != 0) {
            return findLexicographicallyLargestSequence(
                currentIndex + 1, resultSequence, isNumberUsed, targetNumber);
        }

        // Attempt to place numbers from targetNumber to 1 for a
        // lexicographically largest result
        for (int numberToPlace = targetNumber; numberToPlace >= 1;
             numberToPlace--) {
            if (isNumberUsed[numberToPlace]) continue;

            isNumberUsed[numberToPlace] = true;
            resultSequence[currentIndex] = numberToPlace;

            // If placing number 1, move to the next index directly
            if (numberToPlace == 1) {
                if (findLexicographicallyLargestSequence(
                        currentIndex + 1, resultSequence, isNumberUsed,
                        targetNumber)) {
                    return true;
                }
            }
            // Place larger numbers at two positions if valid
            else if (currentIndex + numberToPlace < resultSequence.size() &&
                     resultSequence[currentIndex + numberToPlace] == 0) {
                resultSequence[currentIndex + numberToPlace] = numberToPlace;

                if (findLexicographicallyLargestSequence(
                        currentIndex + 1, resultSequence, isNumberUsed,
                        targetNumber)) {
                    return true;
                }

                // Undo the placement for backtracking
                resultSequence[currentIndex + numberToPlace] = 0;
            }

            // Undo current placement and mark the number as unused
            resultSequence[currentIndex] = 0;
            isNumberUsed[numberToPlace] = false;
        }

        return false;
    }
public:
    vector<int> constructDistancedSequence(int n) {
       // Initialize the result sequence with size 2*n - 1 filled with 0s
        vector<int> resultSequence(n * 2 - 1, 0);

        // Keep track of which numbers are already placed in the sequence
        vector<bool> isNumberUsed(n + 1, false);

        // Start recursive backtracking to construct the sequence
        findLexicographicallyLargestSequence(0, resultSequence, isNumberUsed,
                                             n);

        return resultSequence;
    }
};
```

**Solution 3: (Backtracking, O(n!))**
```
Runtime: 0 ms, Beats 100.00%
Memory: 8.52 MB, Beats 64.94%
```
```c++
class Solution {
    bool bt(int i, vector<bool> &visited, vector<int> &ans) {
        if (i == ans.size()) {
            return true;
        }
        if (ans[i] != 0) {
            return bt(i+1, visited, ans);
        }
        for (int a = visited.size()-1; a >= 1; a--) {
            if (!visited[a]) {
                visited[a] = true;
                ans[i] = a;
                if (a == 1) {
                    if (bt(i+1, visited, ans)) {
                        return true;
                    }
                } else if (i + a < ans.size() && ans[i+a] == 0) {
                    ans[i+a] = a;
                    if (bt(i+1, visited, ans)) {
                        return true;
                    }
                    ans[i+a] = 0;
                }
                visited[a] = false;
                ans[i] = 0;
            }
        }
        return false;
    }
public:
    vector<int> constructDistancedSequence(int n) {
        vector<int> ans(2*n - 1);
        vector<bool> visited(n+1);
        bt(0, visited, ans);
        return ans;
    }
};
```
