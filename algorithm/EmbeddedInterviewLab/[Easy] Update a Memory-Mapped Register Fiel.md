Update a Memory-Mapped Register Fiel

A hardware register often contains several independent bit fields. Implement a pure helper that models the read-modify-write calculation for one field.
```
uint32_t updateRegister(uint32_t reg, uint32_t mask, uint32_t value);
```

`mask` marks the bits that may change. `value` is already positioned in the register; only `value & mask` is written. Every bit outside mask must remain exactly as it was.

Example:
```
reg   = 0b10101100
mask  = 0b00111100
value = 0b00010000
output= 0b10010000
```

The judge models the register as an ordinary uint32_t. In real firmware, an MMIO register is usually accessed through a volatile pointer and may have special semantics such as write-one-to-clear (W1C); those concerns are discussed in evaluation/follow-up rather than simulated by this pure function.

# Submissions
---
**Solution 1: (Bit Manipulation)**
```c++
#include <cstdint>

uint32_t updateRegister(uint32_t reg, uint32_t mask, uint32_t value) {
    // Your code here
    return reg & ~mask | value & mask;
}
```
