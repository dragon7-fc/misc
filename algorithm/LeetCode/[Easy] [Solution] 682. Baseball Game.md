682. Baseball Game

You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

* Integer (one round's score): Directly represents the number of points you get in this round.
* `"+"` (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
* `"D"` (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
* `"C"` (an operation, which isn't a round's score): Represents the last `valid` round's points you get were invalid and should be removed.

Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

**Example 1:**
```
Input: ["5","2","C","D","+"]
Output: 30
Explanation: 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2's data was invalid. The sum is: 5.  
Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.
```

**Example 2:**
```
Input: ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation: 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get -2 points. The sum is: 3.
Round 3: You could get 4 points. The sum is: 7.
Operation 1: The round 3's data is invalid. The sum is: 3.  
Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
Round 5: You could get 9 points. The sum is: 8.
Round 6: You could get -4 + 9 = 5 points. The sum is 13.
Round 7: You could get 9 + 5 = 14 points. The sum is 27.
```

**Note:**

* The size of the input list will be between `1` and `1000`.
* Every integer represented in the list will be between `-30000` and `30000`.

# Solution
---
## Approach #1: Stack [Accepted]
**Intuition and Algorithm**

Let's maintain the value of each valid round on a stack as we process the data. A stack is ideal since we only deal with operations involving the last or second-last valid round.

```python
class Solution(object):
    def calPoints(self, ops):
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of ops. We parse through every element in the given array once, and do $O(1)$ work for each element.

* Space Complexity: $O(N)$, the space used to store our stack.

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 40 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)
```

**Solution 2: (Stack)**
```
Runtime: 4 ms
Memory Usage: 6.4 MB
```
```c


int calPoints(char ** ops, int opsSize){
    int* stack = (int*) malloc(sizeof(int) * opsSize);
    if (!stack) {
        exit(1);
    }
    int sp = -1, tmp = 0, sum = 0, i = 0;
    for (i = 0; i < opsSize; i++) {
        if (**(ops+i) == 'C') {
            if (sp > -1) {
                sum -= stack[sp];
                sp--;
            }
            continue;
        } else if (**(ops+i) == 'D') {
            tmp = 2*stack[sp];
            stack[++sp] = tmp;
        } else if (**(ops+i) == '+') {
            tmp = stack[sp] + stack[sp - 1];
            stack[++sp] = tmp;
        } else {
            stack[++sp] = atoi(*(ops+i));
        }
        sum += stack[sp];
    }
    free(stack);
    return sum;
}
```

**Solution 3: (Stack)**
```
Runtime: 3 ms, Beats 15.73%
Memory: 11.92 MB, Beats 79.75%
```
```c++
class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> ans;
        for (auto op: operations) {
            if (op == "+") {
                ans.push_back(ans[ans.size()-1] + ans[ans.size()-2]);
            } else if (op == "D") {
                ans.push_back(2*ans.back());
            } else if (op == "C") {
                ans.pop_back();
            } else {
                ans.push_back(stoi(op));
            }
        }
        return accumulate(ans.begin(), ans.end(), 0);
    }
};
```
