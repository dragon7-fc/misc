Atomic ISR Event Flags

An interrupt handler and a foreground task share a 32-bit event flag word. The ISR may set one or more bits; the foreground task periodically takes all pending bits and clears them.

Implement the operations using atomic read-modify-write primitives so an event is not lost if set() races with take().
```
class EventFlags {
public:
    void set(uint32_t mask);   // OR mask into pending flags
    uint32_t take();           // atomically return all flags and clear them
};
```

Sequential examples:
```
set(0x01), set(0x04), take() -> 0x05
next take()                 -> 0x00
set(0x02), set(0x02), take()-> 0x02
```

For C, use C11 atomics. For C++, use `std::atomic<uint32_t>`. Do not protect the operations with busy-wait polling. The judge verifies the operation semantics; the evaluator also checks that the implementation uses atomic RMW rather than a vulnerable load/modify/store sequence.

Target note: The judge uses standard atomics. In actual ISR code, the atomic operations used here must be lock-free/ISR-safe on the target; otherwise use the platform's interrupt-safe primitive or a short critical section.

# Submissions
---
**Solution 1: (Brute Force)**
```c++
#include <atomic>
#include <cstdint>

class EventFlags {
public:
    void set(uint32_t mask) {
        flags_.fetch_or(mask);
    }

    uint32_t take() {
        return flags_.exchange(0);
    }

private:
    std::atomic<uint32_t> flags_{0};
};
```
