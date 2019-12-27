553. Optimal Division

Given a list of **positive integers**, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. **Your expression should NOT contain redundant parenthesis**.

**Example:**
```
Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
since they don't influence the operation priority. So you should return "1000/(100/10/2)". 

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
```

**Note:**

1. The length of the input array is `[1, 10]`.
1. Elements in the given array will be in range `[2, 1000]`.
1. There is only one optimal division for each test case.

# Solution
---
## Approach #1 Brute Force [Accepted]
**Algorithm**

Brute force of this problem is to divide the list into two parts $left$ and $right$ and call function for these two parts. We will iterate $i$ from $start$ to $end$ so that $left=(start,i)$ and $right=(i+1,end)$.

$left$ and $right$ parts return their maximum and minimum value and corresponding strings.

Minimum value can be found by dividing minimum of left by maximum of right i.e. $minVal=left.min/right.max$.

Similarly,Maximum value can be found by dividing maximum of left value by minimum of right value. i.e. $maxVal=left.max/right.min$.

Now, how to add parenthesis? As associativity of division operator is from left to right i.e. by default left most divide should be done first, we need not have to add paranthesis to the left part, but we must add parenthesis to the right part.

eg- "2/(3/4)" will be formed as leftPart+"/"+"("+rightPart+")", assuming leftPart is "2" and rightPart is"3/4".

One more point, we also don't require parenthesis to right part when it contains single digit.

eg- "2/3", here left part is "2" and right part is "3" (contains single digit) . 2/(3) is not valid.

```java
public class Solution {
    public String optimalDivision(int[] nums) {
        T t = optimal(nums, 0, nums.length - 1, "");
        return t.max_str;
    }
    class T {
        float max_val, min_val;
        String min_str, max_str;
    }
    public T optimal(int[] nums, int start, int end, String res) {
        T t = new T();
        if (start == end) {
            t.max_val = nums[start];
            t.min_val = nums[start];
            t.min_str = "" + nums[start];
            t.max_str = "" + nums[start];
            return t;
        }
        t.min_val = Float.MAX_VALUE;
        t.max_val = Float.MIN_VALUE;
        t.min_str = t.max_str = "";
        for (int i = start; i < end; i++) {
            T left = optimal(nums, start, i, "");
            T right = optimal(nums, i + 1, end, "");
            if (t.min_val > left.min_val / right.max_val) {
                t.min_val = left.min_val / right.max_val;
                t.min_str = left.min_str + "/" + (i + 1 != end ? "(" : "") + right.max_str + (i + 1 != end ? ")" : "");
            }
            if (t.max_val < left.max_val / right.min_val) {
                t.max_val = left.max_val / right.min_val;
                t.max_str = left.max_str + "/" + (i + 1 != end ? "(" : "") + right.min_str + (i + 1 != end ? ")" : "");
            }
        }
        return t;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n!)$. Number of permutations of expression after applying brackets will be in $O(n!)$ where $n$ is the number of items in the list.

* Space complexity: $O(n^2)$. Depth of recursion tree will be $O(n)$ and each node contains string of maximum length $O(n)$.

## Approach #2 Using Memorization [Accepted]
**Algorithm**

In the above approach we called optimal function recursively for ever $start$ and $end$. We can notice that there are many redundant calls in the above approach, we can reduce these calls by using memorization to store the result of different function calls. Here, $memo$ array is used for this purpose.

```java
public class Solution {
    class T {
        float max_val, min_val;
        String min_str, max_str;
    }
    public String optimalDivision(int[] nums) {
        T[][] memo = new T[nums.length][nums.length];
        T t = optimal(nums, 0, nums.length - 1, "", memo);
        return t.max_str;
    }
    public T optimal(int[] nums, int start, int end, String res, T[][] memo) {
        if (memo[start][end] != null)
            return memo[start][end];
        T t = new T();
        if (start == end) {
            t.max_val = nums[start];
            t.min_val = nums[start];
            t.min_str = "" + nums[start];
            t.max_str = "" + nums[start];
            memo[start][end] = t;
            return t;
        }
        t.min_val = Float.MAX_VALUE;
        t.max_val = Float.MIN_VALUE;
        t.min_str = t.max_str = "";
        for (int i = start; i < end; i++) {
            T left = optimal(nums, start, i, "", memo);
            T right = optimal(nums, i + 1, end, "", memo);
            if (t.min_val > left.min_val / right.max_val) {
                t.min_val = left.min_val / right.max_val;
                t.min_str = left.min_str + "/" + (i + 1 != end ? "(" : "") + right.max_str + (i + 1 != end ? ")" : "");
            }
            if (t.max_val < left.max_val / right.min_val) {
                t.max_val = left.max_val / right.min_val;
                t.max_str = left.max_str + "/" + (i + 1 != end ? "(" : "") + right.min_str + (i + 1 != end ? ")" : "");
            }
        }
        memo[start][end] = t;
        return t;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n^3)$. $memo$ array of size $n^2$ is filled and filling of each cell of the $memo$ array takes $O(n)$ time.

* Space complexity : $O(n^3)$. $memo$ array of size $n^2$ where each cell of array contains string of length $O(n)$.

## Approach #3 Using some Math [Accepted]
**Algorithm**

Using some simple math we can find the easy solution of this problem. Consider the input in the form of [a,b,c,d], now we have to set priority of operations to maximize a/b/c/d. We know that to maximize fraction $p/q$, $q$(denominator) should be minimized. So, to maximize $a/b/c/d$ we have to first minimize b/c/d. Now our objective turns to minimize the expression b/c/d.

There are two possible combinations of this expression, b/(c/d) and (b/c)/d.
```
b/(c/d)        (b/c)/d = b/c/d
(b*d)/c        b/(d*c)
d/c            1/(d*c)
```
Obviously, $d/c > 1/(d*c)$ for $d>1$.

You can see that second combination will always be less than first one for numbers greater than $1$. So, the answer will be a/(b/c/d). Similarly for expression like a/b/c/d/e/f... answer will be a/(b/c/d/e/f...).

```java
public class Solution {
    public String optimalDivision(int[] nums) {
        if (nums.length == 1)
            return nums[0] + "";
        if (nums.length == 2)
            return nums[0] + "/" + nums[1];
        StringBuilder res = new StringBuilder(nums[0] + "/(" + nums[1]);
        for (int i = 2; i < nums.length; i++) {
            res.append("/" + nums[i]);
        }
        res.append(")");
        return res.toString();
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. Single loop to traverse $nums$ array.

* Space complexity : $O(n)$. $res$ variable is used to store the result.

# Submissions
---
**Solution 1:**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0])+'/'+str(nums[1])
        return str(nums[0]) + '/(' + '/'.join(list(map(str,nums[1:]))) + ')'
```