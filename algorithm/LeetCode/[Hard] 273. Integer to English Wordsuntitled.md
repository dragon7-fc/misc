273. Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

**Example 1:**
```
Input: 123
Output: "One Hundred Twenty Three"
```

**Example 2:**
```
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
```

**Example 3:**
```
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

**Example 4:**
```
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
```

# Submissions
---
**Solution 1: (Math, DFS)**
```
Runtime: 32 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"

        ones = {
                0: "",
                1: "One ",
                2: "Two ",
                3: "Three ",
                4: "Four ",
                5: "Five ",
                6: "Six ",
                7: "Seven ",
                8: "Eight ",
                9: "Nine "
                }
        tens = {
                10: "Ten ",
                11: "Eleven ",
                12: "Twelve ",
                13: "Thirteen ",
                14: "Fourteen ",
                15: "Fifteen ",
                16: "Sixteen ",
                17: "Seventeen ",
                18: "Eighteen ",
                19: "Nineteen ",
                0:  "",
                2:  "Twenty ",
                3:  "Thirty ",
                4:  "Forty ",
                5:  "Fifty ",
                6:  "Sixty ",
                7:  "Seventy ",
                8:  "Eighty ",
                9:  "Ninety " 
                }
        powers_of_ten = {
                3:  "Hundred ",
                4:  "Thousand ",
                5:  "Thousand ",
                6:  "Thousand ",
                7:  "Million ",
                8:  "Million ",
                9:  "Million ",
                10: "Billion "
                }
        
        def buildTens(s, num):
            if num[0] == "0":
                return s, num[1:]
            if int(num[:2]) in tens:
                s += tens[int(num[:2])] + powers_of_ten[len(num)]
            else:
                s += tens[int(num[0])]
                s += ones[int(num[1])]  + powers_of_ten[len(num)] 
            return s, num[2:]
        
        def buildHundreds(s, num):
            s += ones[int(num[0])] + powers_of_ten[3]
            return s
        
        def buildString(s, num):
            if len(num) == 1:
                s += ones[int(num)]
                return s
            
            if len(num) == 10 or len(num) == 7 or len(num) == 4:
                if s and num[0] == "0" \
                and (s[-8:] == "Million " \
                  or s[-8:] == "Billion "):
                    return buildString(s, num[1:])
                s += ones[int(num[0])] + powers_of_ten[len(num)]
                return buildString(s, num[1:])
            
            if num[0] == "0":
                return buildString(s, num[1:])
            
            if len(num) == 9 or len(num) == 6:
                s, num = buildTens(buildHundreds(s, num), num[1:])
                return buildString(s, num)
                
            if len(num) == 8 or len(num) == 5:
                s, num = buildTens(s, num)
                return buildString(s, num)
            
            if len(num) == 3:
                return buildString(buildHundreds(s, num), num[1:])
            
            if len(num) == 2:
                if int(num) in tens:
                    s += tens[int(num)]
                    return s
                else:
                    s += tens[int(num[0])]
                    return buildString(s, num[1:])

        return buildString("", str(num))[:-1]
```

**Solution 2: (Math)**
```
Runtime: 4 ms
Memory Usage: 6.4 MB
```
```c++
class Solution {
public:
    string numberToWords(int num) {
        if (num == 0) return "Zero";
        string res;
        for (int divisor = 1e9; divisor > 0; divisor /= 1e3){
            const int quotient = num / divisor;
            if (quotient == 0) continue;
            res += processHundreds(quotient);
            res += largeNums.at(divisor);
            num %= divisor;
        }
        return res.substr(1, res.size());
    }
    
    string processHundreds(int num){
        string res = "";
        if (num >= 100){
            res += " " + digits.at(num/100) + " Hundred";
            num %= 100;
        }
        if (num >= 20){
            res += " " + tens.at(num/10 * 10);
            num %= 10;
        }
        if (num >= 10){
            res += " " + tenToNighteen.at(num);
            num = 0;
        }
        if (num > 0){
            res += " " + digits.at(num);
        }
        return res;
    }
    static const unordered_map<int, string> digits;
    static const unordered_map<int, string> tenToNighteen;
    static const unordered_map<int, string> tens;
    static const unordered_map<int, string> largeNums;
};
const unordered_map<int, string> Solution::digits = {{1,"One"}, {2,"Two"}, {3,"Three"}, {4,"Four"}, {5,"Five"}, {6,"Six"}, 
                                                   {7,"Seven"}, {8,"Eight"}, {9,"Nine"}};

const unordered_map<int, string> Solution::tenToNighteen = {{10,"Ten"}, {11,"Eleven"}, {12,"Twelve"}, {13,"Thirteen"}, 
                                                            {14,"Fourteen"}, {15,"Fifteen"}, {16,"Sixteen"}, {17,"Seventeen"}, 
                                                            {18,"Eighteen"}, {19,"Nineteen"}};
const unordered_map<int, string> Solution::tens = {{20,"Twenty"}, {30,"Thirty"}, {40,"Forty"}, {50,"Fifty"}, {60,"Sixty"},
                                                    {70,"Seventy"}, {80,"Eighty"}, {90,"Ninety"}};
const unordered_map<int, string> Solution::largeNums{{1, ""}, {1e3," Thousand"}, {1e6," Million"}, {1e9," Billion"}};
```