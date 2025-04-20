22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

# Solution
---
## Approach 1: Brute Force
**Intuition**

We can generate all $2^{2n}$ sequences of `'('` and `')'` characters. Then, we will check if each one is valid.

**Algorithm**

To generate all sequences, we use a recursion. All sequences of length `n` is just `'('` plus all sequences of length `n-1`, and then `')'` plus all sequences of length `n-1`.

To check whether a sequence is valid, we keep track of balance, the net number of opening brackets minus closing brackets. If it falls below zero at any time, or doesn't end in zero, the sequence is invalid - otherwise it is valid.

```python
class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans
```

**Complexity Analysis**

* Time Complexity : $O(2^{2n}n)$. For each of $2^{2n}$ sequences, we need to create and validate the sequence, which takes $O(n)$ work.

* Space Complexity : $O(2^{2n}n)$. Naively, every sequence could be valid. See Approach 3 for development of a tighter asymptotic bound.

## Approach 2: Backtracking
**Intuition and Algorithm**

Instead of adding `'('` or `')'` every time as in Approach 1, let's only add them when we know it will remain a valid sequence. We can do this by keeping track of the number of opening and closing brackets we have placed so far.

We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.

```python
class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
```

**Complexity Analysis**

Our complexity analysis rests on understanding how many elements there are in `generateParenthesis(n)`. This analysis is outside the scope of this article, but it turns out this is the `n`-th Catalan number $\dfrac{1}{n+1}\binom{2n}{n}$, which is bounded asymptotically by $\dfrac{4^n}{n\sqrt{n}}$.

* Time Complexity : $O(\dfrac{4^n}{\sqrt{n}})$. Each valid sequence has at most `n` steps during the backtracking procedure.

* Space Complexity : $O(\dfrac{4^n}{\sqrt{n}})$, as described above, and using $O(n)$ space to store the sequence.

## Approach 3: Closure Number
**Intuition**

To enumerate something, generally we would like to express it as a sum of disjoint subsets that are easier to count.

Consider the closure number of a valid parentheses sequence `S`: the least `index >= 0` so that `S[0], S[1], ..., S[2*index+1]` is valid. Clearly, every parentheses sequence has a unique closure number. We can try to enumerate them individually.

**Algorithm**

For each closure number `c`, we know the starting and ending brackets must be at index `0` and `2*c + 1`. Then, the `2*c` elements between must be a valid sequence, plus the rest of the elements must be a valid sequence.

```python
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
```

**Complexity Analysis**

* Time and Space Complexity : $O(\dfrac{4^n}{\sqrt{n}})$. The analysis is similar to Approach 2.

# Submissions
---
**Solution: (Backtracking)**
```
Runtime: 64 ms
Memory Usage: N/A
```
```python
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
```

**Solution: (Backtracking)**
```python
Runtime: 36 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
```

**Solution: (Closure Number)**
```
Runtime: 68 ms
Memory Usage: N/A
```
```python
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
```

**Solution 1: (Backtracking, O(4^n / sqrt(n)))**
```
Runtime: 10 ms
Memory Usage: 15.6 MB
```
```c++
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        // result output string 
        string op = "";
        // number of total opening Parentheses
        int open_brct = n;
        // number of total closing Parentheses
        int close_brct = n;
        solve(open_brct,close_brct,op,res);
        return res;
    }
    
    void solve(int open_brct , int close_brct,string op,vector<string>& res){
        // this is the base condition if we have reached to the leaf of the tree we return
        if(open_brct == 0 && close_brct == 0){
            res.push_back(op);
            return ;
        }
        // we can include as many number of opening Parentheses as we want untill we are left with opening Parentheses 
        if(open_brct != 0){
            string op1 = op;
            op1.push_back('(');
       // after inserting open Parentheses we will decrease the total open Parentheses by 1 
            solve(open_brct-1,close_brct,op1,res);
        }
        // when ever closing Parentheses is higher than opening Parentheses we can insert closing Parentheses
        if(close_brct > open_brct)
        {
            string op2 = op;
            op2.push_back(')');
       // after inserting close Parentheses we will decrease the total close Parentheses by 1 
            solve(open_brct,close_brct-1,op2,res);
        }
        return ;
    }
};
```
