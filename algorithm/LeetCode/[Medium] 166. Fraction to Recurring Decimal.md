166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

**Example 1:**
```
Input: numerator = 1, denominator = 2
Output: "0.5"
```

**Example 2:**
```
Input: numerator = 2, denominator = 1
Output: "2"
```

**Example 3:**
```
Input: numerator = 2, denominator = 3
Output: "0.(6)"
```

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ''
        
        # sign
        if numerator * denominator < 0:
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # before point
        res += str(numerator // denominator)
        carrier = numerator % denominator
        
        # after point
        if carrier > 0:
            res+='.'
        memo = {}
        while carrier > 0:
            if carrier in memo:
                index = memo[carrier]
                res = res[:index] + '(' + res[index:] +')'
                return res
            else:
                memo[carrier] = len(res)
                res += str((carrier * 10) // denominator)
                carrier = ((carrier * 10) % denominator)
                
        return res
```

**Solution 2: (Math)**
```
Runtime: 0 ms
Memory Usage: 6.2 MB
```
```c


char * fractionToDecimal(int numerator, int denominator){
    int index = -1, index1 = 0, pointindex, flag = 0, sign = 0, cnt = 0;
	if ((numerator < 0 && denominator >0) || (numerator > 0 && denominator < 0) ){sign = 1;}
	long long int numerator1 = numerator; 
	long long int denominator1 = denominator; 
	numerator1 = llabs(numerator);
	denominator1 = llabs(denominator);   
	char* ans = malloc(1024*sizeof(char));
	char* temp = calloc(1000,sizeof(char));
	long long int *hash = malloc(sizeof(long long int)*1000);
	if (sign == 1){cnt += sprintf(ans + cnt, "%c", '-');}
	cnt += sprintf(ans + cnt, "%lld", numerator1/denominator1);
	long long int remainder = numerator1 % denominator1;
	if (remainder){
		cnt += sprintf(ans + cnt, "%c", '.');
		pointindex = cnt;
	}

	while(remainder){
		remainder *= 10;
		int d =  remainder / denominator1;

		for (int i = 0; i < index1; i++){
			if (hash[i] == remainder ){                
				index = i;
				break;
			}           
		}       

		if (index>=0){            
			strcat(temp,ans+index+pointindex);            
			ans[pointindex+index] = '(';      
			ans[pointindex+index+1] = '\0';
			strcat(ans,temp);
			strcat(ans,")");
			break;
		}

		hash[index1++] = remainder;
		cnt += sprintf(ans + cnt, "%lld", d);
		remainder %= denominator1;

	}
	return ans;
}
```

**Solution 3: (uthash)**
```
Runtime: 4 ms
Memory Usage: 7.4 MB
```
```c
#define MAX_STR 10000

/* uthash wrappers START */
struct inthash{
   long long val;
   long long q;   
   int idx;
   UT_hash_handle hh;
};

void hash_add(struct inthash **ihash, int num, int q, int idx){
   struct inthash *el = malloc(sizeof(struct inthash));
   el->val = num;
   el->idx = idx;
   el->q = q;
   HASH_ADD_INT(*ihash, val, el);
}
bool hash_find(struct inthash **ihash, int num, int *rec_idx){
    struct inthash *el = NULL;
    HASH_FIND_INT(*ihash, &num, el);
    if(el != NULL)
       *rec_idx = el->idx;
    return el != NULL;
}
int sort_idx(struct inthash *a, struct inthash *b) {
    return (a->idx - b->idx);
}
/* uthash wrappers END*/
#define ABS(num) ((num) < 0 ? (-((long long)num)) : (num))

char * fractionToDecimal(int numerator, int denominator){
    char *res = calloc(sizeof(char), MAX_STR);
   int res_idx = 0;
   
   /* Result sign */
   bool is_neg = (numerator < 0) ^ (denominator < 0);
   if(is_neg)
      res_idx += snprintf(res, MAX_STR, "-");

   /* Remove the sign from numerator and denominator */
   long long nume = ABS(numerator);
   long long deno = ABS(denominator);

   /* resultant full non-fractional number */
   long long res_num = nume / deno;
   res_idx += snprintf(res + res_idx, MAX_STR, "%lld", res_num);
   
   /* No remainder left, completely divides no decimal point */
   if((nume % deno) == 0) {
      if(res_num == 0) {
         memset(res, 0, MAX_STR);
         res[0] = '0';
      }
      return res;
   }
   /* Find the fractional part here */
   struct inthash *ihash = NULL; /* to find recurrance pattern */
   long long remainder = nume % deno;
   long long quos = (remainder * 10) / deno;
   bool is_recurring = false;
   int res_fract_idx = 0;
   int rec_idx = 0;
   
   while(remainder != 0 && !is_recurring) {
      if(hash_find(&ihash, remainder, &rec_idx) == false) {
         hash_add(&ihash, remainder, quos, res_fract_idx);
      }else {
         is_recurring = true;
         break;
      }
      remainder = (remainder * 10) % deno;
      quos = (remainder * 10) / deno;
      res_fract_idx++;
   }
   HASH_SORT(ihash, sort_idx);

   char *res_fract = calloc(sizeof(char), MAX_STR);
   char *res_recurring = calloc(sizeof(char), MAX_STR);
   int rf_idx = 0;
   int rr_idx = 0;

   struct inthash *el, *tmp;
   HASH_ITER(hh, ihash, el, tmp) {
      if(is_recurring && el->idx >= rec_idx)
         res_recurring[rr_idx++] = el->q + '0';
      else
         res_fract[rf_idx++] = el->q + '0';

      HASH_DEL(ihash, el);
      free(el);
   }

   res_idx += snprintf(res + res_idx, MAX_STR, ".%s", res_fract);
   
   if(is_recurring == true) 
      res_idx += snprintf(res + res_idx, MAX_STR, "(%s)", res_recurring);
   
   free(res_fract);
   free(res_recurring);
   return res;
}
```

**Solution 4: (Hash Table)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 9.52 MB, Beats 13.86%
```
```c++
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) {
            return "0";
        } 
        unordered_map<long long,int> m;
        string ans = (numerator >= 0) ^ (denominator >= 0) ? "-":"";
        long long r = abs((long long)numerator), d = abs((long long)denominator);
        ans += to_string(r/d);
        r %= d;
        if (r) {
            ans += ".";
            while (r) {
                r *= 10;
                if (m.count(r)) {
                    ans.insert(ans.begin() + m[r], "(");
                    ans += ")";
                    break;
                } else {
                    ans += to_string(r/d);
                    m[r] = ans.length() - 1;
                    r %= d;
                }
            }
        }
        return ans;
    }
};
```
