Parse UART Frames from a Byte Stream

A UART byte stream contains zero or more framed packets mixed with noise.

Frame format:
```
0xAA | 0x55 | LEN | PAYLOAD[LEN] | CHECKSUM
```

* `LEN` is 0..64.
* `CHECKSUM` is the low 8 bits of the sum of all payload bytes.
* Return the payload of every valid frame in order.
* If a candidate header has an invalid length, bad checksum, or is truncated, advance by one byte from that candidate start and continue searching so the parser can resynchronize.

C++ signature:
```
std::vector<std::vector<uint8_t>> parseUartFrames(const std::vector<uint8_t>& stream);
```

Example:
```
Input:  [0x00,0xAA,0x55,0x03,0x10,0x20,0x30,0x60]
Output: [[0x10,0x20,0x30]]
```

This models the same framing/resynchronization logic used by a streaming UART state machine while keeping the problem deterministic for an online judge.

# Submissions
---
**Solution 1: (Greedy, if pattern search fail start all over agagin)**
```c++
std::vector<std::vector<uint8_t>> parseUartFrames(const std::vector<uint8_t>& stream) {
    std::vector<std::vector<uint8_t>> out;
    size_t i = 0;
    while (i + 2 < stream.size()) {
        if (stream[i] != 0xAAu || stream[i + 1] != 0x55u) {
            ++i;
            continue;
        }
        size_t len = stream[i + 2];
        if (len > 64) {
            ++i;
            continue;
        }
        size_t frameSize = len + 4;
        if (frameSize > stream.size() - i) {
            ++i;
            continue;
        }
        uint8_t sum = 0;
        for (size_t j = 0; j < len; ++j) {
            sum = static_cast<uint8_t>(sum + stream[i + 3 + j]);
        }
        if (sum != stream[i + 3 + len]) {
            ++i;
            continue;
        }
        out.emplace_back(stream.begin() + i + 3, stream.begin() + i + 3 + len);
        i += frameSize;
    }
    return out;
}
```
