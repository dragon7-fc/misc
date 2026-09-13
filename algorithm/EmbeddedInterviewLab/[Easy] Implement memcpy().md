Implement memcpy()

Implement memcpy — copy `n` bytes from `src` to `dest` and return `dest`.

**Assumptions (classic interview contract)**: regions do **not** overlap. If they might overlap, use `memmove`.

Do not call the standard library `memcpy`.

Example:
```
src  = {1,2,3,4}
n    = 4
dest = {0,0,0,0}
→ dest becomes {1,2,3,4}; return dest
```

# Submissions
---
**Solution 1: (Brute Force)**
```c++
void* my_memcpy(void* dest, const void* src, size_t n) {
        // Your code here
        unsigned char* d = dest;
        const unsigned char* s = src;
        for (size_t i = 0; i < n; i ++) {
            d[i] = s[i];
        }
        return dest;
    }

// --- Test your solution ---
// int main() {
//     // Add a quick local test if helpful
//     return 0;
// }
```
