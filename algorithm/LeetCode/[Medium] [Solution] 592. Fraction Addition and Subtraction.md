592. Fraction Addition and Subtraction

Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say `2`, you need to change it to the format of fraction that has denominator `1`. So in this case, 2 should be converted to `2/1`.

**Example 1:**
```
Input:"-1/2+1/2"
Output: "0/1"
```

**Example 2:**
```
Input:"-1/2+1/2+1/3"
Output: "1/3"
```

**Example 3:**
```
Input:"1/3-1/2"
Output: "-1/6"
```

**Example 4:**
```
Input:"5/3+1/3"
Output: "2/1"
```

**Note:**

* The input string only contains `'0'` to `'9'`, `'/'`, `'+'` and `'-'`. So does the output.
* Each fraction (input and output) has format `±numerator/denominator`. If the first input fraction or the output is positive, then `'+'` will be omitted.
* The input only contains valid **irreducible fractions**, where the **numerator** and **denominator** of each fraction will always be in the range `[1,10]`. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
* The number of given fractions will be in the range [1,10].
* The numerator and denominator of the **final result** are guaranteed to be valid and in the range of 32-bit int.

# Solution
---
## Approach #1 Using LCM[Accepted]
The first obvious step to be undertaken is to split the given string into individual fractions. We split the string based on `+` and `-` sign. We store the signs in the order in which they appear in the string in $sign$ array. Further, after getting the individual fractions, we further split the fractions based on `/` sign. Thus, we obtain the individual numerator and denominator parts. We store the same in $num$ and $den$ arrays respectively.

Now, we've got the data ready to be worked upon. In order to see the method we've used in this implementation, we'll take an example and understand the way we work on it.

Let's say, the given fraction is:

$\frac{3}{2} + \frac{5}{3} -\frac{7}{6}$

We need to equalize all the denominators so as to be able to add and subtract the numerators easily. The nearest value the denominators can be scaled upto is the LCM of all the denominators. Thus, we need to find the LCM of all the denominators and then multiply all the denominators with appropriate integer factors to make them equal to the LCM. But, in order to keep the individual fraction values unchanged, we need to multiply the individual numerators also with the same factors.

In order to find the LCM, we can go as follows. We use the method $lcm(a,b,c) = lcm( lcm(a,b), c)$. Thus, if we can compute the lcm of two denominators, we can keep on repeating the process iteratively over the denominators to get the overall lcm. To find the lcm of two numbers $a$ and bb, we use $lcm(a,b) = (a*b)/gcd(a,b)$. For the above example, the $lcm$ turns out to be `6`.

Thus, we scale up the denominators to `6` as follows:

$\frac{3*3}{2*3} + \frac{5*2}{3*2} -\frac{7}{6}$

Thus, we can observe that, the scaling factor for a fraction $\frac{num}{den}$ is given by: ${num*x}/{den*x}$, where $x$ is the corresponding scaling factor. Note that, $den*x=lcm$. Thus, $x=lcm/den$. Thus, we find out the corresponding scaling factor $x_i$ for each fraction.

After this, we can directly add or subtract the new scaled numerators.

In the current example, we obtain $\frac{12}{6}$ as the result. Now, we need to convert this into an irreducible fraction. Thus, if we obtain $\frac{num_i}{den_i}$ as the final result, we need to find a largest factor $y$, which divides both $num_i$ and $den_i$. Such a number, as we know, is the gcd of $num_i$ and $den_i$.

Thus, to convert the result $\frac{num_i}{den_i}$, we divide both the numerator and denominator by the gcd of the two numbers $y$ to obtain the final irreducible $\frac{num_i/y}{den_i/y}$.

Note: A problem with this approach is that we find the lcm of all the denominators in a single go and then reduce the overall fraction at the end. Thus, the lcm value could become very large and could lead to an overflow. But, this solution suffices for the current range of numbers.

```java

public class Solution {
    public String fractionAddition(String expression) {
        List < Character > sign = new ArrayList < > ();
        for (int i = 1; i < expression.length(); i++) {
            if (expression.charAt(i) == '+' || expression.charAt(i) == '-')
                sign.add(expression.charAt(i));
        }
        List < Integer > num = new ArrayList < > ();
        List < Integer > den = new ArrayList < > ();
        for (String sub: expression.split("\\+")) {
            for (String subsub: sub.split("-")) {
                if (subsub.length() > 0) {
                    String[] fraction = subsub.split("/");
                    num.add(Integer.parseInt(fraction[0]));
                    den.add(Integer.parseInt(fraction[1]));
                }
            }
        }
        if (expression.charAt(0) == '-')
            num.set(0, -num.get(0));
        int lcm = 1;
        for (int x: den) {
            lcm = lcm_(lcm, x);
        }

        int res = lcm / den.get(0) * num.get(0);
        for (int i = 1; i < num.size(); i++) {
            if (sign.get(i - 1) == '+')
                res += lcm / den.get(i) * num.get(i);
            else
                res -= lcm / den.get(i) * num.get(i);
        }
        int g = gcd(Math.abs(res), Math.abs(lcm));
        return (res / g) + "/" + (lcm / g);
    }
    public int lcm_(int a, int b) {
        return a * b / gcd(a, b);
    }
    public int gcd(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(nlogx)$. Euclidean GCD algorithm takes $O(log(a.b))$ time for finding gcd of two numbers $a$ and $b$. Here $n$ refers to the number of fractions in the input string and $x$ is the maximum possible value of denominator.

* Space complexity : $O(n)$. Size of $num$, $en$ and $sign$ list grows upto $n$.

## Approach #2 Using GCD[Accepted]
**Algorithm**

We know that we can continue the process of evaluating the given fractions by considering pairs of fractions at a time and continue the process considering the result obtained and the new fraction to be evaluated this time. We make use of this observation, and thus, instead of segregating the signs, numerators and denominators first, we directly start scanning the given strings and operate on the fractions obtained till now whenever a new sign is encountered.

We operate on the pairs of fractions, and keep on reducing the result obtained to irreducible fractions on the way. By doing this, we can reduce the chances of the problem of potential overflow possible in case the denominators lead to a large value of lcm.

We also observed from the last approach, that we need to equalize the denominators of a pair of fractions say:

$\frac{a}{b} + \frac{c}{d}$

We used a scaling factor of $x$ for the first fraction(both numerator and denominator). Here, $x=lcm(b,d)/b$. For the second fraction, the scaling factor $y$ is given by $y=lcm(b,d)/d$. Here, $lcm(b,d)=b*d/gcd(b,d)$. Thus, instead of finding the lcm and then again determining the scaling factor, we can directly use: $x=(b*d)/(gcd(b,d)*b) = d/gcd(b,d)$, and $y=(b*d)/(gcd(b,d)*d)$. Thus, we need to scale the numerators appropriately and add/subtract them in terms of pairs. The denominators are scaled in the same manner to the lcm of the two denominators involved.

After evaluting every pair of fractions, we again reduce them to irreducible fractions by diving both the numerator and denominator of the resultant fraction by the gcd of the two.

```java
public class Solution {
    public String fractionAddition(String expression) {
        List < Character > sign = new ArrayList < > ();
        if (expression.charAt(0) != '-')
            sign.add('+');
        for (int i = 0; i < expression.length(); i++) {
            if (expression.charAt(i) == '+' || expression.charAt(i) == '-')
                sign.add(expression.charAt(i));
        }
        int prev_num = 0, prev_den = 1, i = 0;
        for (String sub: expression.split("(\\+)|(-)")) {
            if (sub.length() > 0) {
                String[] fraction = sub.split("/");
                int num = (Integer.parseInt(fraction[0]));
                int den = (Integer.parseInt(fraction[1]));
                int g = Math.abs(gcd(den, prev_den));
                if (sign.get(i++) == '+')
                    prev_num = prev_num * den / g + num * prev_den / g;
                else
                    prev_num = prev_num * den / g - num * prev_den / g;
                prev_den = den * prev_den / g;
                g = Math.abs(gcd(prev_den, prev_num));
                prev_num /= g;
                prev_den /= g;
            }
        }
        return prev_num + "/" + prev_den;
    }
    public int gcd(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(nlogx)$. Euclidean GCD algorithm takes $O(log(a.b))$ time for finding gcd of two numbers $a$ and $b$. Here $n$ refers to the number of fractions in the input string and $x$ is the maximum possible value of denominator.

* Space complexity : $O(n)$. Size of $sign$ list grows upto $n$.

# Submisssions
---
**Solution 1: (Using GCD)**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
import re
class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a

        sign = []
        if expression[0] != '-':
            sign.append('+')
        for i in range(len(expression)):
            if expression[i] == '+' or expression[i] == '-':
                sign.append(expression[i])
                
        prev_num = 0
        prev_den = 1
        i = 0
        for sub in re.split('\+|\-', expression):
            if len(sub) > 0:
                fraction = sub.split('/')
                num = int(fraction[0])
                den = int(fraction[1])
                g = abs(gcd(den, prev_den))
                if sign[i] == '+':
                    prev_num = prev_num * den // g + num * prev_den // g
                else:
                    prev_num = prev_num * den // g - num * prev_den // g
                i += 1
                prev_den = den * prev_den // g;
                g = abs(gcd(prev_den, prev_num))
                prev_num //= g
                prev_den //= g
        return '{}/{}'.format(prev_num, prev_den)
```

**Solution 2: (String)**
```
Runtime: 0 ms
Memory Usage: 6.1 MB
```
```c++
class Solution {
public:
    string fractionAddition(string expression) {
        int numerator = 0;
        int denominator = 1;
        int numeratorNew, denominatorNew;
        int tempNumerator, tempDenominator;
        
        int i=0;
        bool isAddition = true;
        
        while(i < expression.size()){
            if(expression[i] == '-'){
                isAddition = false;
                i++;
            }
            else if(expression[i] == '+'){
                isAddition = true;
                i++;
            }
            
            numeratorNew = 0;
            while(i<expression.size() && expression[i] != '/'){
                numeratorNew = numeratorNew * 10 + expression[i] - '0';
                i++;
            }
            i++;
            denominatorNew = 0;
            while(i<expression.size() && (expression[i] >= '0' && expression[i] <= '9')){
                denominatorNew = denominatorNew * 10 + expression[i] - '0';
                i++;
            }
            
            if(!isAddition)
                tempNumerator = numerator*denominatorNew - denominator*numeratorNew;
            else
                tempNumerator = numerator*denominatorNew + denominator*numeratorNew;
            
            tempDenominator = denominator*denominatorNew;
            
            numerator = tempNumerator;
            denominator = tempDenominator;        
        }
        
        if(numerator == 0)
            return "0/1";
        
        
        bool isNegative;
        int numeratorAbs;
        bool flag;
        
        if(numerator < 0){
            isNegative = true;
            numeratorAbs = -1 * numerator;
        }
        else{
            isNegative = false;
            numeratorAbs = numerator;
        }
        
        if(numeratorAbs == denominator){
            if(isNegative)
                return "-1/1";
            else
                return "1/1";
        } 
        
        while(1){
            flag = false;
            for(int i=2; i<=min(numeratorAbs, denominator); i++){
                if(numeratorAbs % i == 0 && denominator % i == 0){
                    flag = true;
                    numeratorAbs = numeratorAbs / i;
                    denominator = denominator / i;
                    break;
                }
            }
            if(!flag)
                break;
        }
        if(isNegative)
            return "-" + to_string(numeratorAbs)+"/"+to_string(denominator);
        else
            return to_string(numeratorAbs)+"/"+to_string(denominator);  
    }
};
```

**Solution 3: (Manual Parsing + Common Denominator)**
```
Runtime: 0 ms
Memory: 7.49 MB
```
```c++
class Solution {
    int FindGCD(int a, int b) {
        if (a == 0) return b;
        return FindGCD(b % a, a);
    }
public:
    string fractionAddition(string expression) {
        int num = 0;
        int denom = 1;

        int i = 0;
        while (i < expression.size()) {
            int currNum = 0;
            int currDenom = 0;

            bool isNegative = false;

            // check for sign
            if (expression[i] == '-' || expression[i] == '+') {
                if (expression[i] == '-') {
                    isNegative = true;
                }
                // move to next character
                i++;
            }

            // build numerator
            while (isdigit(expression[i])) {
                int val = expression[i] - '0';
                currNum = currNum * 10 + val;
                i++;
            }

            if (isNegative) currNum *= -1;

            // skip divisor
            i++;

            // build denominator
            while (i < expression.size() && isdigit(expression[i])) {
                int val = expression[i] - '0';
                currDenom = currDenom * 10 + val;
                i++;
            }

            // add fractions together using common denominator
            num = num * currDenom + currNum * denom;
            denom = denom * currDenom;
        }

        int gcd = abs(FindGCD(num, denom));

        // reduce fractions
        num /= gcd;
        denom /= gcd;

        return to_string(num) + "/" + to_string(denom);
    }
};
```

**Solution 4: (Parsing with Regular Expressions)**
```
Runtime: 0 ms
Memory: 8.21 MB
```
```c++
class Solution {
    int FindGCD(int a, int b) {
        if (a == 0) return b;
        return FindGCD(b % a, a);
    }
public:
    string fractionAddition(string expression) {
        int num = 0;
        int denom = 1;

        // separate expression into signed numbers
        vector<string> nums;
        int i = 0;
        if (expression[0] != '-') expression = '+' + expression;
        while (i < expression.size()) {
            int j = i + 1;
            while (j < expression.size() && expression[j] != '+' &&
                   expression[j] != '-') {
                j++;
            }
            nums.push_back(expression.substr(i, j - i));
            i = j;
        }

        for (int i = 0; i < nums.size(); ++i) {
            size_t pos = nums[i].find('/');
            int currNum = stoi(nums[i].substr(1, pos - 1));
            if (nums[i][0] == '-') currNum = -currNum;
            int currDenom = stoi(nums[i].substr(pos + 1));

            num = num * currDenom + currNum * denom;
            denom = denom * currDenom;

            int gcd = abs(FindGCD(num, denom));

            num /= gcd;
            denom /= gcd;
        }

        return to_string(num) + "/" + to_string(denom);
    }
};
```
