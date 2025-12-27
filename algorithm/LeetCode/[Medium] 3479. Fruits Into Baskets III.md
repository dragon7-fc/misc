3479. Fruits Into Baskets III

You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where `fruits[i]` represents the quantity of the `i`th type of fruit, and `baskets[j]` represents the capacity of the `j`th basket.

From left to right, place the fruits according to these rules:

* Each fruit type must be placed in the **leftmost available** basket with a capacity greater than or equal to the quantity of that fruit type.
* Each basket can hold only one type of fruit.
* If a fruit type **cannot be placed** in any basket, it remains **unplaced**.

Return the number of fruit types that remain unplaced after all possible allocations are made.

 

**Example 1:**
```
Input: fruits = [4,2,5], baskets = [3,5,4]

Output: 1

Explanation:

fruits[0] = 4 is placed in baskets[1] = 5.
fruits[1] = 2 is placed in baskets[0] = 3.
fruits[2] = 5 cannot be placed in baskets[2] = 4.
Since one fruit type remains unplaced, we return 1.
```

**Example 2:**
```
Input: fruits = [3,6,1], baskets = [6,4,7]

Output: 0

Explanation:

fruits[0] = 3 is placed in baskets[0] = 6.
fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
fruits[2] = 1 is placed in baskets[1] = 4.
Since all fruits are successfully placed, we return 0.
```
 

**Constraints:**

* `n == fruits.length == baskets.length`
* `1 <= n <= 10^5`
* `1 <= fruits[i], baskets[i] <= 10^9`

# Submissions
---
**Solution 1: (Segment Tree, Binary Search)**
```
Runtime: 566 ms, Beats 68.18%
Memory: 196.42 MB, Beats 90.91%
```
```c++
#define ll long long

class SGT 
{
public:
    vector<ll> seg;

    SGT(ll n) 
    {
        seg.resize(4 * n + 1);
    }

    void build(ll ind, ll low, ll high, vector<ll> &arr) 
    {
        if (low == high) 
        {
            seg[ind] = arr[low];
            return;
        }

        ll mid = (low + high) / 2;

        build(2 * ind + 1, low, mid, arr);
        build(2 * ind + 2, mid + 1, high, arr);

        seg[ind] = max(seg[2 * ind + 1], seg[2 * ind + 2]);
    }

    ll query(ll ind, ll low, ll high, ll l, ll r) 
    {
        if (r < low || high < l) 
            return 0;

        if (low >= l && high <= r) 
            return seg[ind];

        ll mid = (low + high) >> 1;
        ll left = query(2 * ind + 1, low, mid, l, r);
        ll right = query(2 * ind + 2, mid + 1, high, l, r);

        return max(left, right);
    }

    void update(ll ind, ll low, ll high, ll i, ll val) 
    {
        if (low == high) 
        {
            seg[ind] = val;
            return;
        }

        ll mid = (low + high) >> 1;

        if (i <= mid) 
            update(2 * ind + 1, low, mid, i, val);
        else 
            update(2 * ind + 2, mid + 1, high, i, val);

        seg[ind] = max(seg[2 * ind + 1], seg[2 * ind + 2]);
    }

};





ll res;

void find(ll val, SGT &st, ll n)
{
    ll low = 0;
    ll high = n-1;

    ll ans = -1;
    
    while(low <= high)
    {
        ll mid = (low+high)/2;
        ll mx = st.query(0, 0, n-1, 0, mid); // finding max value in the range 0 to mid. 
            
        if(mx >= val)
        {
            ans = mid; 
            high = mid-1; // looking for index further left. 
        }
        
        else
            low = mid+1;
    }
    
    if(ans != -1)
        st.update(0, 0, n-1, ans, 0);
    
    else // if no suitable index is found increase the answer. 
        ++res;
    
    return;
}

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        res = 0; // global variable res initialised to zero;
        
        int n = fruits.size();
        vector<ll> tb(baskets.begin(), baskets.end());
        
        SGT st(n);
        st.build(0, 0, n-1, tb); // building the segment tree.
        
        for(int i=0; i<n; ++i)
            find(fruits[i], st, n); // checking answer for each fruit. 
        
        return res;
    }
};
```

**Solution 2: (Square Root Decomposition)**
```
Runtime: 409 ms, Beats 30.92%
Memory: 176.08 MB, Beats 98.89%
```
```c++
class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = fruits.size(), m = sqrt(n+1), i, j, k = (n + m - 1)/m, ck, ans = 0;
        bool flag;
        vector<int> dp(k);
        for (i = 0; i < n; i ++) {
            dp[i/m] = max(dp[i/m], baskets[i]);
        }
        for (i = 0; i < n; i ++) {
            flag = true;
            for (ck = 0; ck < k; ck ++) {
                if (fruits[i] <= dp[ck]) {
                    dp[ck] = 0;
                    for (j = ck*m; j < ck*m + m && j < n; j ++) {
                        if (fruits[i] <= baskets[j] && flag) {
                            baskets[j] = 0;
                            flag = false;
                        }
                        dp[ck] = max(dp[ck], baskets[j]);
                    }
                }
                if (!flag) {
                    break;
                }
            }
            if (flag) {
                ans += 1;
            }
        }
        return ans;
    }
};
```

**Solution 3: (Segment Tree, Binary Search, O(n logn logn))**

    fruits = [4,2,5], baskets = [3,5,4]

sgt
        
                   0 (5)
                 /    \
               1 (5)   2 (4)
            /    \
         3 (3)   4 (5)
buskets    3     5     4
          0  1  2  3  4
tree      5  5  4  3  5

find 4
query
          0  1  2  3  4
          ql qr
          p
          l     r
             p
          l  rx
    i        x
        ----------------
          qlr
          p
          l    r
             p
          l  r
                    p
          lrx
update
             vi
          0  1  2  3  4
          p
          l     r
             p
          l  r
                p
                lrx
                   p
          lr
                      p
             lrx
tree      4  3  4  3  0

find 2
query
          0  1  2  3  4
          ql qr
          p
          l     r
             p
          l  rx
    i        x
        ----------------
          qlr
          p
          l    r
             p
          l  r
                    p
          lrx
    i     x
update
          vi
          0  1  2  3  4
          p
          l     r
             p
          l  r
                p
                lrx
                   p
          lr
tree      4  0  4  0  0

find 5
query
          0  1  2  3  4
          ql qr
          p
          l     r
             p
          l  rx
          ---------------
                qlr
           p
           l    r
              p
           l  r
                   p
           lr
                      p
              lr
              p
                lr

```
Runtime: 644 ms, Beats 16.54%
Memory: 204.76 MB, Beats 33.27%
```
```c++
class SegmentTree {
public:
    vector<int> dp;
    SegmentTree(int n) {
        dp.resize(4 * n);
    }

    void build(int pos, int left, int right, vector<int> &arr)  {
        if (left == right) {
            dp[pos] = arr[left];
            return;
        }
        int mid = left + (right - left) / 2;
        build(2 * pos + 1, left, mid, arr);
        build(2 * pos + 2, mid + 1, right, arr);
        dp[pos] = max(dp[2 * pos + 1], dp[2 * pos + 2]);
    }

    int query(int pos, int left, int right, int q_left, int q_right)  {
        if (q_left <= left && q_right >= right) {
            return dp[pos];
        }
        if (q_left > right || q_right < left) { 
            return 0;
        }
        int mid = left + (right - left) / 2;
        return max(query(2 * pos + 1, left, mid, q_left, q_right),
                    query(2 * pos + 2, mid + 1, right, q_left, q_right));
    }

    void update(int pos, int left, int right, int i, int val)  {
        if (left == right) {
            dp[pos] = val;
            return;
        }
        int mid = left + (right - left) / 2;
        if (i <= mid) {
            update(2 * pos + 1, left, mid, i, val);
        } else { 
            update(2 * pos + 2, mid + 1, right, i, val);
        }
        dp[pos] = max(dp[2 * pos + 1], dp[2 * pos + 2]);
    }
};

void find(int val, SegmentTree &sgt, int n, int &ans) {
    int left = 0, right = n-1, mid, mx, i = -1;
    while (left <= right) {
        mid = left + (right - left) / 2;
        mx = sgt.query(0, 0, n - 1, 0, mid);
        if (mx >= val) {
            i = mid; 
            right = mid - 1; 
        } else {
            left = mid + 1;
        }
    }
    sgt.update(0, 0, n - 1, i, 0);
    return;
}

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = fruits.size(), i, ans = 0;
        SegmentTree sgt(n);
        sgt.build(0, 0, n - 1, baskets);
        for (i = 0; i < n; i ++) {
            if (sgt.dp[0] < fruits[i]) {
                ans += 1;
                continue;
            }
            find(fruits[i], sgt, n, ans);
        }
        return ans;
    }
};
```

**Solution 3: (Segment Tree, Binary Search, O(n logn))**
```
Runtime: 80 ms, Beats 88.80%
Memory: 204.79 MB, Beats 33.59%
```
```c++
class SegmentTree {
public:
    vector<int> dp;
    SegmentTree(int n) {
        dp.resize(4 * n);
    }

    void build(int ti, int left, int right, vector<int> &arr)  {
        if (left == right) {
            dp[ti] = arr[left];
            return;
        }
        int mid = left + (right - left) / 2;
        build(2 * ti + 1, left, mid, arr);
        build(2 * ti + 2, mid + 1, right, arr);
        dp[ti] = max(dp[2 * ti + 1], dp[2 * ti + 2]);
    }

    bool place(int ti, int left, int right, int val) {
        if (dp[ti] < val) {
            return false;
        }
        if (left == right) {
            dp[ti] = -1;
            return true;
        }
        int mid = left + (right - left) / 2;
        bool placed = place(2 * ti + 1, left, mid, val);
        if (!placed)
            placed = place(2 * ti + 2, mid + 1, right, val);
        dp[ti] = max(dp[2 * ti + 1], dp[2 * ti + 2]);
        return placed;
    }
};

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = fruits.size(), i, ans = 0;
        SegmentTree sgt(n);
        sgt.build(0, 0, n - 1, baskets);
        for (i = 0; i < n; i ++) {
            if (sgt.dp[0] < fruits[i]) {
                ans += 1;
                continue;
            }
            sgt.place(0, 0, n - 1, fruits[i]);
        }
        return ans;
    }
};
```
