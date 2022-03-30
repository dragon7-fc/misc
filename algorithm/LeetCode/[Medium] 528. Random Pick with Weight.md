528. Random Pick with Weight

Given an array w of positive integers, where `w[i]` describes the weight of index `i`, write a function `pickIndex` which randomly picks an index in proportion to its weight.

**Note:**

* `1 <= w.length <= 10000`
* `1 <= w[i] <= 10^5`
* `pickIndex` will be called at most `10000` times.

**Example 1:**
```
Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
```

**Example 2:**
```
Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
```

**Explanation of Input Syntax:**

The input is two lists: the subroutines called and their arguments. `Solution`'s constructor has one argument, the array `w`. `pickIndex` has no arguments. Arguments are always wrapped with a list, even if there aren't any.

# Submissions
---
**Solution 1: (Random, Binary Search)**

* Sum all left weights for each index.
* Then generate a random value between 0 and len(w) to see in which section it falls.
* To do that, we can perform a binarysearch.

```
Runtime: 236 ms
Memory Usage: 17.4 MB
```
```python
class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.w = w  # prefix sum

    def pickIndex(self) -> int:
        ranint = random.randint(1, self.w[-1])
        return bisect.bisect_left(self.w, ranint)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```

**Solution 2: (Binary Search)**
```
Runtime: 116 ms
Memory Usage: 28.4 MB
```
```c



typedef struct {
    int* w;
    int size;
    int* counts;
    int total;
} Solution;


Solution* solutionCreate(int* w, int wSize) {
    int i;
    Solution* obj = NULL;
    
    obj = (Solution*)malloc(sizeof(Solution));
    obj->w = w;
    obj->size = wSize;
    obj->counts = (int*)calloc(wSize,sizeof(int));
    obj->counts[0] = w[0];
    for(i=1;i<wSize;i++)
    {
        obj->counts[i] = obj->counts[i-1] + w[i];
    }
    obj->total = obj->counts[i-1];
    
    return obj;
}

int search(int* arr, int size, int target)
{
    int left = 0, right = size - 1, mid;
    
    while(left<right)
    {
        mid = left + (right-left)/2;
        if(arr[mid] == target)
        {
            return mid+1;
        }
        else if(arr[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid;
        }
    }
    
    return left;
}

int solutionPickIndex(Solution* obj) {
    int pos = rand()%obj->total;
    
    return search(obj->counts,obj->size,pos);
}

void solutionFree(Solution* obj) {
    free(obj->counts);
    free(obj);
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(w, wSize);
 * int param_1 = solutionPickIndex(obj);
 
 * solutionFree(obj);
*/
```

**Solution 3: (Random, Binary Search)**
```
Runtime: 68 ms
Memory Usage: 40.1 MB
```
```c++
class Solution {
    int sum = 0,n;
    vector<int>pre;
public:
    Solution(vector<int>& w) {
        n = w.size();
        for(auto x:w) sum+=x;
        pre.resize(n);
        pre[0] = w[0];
        for(int i=1;i<n;i++){
            pre[i] = (pre[i-1]+w[i]);
        }
    }
    
    int pickIndex() {
        int x = (rand()%sum)+1;
        int idx = lower_bound(pre.begin(),pre.end(),x)-pre.begin();
        return idx;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
```
