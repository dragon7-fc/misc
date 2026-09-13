Implement memmove()

Implement memmove — copy `n` bytes from `src` to `dest` even if regions overlap, and return `dest`.

Overlap rule: if `dest > src` (destination starts at a higher address), a naive **forward** copy corrupts unread source bytes — copy **backward** from the end. If `dest < src`, forward copy is safe.

Do not call libc memmove/memcpy.

Example (overlap, shift right):
```
buf = [A B C D E]
memmove(buf+1, buf, 4)  // dest > src
→ [A A B C D]
```

# Submissions
---
**Solution 1: (Greedy)**
```c++
void* my_memmove(void* dest, const void* src, size_t n) {
        // Your code here
        if (dest == src || n == 0) {
            return dest;
        }
        unsigned char* d = dest;
        const unsigned char* s = src;
        if (d < s) {
            for (size_t i = 0; i < n; i ++) {
                d[i] = s[i]; 
            }
        } else {
            for (size_t i = n; i > 0; i --) {
                d[i - 1] = s[i - 1];
            }
        }
        return dest;
    }

// --- Test your solution ---
// int main() {
//     // Add a quick local test if helpful
//     return 0;
// }
```
