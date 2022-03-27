640. Solve the Equation

Solve a given equation and return the value of `x` in the form of string "x=#value". The equation contains only '+', '-' operation, the variable `x` and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of `x` is an integer.

**Example 1:**
```
Input: "x+5-3+x=6+x-2"
Output: "x=2"
```

**Example 2:**
```
Input: "x=x"
Output: "Infinite solutions"
```

**Example 3:**
```
Input: "2x=x"
Output: "x=0"
```

**Example 4:**
```
Input: "2x+3x-6x=x+2"
Output: "x=-1"
```

**Example 5:**
```
Input: "x=x+2"
Output: "No solution"
```

# Solution
---
## Approach #1 Partioning Coefficients [Accepted]
In the current approach, we start by splitting the given $equation$ based on `=` sign. This way, we've separated the left and right hand side of this equation. Once this is done, we need to extract the individual elements(i.e. x's and the numbers) from both sides of the equation. To do so, we make use of `breakIt` function, in which we traverse over the given equation(either left hand side or right hand side), and put the separated parts into an array.

Now, the idea is as follows. We treat the given equation as if we're bringing all the `x`'s on the left hand side and all the rest of the numbers on the right hand side as done below for an example.

$x+5-3+x=6+x-2$

$x+x-x=6-2-5+3$

Thus, every `x` in the left hand side of the given equation is treated as positive, while that on the right hand side is treated as negative, in the current implementation.

Likewise, every number on the left hand side is treated as negative, while that on the right hand side is treated as positive. Thus, by doing so, we obtain all the x's in the new $lhs$ and all the numbers in the new $rhs$ of the original equation.

Further, in case of an `x`, we also need to find its corresponding coefficients in order to evaluate the final effective coefficient of `x` on the left hand side. We also evaluate the final effective number on the right hand side as well.

Now, in case of a unique solution, the ratio of the effective $rhs$ and $lhs$ gives the required result. In case of infinite solutions, both the effective $lhs$ and $rhs$ turns out to be zero e.g. `x+1=x+1`. In case of no solution, the coefficient of x($lhs$) turns out to be zero, but the effective number on the $rhs$ is non-zero.

```java

public class Solution {
    public String coeff(String x) {
        if (x.length() > 1 && x.charAt(x.length() - 2) >= '0' && x.charAt(x.length() - 2) <= '9')
            return x.replace("x", "");
        return x.replace("x", "1");
    }
    public String solveEquation(String equation) {
        String[] lr = equation.split("=");
        int lhs = 0, rhs = 0;
        for (String x: breakIt(lr[0])) {
            if (x.indexOf("x") >= 0) {
                lhs += Integer.parseInt(coeff(x));
            } else
                rhs -= Integer.parseInt(x);
        }
        for (String x: breakIt(lr[1])) {
            if (x.indexOf("x") >= 0)
                lhs -= Integer.parseInt(coeff(x));
            else
                rhs += Integer.parseInt(x);
        }
        if (lhs == 0) {
            if (rhs == 0)
                return "Infinite solutions";
            else
                return "No solution";
        }
        return "x=" + rhs / lhs;
    }
    public List < String > breakIt(String s) {
        List < String > res = new ArrayList < > ();
        String r = "";
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '+' || s.charAt(i) == '-') {
                if (r.length() > 0)
                    res.add(r);
                r = "" + s.charAt(i);
            } else
                r += s.charAt(i);
        }
        res.add(r);
        return res;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. Generating coefficients and findinn $lhs$ and $rhs$ will take $O(n)$.

* Space complexity : $O(n)$. ArrayList $res$ size can grow upto $n$.

## Approach #2 Using regex for spliting [Accepted]
**Algorithm**

In the last approach, we made use of a new function `breakIt` to obtain the individual components of either the left hand side or the right hand side. Instead of doing so, we can also make use of splitting based on `+` or `-` sign, to obtain the individual elements. The rest of the process remains the same as in the last approach.

In order to do the splitting, we make use of an expression derived from regular expressions(regex). Simply speaking, regex is a functionality used to match a target string based on some given criteria. The `?=n` quantifier, in regex, matches any string that is followed by a specific string $n$. What it's saying is that the captured match must be followed by $n$ but the $n$ itself isn't captured.

By making use of this kind of expression in the `split` functionality, we make sure that the partitions are obtained such that the `+` or `-` sign remains along with the parts(numbers or coefficients) even after the splitting.

```java

public class Solution {
    public String coeff(String x) {
        if (x.length() > 1 && x.charAt(x.length() - 2) >= '0' && x.charAt(x.length() - 2) <= '9')
            return x.replace("x", "");
        return x.replace("x", "1");
    }
    public String solveEquation(String equation) {
        String[] lr = equation.split("=");
        int lhs = 0, rhs = 0;
        for (String x: lr[0].split("(?=\\+)|(?=-)")) {
            if (x.indexOf("x") >= 0) {

                lhs += Integer.parseInt(coeff(x));
            } else
                rhs -= Integer.parseInt(x);
        }
        for (String x: lr[1].split("(?=\\+)|(?=-)")) {
            if (x.indexOf("x") >= 0)
                lhs -= Integer.parseInt(coeff(x));
            else
                rhs += Integer.parseInt(x);
        }
        if (lhs == 0) {
            if (rhs == 0)
                return "Infinite solutions";
            else
                return "No solution";
        } else
            return "x=" + rhs / lhs;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. Generating coefficients and finding $lhs$ and $rhs$ will take $O(n)$.

* Space complexity : $O(n)$. ArrayList $res$ size can grow upto $n$.

# Submissions
---
**Solution 1: (Using regex for spliting)**
```
Runtime: 12 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def solveEquation(self, equation: str) -> str:
        def coeff(x):
            if len(x) > 1 and x[len(x) - 2] >= '0' and x[len(x) - 2] <= '9':
                return x.replace('x', '')
            return x.replace('x', '1')

        lr = equation.split('=')
        lhs = 0
        rhs = 0
        for x in re.split(r"(?=\+)|(?=-)", lr[0]):
            if x.find('x') >= 0:
                lhs += int(coeff(x))
            else:
                rhs -= int(x) if x != '' else 0
        for x in re.split(r"(?=\+)|(?=-)", lr[1]):
            if x.find('x') >= 0:
                lhs -= int(coeff(x))
            else:
                rhs += int(x) if x != '' else 0
        if (lhs == 0):
            if (rhs == 0):
                return "Infinite solutions";
            else:
                return "No solution";
        else:
            return 'x={}'.format(rhs // lhs)
```

**Solution 2: (String)**
```
Runtime: 3 ms
Memory Usage: 6.2 MB
```
```c++
class Solution {
public:
    string solveEquation(string equation) {
        stringstream ss(equation);
        string s;
        int var_x_left=0;
        int constant_left=0;
        int var_x_right=0;
        int constant_right=0;
        getline(ss,s,'=');
        calculate(s,var_x_left,constant_left);
        getline(ss,s,'=');
        calculate(s,var_x_right,constant_right);
        if(var_x_left==var_x_right && (constant_left!=0 || constant_right!=0) && constant_left!=constant_right)
            return "No solution";
        if(var_x_left==var_x_right) 
            return "Infinite solutions";
        var_x_left-=var_x_right;
        constant_right-=constant_left;
        int val=constant_right/var_x_left;
        return "x="+to_string(val);
    }
    
    void calculate(string s,int &x,int &y){
        string word;
        int i=0;
        bool flag=true;
        if(s[0]=='-'){
            flag=false;
            i++;
        }

        while(i<s.length()){
            word="";
            while(i<s.length() && s[i]!='-' && s[i]!='+' && s[i]!='x' )
                word+=s[i++];


            if(i==s.length() || s[i]=='-' || s[i]=='+'){
                if(flag){

                    y+=stoi(word);
                }
                else
                y-=stoi(word);
            }
           else if(s[i]=='x'){
                if(flag){
                    if(word!="")
                    x+=stoi(word);
                    else
                        x+=1;
                }
                else{
                    if(word!="")
                    x-=stoi(word);
                    else 
                        x-=1;
                }
            }

            if(i!=s.length()){
                if(s[i]=='x' && i+1!=s.length()){
                    if(s[i+1]=='-')
                        flag=false;
                    else
                        flag=true;
                    i+=2;
                }
                 else if(s[i]=='-')
                {
                    flag=false;
                    i++;
                }
                else 
                {
                    flag=true;
                    i++;
                }
            } 
        }
    }
};
```
