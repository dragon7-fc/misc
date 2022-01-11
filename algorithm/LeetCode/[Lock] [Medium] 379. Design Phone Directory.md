379. Design Phone Directory

Design a phone directory that initially has maxNumbers empty slots that can store numbers. The directory should store numbers, check if a certain slot is empty or not, and empty a given slot.

Implement the `PhoneDirectory` class:

* `PhoneDirectory(int maxNumbers)` Initializes the phone directory with the number of available slots `maxNumbers`.
* `int get()` Provides a number that is not assigned to anyone. Returns -1 if no number is available.
* `bool check(int number)` Returns `true` if the slot `number` is available and `false` otherwise.
* `void release(int number)` Recycles or releases the slot `number`.
 

**Example 1:**

```
Input
["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
[[3], [], [], [2], [], [2], [2], [2]]
Output
[null, 0, 1, true, 2, false, null, true]

Explanation
PhoneDirectory phoneDirectory = new PhoneDirectory(3);
phoneDirectory.get();      // It can return any available phone number. Here we assume it returns 0.
phoneDirectory.get();      // Assume it returns 1.
phoneDirectory.check(2);   // The number 2 is available, so return true.
phoneDirectory.get();      // It returns 2, the only number that is left.
phoneDirectory.check(2);   // The number 2 is no longer available, so return false.
phoneDirectory.release(2); // Release number 2 back to the pool.
phoneDirectory.check(2);   // Number 2 is available again, return true.
```

Constraints:

* `1 <= maxNumbers <= 10^4`
* `0 <= number < maxNumbers`
* At most `2 * 10^4` calls will be made to `get`, `check`, and `release`.

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 101 ms
Memory Usage: 15.9 MB
```
```c



typedef struct {
    bool *inUse;
    int maxSize;
} PhoneDirectory;


PhoneDirectory* phoneDirectoryCreate(int maxNumbers) {
    PhoneDirectory* phnDir = (PhoneDirectory*) malloc(sizeof(PhoneDirectory));
    bool *array = calloc(1, sizeof(bool) * maxNumbers);
    phnDir->inUse = array;
    phnDir->maxSize= maxNumbers;
    int i;
    for(i=0;i<maxNumbers;i++){
        phnDir->inUse[i] = false;
    }
    return phnDir;
}

int phoneDirectoryGet(PhoneDirectory* obj) {
    int i;
    int max = obj->maxSize;
    for(i=0;i<max;i++){
        if(obj->inUse[i] == false){
            obj->inUse[i] = true;
            return i;
        }
    }
    return -1;
}

bool phoneDirectoryCheck(PhoneDirectory* obj, int number) {
    if(number >= obj->maxSize){
        return false;
    }  
    if(obj->inUse[number] == false){
        return true;
    }
    else{
        return false;
    }
}

void phoneDirectoryRelease(PhoneDirectory* obj, int number) {
    if(number >= obj->maxSize){
        return;
    }  
    
    obj->inUse[number] = false;
}

void phoneDirectoryFree(PhoneDirectory* obj) {
    free(obj->inUse);
    free(obj);
}

/**
 * Your PhoneDirectory struct will be instantiated and called as such:
 * PhoneDirectory* obj = phoneDirectoryCreate(maxNumbers);
 * int param_1 = phoneDirectoryGet(obj);
 
 * bool param_2 = phoneDirectoryCheck(obj, number);
 
 * phoneDirectoryRelease(obj, number);
 
 * phoneDirectoryFree(obj);
*/
```
