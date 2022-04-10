2232. Minimize Result by Adding Parentheses to Expression

You are given a **0-indexed** string `expression` of the form `"<num1>+<num2>"` where `<num1>` and `<num2>` represent positive integers.

Add a pair of parentheses to `expression` such that after the addition of parentheses, `expression` is a **valid** mathematical expression and evaluates to the **smallest** possible value. The left parenthesis must be added to the left of `'+'` and the right parenthesis must be added to the right of `'+'`.

Return `expression` after adding a pair of parentheses such that `expression` evaluates to the **smallest** possible value. If there are multiple answers that yield the same result, return any of them.

The input has been generated such that the original value of `expression`, and the value of `expression` after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

 

**Example 1:**
```
Input: expression = "247+38"
Output: "2(47+38)"
Explanation: The expression evaluates to 2 * (47 + 38) = 2 * 85 = 170.
Note that "2(4)7+38" is invalid because the right parenthesis must be to the right of the '+'.
It can be shown that 170 is the smallest possible value.
```

**Example 2:**
```
Input: expression = "12+34"
Output: "1(2+3)4"
Explanation: The expression evaluates to 1 * (2 + 3) * 4 = 1 * 5 * 4 = 20.
```

**Example 3:**
```
Input: expression = "999+999"
Output: "(999+999)"
Explanation: The expression evaluates to 999 + 999 = 1998.
```

**Constraints:**

* `3 <= expression.length <= 10`
* `expression` consists of digits from `'1'` to `'9'` and `'+'`.
* `expression` starts and ends with digits.
* `expression` contains exactly one `'+'`.
* The original value of `expression`, and the value of `expression` after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

# Submissions
---
**Solution 1: (String, Brute Force)**
```
Runtime: 62 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_index, n, ans = expression.find('+'), len(expression), [float(inf),expression] 
        def evaluate(exps: str):
            return eval(exps.replace('(','*(').replace(')', ')*').lstrip('*').rstrip('*'))
        for l in range(plus_index):
            for r in range(plus_index+1, n):
                exps = f'{expression[:l]}({expression[l:plus_index]}+{expression[plus_index+1:r+1]}){expression[r+1:n]}'
                res = evaluate(exps)
                if ans[0] > res:
                    ans[0], ans[1] = res, exps
        return ans[1]
```

**Solution 2: (String, Brute Force)**
```
Runtime: 0 ms
Memory Usage: 6 MB
```
```c++
class Solution {
public:
    string minimizeResult(string expression) {
        //First find the index of '+ in expresseion. let it be idx.
		int idx;
        int n=expression.size();
        for(int i=0;i<n;i++)
            if(expression[i]=='+')
            {
                idx=i;
                break;
            }
			
		//Now find two numbers which are on left and right side of '+' sign in expression	
        string num1 = expression.substr(0,idx);
        string num2 = expression.substr(idx+1,n-idx-1);
		
		//b1 and b2 are for brackets . b1=left bracket, b2=right bracket
        int b1=0,b2=0;
        int min =INT_MAX;
        string ans;
		
		//p1 and p2 are product number outside the brackets i.e our expresion is p1(sum)p2
        int p1,p2;
		
		//Find all possible conditions, iterate left bracket over num1 and right bracket over num2
        for(int b1=0;b1<num1.size();b1++)
        {
            for(int b2=0;b2<num2.size();b2++)
            {
                // s1 and s2 are strings which are outside the left parenthesis and right parenthesis respectively 
                string s1=num1.substr(0,b1);
                string s2=num2.substr(b2+1,b2-num2.size()-1);
               
               //if any of the string is empty then its int value should be 1 else its same as string.
			   if(s1.empty())
                    p1=1;
                else
                    p1=stoi(num1.substr(0,b1));
                if(s2.empty())
                    p2=1;
                else
                    p2=stoi(num2.substr(b2+1,b2-num2.size()-1));
					
				//sum stores the numerical value of the sum between the parenthesis	
                int sum=stoi(num1.substr(b1,num1.size())) + stoi(num2.substr(0,b2+1));
               //eval stores the numerical value of whole expression
			   int eval=p1*sum*p2;
			   
			   //if velue of expression is less then minimum, then make ans string = s1(sum) s1
                if(eval<min){
                    
                    min=eval;
                    ans=s1+"("+num1.substr(b1,num1.size())+"+"+num2.substr(0,b2+1)+")"+s2;
                
                }
                
            }
        }
        return ans;
    }
};
```
