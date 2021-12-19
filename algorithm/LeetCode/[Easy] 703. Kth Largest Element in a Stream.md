703. Kth Largest Element in a Stream

Design a class to find the `k`th largest element in a stream. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

Your KthLargest class will have a constructor which accepts an integer `k` and an integer array `nums`, which contains initial elements from the stream. For each call to the method `KthLargest.add`, return the element representing the `k`th largest element in the stream.

**Example:**
```
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
```

**Note:**

* You may assume that `nums' length ≥ k-1` and `k ≥ 1`.

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 84 ms
Memory Usage: 16.6 MB
```
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h, self.k = nums, k
        heapq.heapify(self.h)
        while len(self.h) > self.k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val > self.h[0]:
            heapq.heappushpop(self.h, val)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```

**Solution 2: (Heap)**
```
Runtime: 36 ms
Memory Usage: 14.5 MB
```
```c
typedef struct {
    int *nums;
    int k;
    int size;
} KthLargest;
int cmp(const int*a,const int*b){
    return *b-*a;
}
void swap(int *a,int* b){
    int mi=*a;
    *a=*b;
    *b=mi;
}
void MinHeapFixDown(int i,int* nums, int numsSize){
    int j=2*i+1;
    while(j<numsSize){
        if(j+1<numsSize&&nums[j+1]<nums[j])
            j++;
        if(nums[i]>nums[j])
            swap(&(nums[i]),&(nums[j]));
        else
            break;
        i=j;
        j=2*i+1;
    }
}
void CreateMinHeap(int* nums, int numsSize){
    for(int i=numsSize/2-1;i>=0;i--){
        MinHeapFixDown(i,nums,numsSize);
    }
}
KthLargest* kthLargestCreate(int k, int* nums, int numsSize) {
    KthLargest* obj=(KthLargest*)malloc(sizeof(KthLargest));
    obj->nums=(int*)malloc(k*sizeof(int));
    qsort(nums,numsSize,sizeof(int),cmp);
    for(int i=0;i<k&&i<numsSize;i++){
        obj->nums[i]=nums[i];
    }
    obj->k=k;
    if(k>numsSize)
        k=numsSize;
    obj->size=k;
    CreateMinHeap( obj->nums,k);
    return obj;
}

int kthLargestAdd(KthLargest* obj, int val) {
    if(obj->size<obj->k){
        obj->nums[obj->size]=val;
        int i=obj->size;
        int j=(i-1)/2;
        for(;j>=0&&obj->nums[j]>obj->nums[i];i=j,j=(i-1)/2){
            swap(&(obj->nums[i]),&(obj->nums[j]));
        }
        obj->size++;
        return obj->nums[0];
    }
    if(val<=obj->nums[0])
        return obj->nums[0];
    else{
        obj->nums[0]=val;
        MinHeapFixDown(0,obj->nums,obj->k);
        return obj->nums[0];
    }
}
void kthLargestFree(KthLargest* obj) {
    free(obj->nums);
    free(obj);
}


/**
 * Your KthLargest struct will be instantiated and called as such:
 * KthLargest* obj = kthLargestCreate(k, nums, numsSize);
 * int param_1 = kthLargestAdd(obj, val);
 
 * kthLargestFree(obj);
*/
```
