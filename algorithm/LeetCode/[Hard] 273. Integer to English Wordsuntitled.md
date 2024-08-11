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
**Solution 1: (Math, Hash Table)**
```
Runtime: 36 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def numberToWords(self, num: int) -> str:
        digits = {1: "One",
                  2: "Two",
                  3: "Three",
                  4: "Four",
                  5: "Five",
                  6: "Six", 
                  7: "Seven",
                  8: "Eight",
                  9: "Nine"}
        tenToNighteen = {10: "Ten",
                         11: "Eleven",
                         12: "Twelve",
                         13: "Thirteen",
                         14: "Fourteen",
                         15: "Fifteen",
                         16: "Sixteen",
                         17: "Seventeen",
                         18: "Eighteen",
                         19: "Nineteen"}
        tens = {20: "Twenty",
                30: "Thirty",
                40: "Forty",
                50: "Fifty",
                60: "Sixty",
                70: "Seventy",
                80: "Eighty",
                90: "Ninety"}
        largeNums = {1: "",
                     1e3: " Thousand",
                     1e6: " Million",
                     1e9: " Billion"}
        
        def processHundreds(num):
            res = ""
            if num >= 100:
                res += " " + digits[num//100] + " Hundred"
                num %= 100
            if num >= 20:
                res += " " + tens[num//10 * 10]
                num %= 10
            if num >= 10:
                res += " " + tenToNighteen[num]
                num = 0
            if num > 0:
                res += " " + digits[num]
            return res
        
        if num == 0: return "Zero"
        res = ""
        divisor = 10**9
        while divisor > 0:
            quotient = num // divisor
            if quotient == 0:
                divisor = divisor // 10**3
                continue
            res += processHundreds(quotient)
            res += largeNums[divisor]
            num %= divisor
            divisor = divisor // 10**3
        return res[1:]
```

**Solution 2: (Math, DFS)**
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

**Solution 3: (Recursive Approach)**
```
Runtime: 3 ms
Memory: 11.32 MB
```
```c++
class Solution {
    // Recursive function to convert numbers to words
    // Handles numbers based on their ranges: <10, <20, <100, <1000, <1000000, <1000000000, and >=1000000000
    string convertToWords(int num) {
        if (num < 10) {
            return belowTen[num];
        }
        if (num < 20) {
            return belowTwenty[num - 10];
        }
        if (num < 100) {
            return belowHundred[num / 10] + (num % 10 ? " " + convertToWords(num % 10) : "");
        }
        if (num < 1000) {
            return convertToWords(num / 100) + " Hundred" + (num % 100 ? " " + convertToWords(num % 100) : "");
        }
        if (num < 1000000) {
            return convertToWords(num / 1000) + " Thousand" + (num % 1000 ? " " + convertToWords(num % 1000) : "");
        }
        if (num < 1000000000) {
            return convertToWords(num / 1000000) + " Million" + (num % 1000000 ? " " + convertToWords(num % 1000000) : "");
        }
        return convertToWords(num / 1000000000) + " Billion" + (num % 1000000000 ? " " + convertToWords(num % 1000000000) : "");
    }
    // Arrays to store words for numbers less than 10, 20, and 100
    const vector<string> belowTen = { "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine" };
    const vector<string> belowTwenty = { "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen" };
    const vector<string> belowHundred = { "", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety" };
public:
    string numberToWords(int num) {
        // Handle the special case where the number is zero
        if (num == 0) {
            return "Zero";
        }
        // Call the helper function to start the conversion
        return convertToWords(num);
    }
};
```

**Solution 4: (Iterative Approach)**
```
Runtime: 7 ms
Memory: 10.88 MB
```
```c++
class Solution {
public:
    string numberToWords(int num) {
        // Handle the special case where the number is zero
        if (num == 0) return "Zero";

        // Arrays to store words for single digits, tens, and thousands
        const vector<string> ones = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        const vector<string> tens = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
        const vector<string> thousands = {"", "Thousand", "Million", "Billion"};

        // StringBuilder to accumulate the result
        string result = "";
        int groupIndex = 0;

        // Process the number in chunks of 1000
        while (num > 0) {
            // Process the last three digits
            if (num % 1000 != 0) {
                string groupResult = "";
                int part = num % 1000;

                // Handle hundreds
                if (part >= 100) {
                    groupResult = ones[part / 100] + " Hundred ";
                    part %= 100;
                }

                // Handle tens and units
                if (part >= 20) {
                    groupResult += tens[part / 10] + " ";
                    part %= 10;
                }

                // Handle units
                if (part > 0) {
                    groupResult += ones[part] + " ";
                }

                // Append the scale (thousand, million, billion) for the current group
                groupResult += thousands[groupIndex] + " ";
                // Insert the group result at the beginning of the final result
                result = groupResult + result;
            }
            // Move to the next chunk of 1000
            num /= 1000;
            groupIndex++;
        }

        return result.substr(0, result.find_last_not_of(" ") + 1); // Remove trailing spaces
    }
};
```

**Solution 5: (Pair-Based Approach)**
```
Runtime: 8 ms
Memory: 12.34 MB
```
```c++
class Solution {
    // Mapping of numeric values to their corresponding English words
    vector<pair<int, string>> numberToWordsMap = {
        {1000000000, "Billion"}, {1000000, "Million"}, {1000, "Thousand"},
        {100, "Hundred"}, {90, "Ninety"}, {80, "Eighty"}, {70, "Seventy"},
        {60, "Sixty"}, {50, "Fifty"}, {40, "Forty"}, {30, "Thirty"},
        {20, "Twenty"}, {19, "Nineteen"}, {18, "Eighteen"}, {17, "Seventeen"},
        {16, "Sixteen"}, {15, "Fifteen"}, {14, "Fourteen"}, {13, "Thirteen"},
        {12, "Twelve"}, {11, "Eleven"}, {10, "Ten"}, {9, "Nine"}, {8, "Eight"},
        {7, "Seven"}, {6, "Six"}, {5, "Five"}, {4, "Four"}, {3, "Three"},
        {2, "Two"}, {1, "One"}
    };
public:
    string numberToWords(int num) {
        if (num == 0) {
            return "Zero";
        }

        for (auto& [value, word] : numberToWordsMap) {
            // Check if the number is greater than or equal to the current unit
            if (num >= value) {
                // Convert the quotient to words if the current unit is 100 or greater
                string prefix = (num >= 100) ? numberToWords(num / value) + " " : "";

                // Get the word for the current unit
                string unit = word;

                // Convert the remainder to words if it's not zero
                string suffix = (num % value == 0) ? "" : " " + numberToWords(num % value);

                return prefix + unit + suffix;
            }
        }

        return "";
    }
};
```
