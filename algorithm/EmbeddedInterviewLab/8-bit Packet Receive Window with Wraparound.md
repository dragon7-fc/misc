8-bit Packet Receive Window with Wraparound

Packets carry an 8-bit sequence number that wraps from 255 back to 0. Implement a receiver that accepts new packets, rejects duplicates, and tolerates limited out-of-order delivery.

Maintain a 32-packet receive window:
```
class SequenceWindow {
public:
    // Return true if this sequence number should be accepted.
    // Return false for a duplicate, stale packet, or ambiguous ordering.
    bool accept(uint8_t seq);
};
```

Use half-range serial-number arithmetic:

* Relative to the newest accepted sequence number newest, seq is newer when `uint8_t(seq - newest)` is in `1..127`.
* A forward distance of exactly `128` is ambiguous and must be rejected.
* The window contains the newest sequence and the previous 31 sequence numbers.
* A previously unseen packet within that 32-packet window may arrive out of order and should be accepted once.
* A packet more than 31 positions behind the newest packet is stale and must be rejected.
* A convenient representation is a 32-bit bitmap where bit 0 represents newest, bit 1 represents newest - 1, and so on.

Examples:
```
accept(254) -> true      // first packet
accept(255) -> true
accept(0)   -> true      // wraparound, newer than 255
accept(255) -> false     // duplicate within window
accept(253) -> true      // out of order, still within window and unseen
accept(253) -> false     // duplicate
```

If a newly accepted sequence jumps forward by 32 or more positions, all older bitmap history falls outside the receive window.

# Submissions
---
**Solution 1: (Math)**
```c++
class SequenceWindow {
public:
    bool accept(uint8_t seq) {
        if (!initialized_) {
            initialized_ = true;
            newest_ = seq;
            seen_ = 1u;
            return true;
        }

        uint8_t forward = static_cast<uint8_t>(seq - newest_);
        if (forward == 0 || forward == 128) return false;

        if (forward < 128) {
            if (forward >= 32) {
                seen_ = 1u;
            } else {
                seen_ = static_cast<uint32_t>((seen_ << forward) | 1u);
            }
            newest_ = seq;
            return true;
        }

        uint8_t back = static_cast<uint8_t>(newest_ - seq);
        if (back >= 32) return false;

        uint32_t mask = 1u << back;
        if ((seen_ & mask) != 0) return false;
        seen_ |= mask;
        return true;
    }

private:
    bool initialized_ = false;
    uint8_t newest_ = 0;
    uint32_t seen_ = 0;
};
```
