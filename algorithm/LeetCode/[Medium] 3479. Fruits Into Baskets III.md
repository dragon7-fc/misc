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

**Solution 2: (Segment Tree, Binary Search)**

    fruits = [4,2,5], baskets = [3,5,4]

sgt
                   5
               5       4
            3    5

query 4
                   4
               3        4
            3    0
query 2
                   4
               0       4
            0    0

```
Runtime: 607 ms, Beats 21.13%
Memory: 189.37 MB, Beats 30.91%
```
```c++
class SGT {
public:
    vector<int> tree;
    SGT(int n) {
        tree.resize(4*n + 1);
    }

    void build(int pos, int left, int right, vector<int> &arr)  {
        if (left == right) {
            tree[pos] = arr[left];
            return;
        }
        int mid = left + (right - left) / 2;
        build(2*pos + 1, left, mid, arr);
        build(2*pos + 2, mid + 1, right, arr);
        tree[pos] = max(tree[2*pos + 1], tree[2*pos + 2]);
    }

    int query(int pos, int q_left, int q_right, int left, int right)  {
        if (q_left <= left && q_right >= right) {
            return tree[pos];
        }
        if (q_left > right || q_right < left) { 
            return 0;
        }
        int mid = left + (right - left)/2;
        return max(query(2*pos + 1, q_left, q_right, left, mid), query(2*pos + 2, q_left, q_right, mid + 1, right));
    }

    void update(int pos, int left, int right, int i, int val)  {
        if (left == right) {
            tree[pos] = val;
            return;
        }
        int mid = left + (right - left)/2;
        if (i <= mid) {
            update(2*pos + 1, left, mid, i, val);
        } else { 
            update(2*pos + 2, mid + 1, right, i, val);
        }
        tree[pos] = max(tree[2*pos + 1], tree[2*pos + 2]);
    }
};

void find(int val, SGT &sgt, int n, int &ans) {
    int left = 0, right = n-1, mid, mx, i = -1;
    while (left <= right) {
        mid = left + (right - left)/2;
        mx = sgt.query(0, 0, mid, 0, n-1);
        if (mx >= val) {
            i = mid; 
            right = mid - 1; 
        } else {
            left = mid + 1;
        }
    }
    if (i != -1) {
        sgt.update(0, 0, n-1, i, 0);
    } else {
        ans += 1;
    }
    return;
}

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = fruits.size(), i, ans = 0;
        SGT sgt(n);
        sgt.build(0, 0, n-1, baskets);
        for (i = 0; i < n; i ++) {
            find(fruits[i], sgt, n, ans);
        }
        return ans;
    }
};
```
