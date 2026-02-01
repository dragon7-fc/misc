465. Optimal Account Balancing

A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple `(x, y, z)` which means person `x` gave person `y` `$z`. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as `[[0, 1, 10], [2, 0, 5]]`.

Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

**Note:**

1. A transaction will be given as a tuple `(x, y, z)`. Note that `x ≠ y` and `z > 0`.
1. Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.

**Example 1:**
```
Input:
[[0,1,10], [2,0,5]]

Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
```

**Example 2:**
```
Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.
```

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 224 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        final_balances = defaultdict(int);
        debtors = [];
        creditors = [];
        
        ## get everyone's final balances, which might be positive or negative
        for i,j, trans in transactions:
            final_balances[i]-=trans;
            final_balances[j]+=trans;
        
        ## seperate into creditors and debtors
        for k,v in final_balances.items():
            if(v<0):
                debtors.append((v))
            elif(v>0):
                creditors.append((v))
        
        ## now the bactracking part
        self.ansr = float('Inf')
        def recurse(creditors, debtors, n = 0):
            nc = len(creditors);
            nd = len(debtors);
 
            if(nc == 0 or nd == 0):
                #print(creditors, debtors, n)
                if(nc == 0 and nd == 0):
                    self.ansr = min(self.ansr, n);
                return
            
            ## instead of iterating all debtors and creditors
            # remove the largest debt
            debt_val = min(debtors); #vd = debtors[0]
            idx = debtors.index(debt_val);
            for i in range(nc):
                credit = creditors[i]
                #print(vc, vd,vc+vd)
                if(credit+debt_val>0): ## debtor is satisfied, creditor has more money left
                    creditors[i] = (credit+debt_val);
                    recurse(creditors,debtors[0:idx]+debtors[idx+1:],n+1 )
                    creditors[i] = (credit)
                elif(credit + debt_val == 0):
                    recurse(creditors[0:i]+creditors[i+1:], debtors[0:idx]+debtors[idx+1:],n+1)
                else:
                    debtors[idx] = (credit+debt_val);
                    recurse(creditors[0:i]+creditors[i+1:], debtors,n+1)
                    debtors[idx] = (debt_val);
                        
        recurse(creditors, debtors)
        return self.ansr;    
```

**Solution 2: (Backtracking)**

    transactions = [[0,1,10],[2,0,5]]
bal
     0   1   2
   -10  10
     5      -5
    ----------
dp  -5  10  -5
     ^   ^
         ^   ^
         5   0
                ^
ans     +1  +1  0
     2

```
Runtime: 7 ms, Beats 59.64%
Memory: 9.22 MB, Beats 80.00%
```
```c++
class Solution {
    vector<long> dp; // all non-zero debts
    int bt(int i) { // min number of transactions to settle starting from debt[i] 
    	while (i < dp.size() && !dp[i]) { // get next non-zero debt
            i += 1;
        }
    	int rst = INT_MAX;
    	for (int j = i + 1; j < dp.size(); j ++) {
    	    if (dp[j] * dp[i] < 0) { // skip same sign debt
                dp[j] += dp[i]; 
		rst = min(rst, 1 + bt(i + 1)); 
		dp[j] -= dp[i];
	    }
        }
    	return rst < INT_MAX ? rst : 0;
    }
public:
    int minTransfers(vector<vector<int>>& transactions) {
        unordered_map<int, long> bal; // each person's overall balance
        for (auto &t: transactions) {
	    bal[t[0]] -= t[2];
	    bal[t[1]] += t[2];
	}
        for (auto &[_, b]: bal) {// only deal with non-zero debts
	    if (b) {
                dp.push_back(b);
            }
        }
        return bt(0);
    }
};
```
