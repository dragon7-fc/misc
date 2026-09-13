CRC-16/CCITT-FALSE

Implement the CRC-16/CCITT-FALSE checksum for a byte buffer.

Parameters are fixed for this problem:

* width: 16
* polynomial: `0x1021`
* initial value: `0xFFFF`
* refin: false
* refout: false
* xorout: `0x0000`

C++ signature:
```
uint16_t crc16CcittFalse(const std::vector<uint8_t>& data);
```

A standard check vector is:
```
ASCII "123456789" -> 0x29B1
empty input       -> 0xFFFF
```

Do not call a CRC library. Process each byte most-significant-bit first.

# Submissions
---
**Solution 1: (Bit Manipulation)**
```c++
uint16_t crc16CcittFalse(const std::vector<uint8_t>& data) {
    // Your code here
    uint16_t crc = 0xffff;
    for (const auto &byte: data) {
        crc ^= byte << 8;
        for (int _ = 0; _ < 8; _ ++) {
            if (crc & (1 << 15)) {
                crc = crc << 1;
                crc ^= 0x1021;
            } else {
                crc <<= 1;
            }
        }
    }
    return crc;
}
```
