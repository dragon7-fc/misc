Decode Byte-Stuffed Serial Frames

Decode serial frames using HDLC/PPP-style byte stuffing.

Constants:
```
FLAG = 0x7E
ESC  = 0x7D
```
A frame starts and ends with FLAG. Inside a frame, a byte that needs escaping is transmitted as:
```
ESC, (original_byte XOR 0x20)
```

Thus `0x7E` becomes `0x7D 0x5E`, and `0x7D` becomes `0x7D 0x5D`.

Implement:
```
vector<vector<uint8_t>> decodeFrames(const vector<uint8_t>& stream);
```

Rules:

* Ignore bytes before the first `FLAG`.
* Consecutive `FLAG`s do not produce empty frames.
* `ESC` applies to exactly the following byte.
* If a frame ends immediately after an unmatched `ESC`, discard that frame.
* A closing `FLAG` may also serve as the opening delimiter for the next frame.

Example:
```
Input:  [7E, 01, 7D, 5E, 02, 7E]
Output: [[01, 7E, 02]]
```

# Submissions
---
**Solution 1: (Greedy)**
```c++
#include <cstdint>
#include <vector>
std::vector<std::vector<uint8_t>> decodeFrames(const std::vector<uint8_t>& stream) {
    // Your code here
    constexpr uint8_t FLAG = 0x7E;
    constexpr uint8_t ESC = 0x7D;
    std::vector<std::vector<uint8_t>> out;
    std::vector<uint8_t> cur;
    bool inFrame = false;
    bool escaped = false;

    for (uint8_t b : stream) {
        if (b == FLAG) {
            if (inFrame && !escaped && !cur.empty()) out.push_back(cur);
            cur.clear();
            inFrame = true;
            escaped = false;
            continue;
        }
        if (!inFrame) continue;
        if (escaped) {
            cur.push_back(static_cast<uint8_t>(b ^ 0x20));
            escaped = false;
        } else if (b == ESC) {
            escaped = true;
        } else {
            cur.push_back(b);
        }
    }
    return out;
}
```
