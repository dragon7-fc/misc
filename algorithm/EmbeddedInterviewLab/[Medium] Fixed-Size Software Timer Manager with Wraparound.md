Fixed-Size Software Timer Manager with Wraparound

A firmware system has a free-running 32-bit millisecond tick counter that wraps naturally from UINT32_MAX to 0.

Implement a fixed-size one-shot software timer manager for 8 timers. The manager must not dynamically allocate storage for timer state.

```
class SoftwareTimerManager {
public:
    static constexpr size_t kTimerCount = 8;

    // Start or restart timer id at tick `now`.
    // Return false when id is invalid.
    bool startTimer(size_t id, uint32_t now, uint32_t timeout);

    // Cancel timer id. Return false when id is invalid.
    bool cancelTimer(size_t id);

    // Return IDs that have expired as of `now`.
    // Expired timers are one-shot: polling them deactivates them.
    std::vector<size_t> pollExpired(uint32_t now);

    bool isActive(size_t id) const;
};
```

For each active timer, expiration is based on elapsed unsigned time:
```
elapsed = uint32_t(now - start)
expired when elapsed >= timeout
```

Assume the true elapsed interval for any active timer is less than `2^32` ticks. Do not store or compare an absolute deadline such as `start + timeout`; that fails when the counter wraps.

Requirements:

* `IDs` are `0..7`.
* Starting an active timer restarts it with the `new` `now` and `timeout`.
* `timeout == 0` is allowed and expires on the next call to pollExpired.
* pollExpired returns expired IDs in increasing ID order.
* A timer is returned at most once unless it is started again.

Example:
```
startTimer(2, 0xFFFFFFFA, 10)
pollExpired(3)  -> []      // elapsed = 9
pollExpired(4)  -> [2]     // elapsed = 10 across wrap
pollExpired(20) -> []      // already deactivated
```

# Submissions
---
**Solution 1: (Brute Force)**
```c++
class SoftwareTimerManager {
public:
    static constexpr size_t kTimerCount = 8;

    bool startTimer(size_t id, uint32_t now, uint32_t timeout) {
        // Your code here
        if (id >= kTimerCount) {
            return false;
        }
        timers_[id].active = true;
        timers_[id].start = now;
        timers_[id].timeout = timeout;
        return true;
    }

    bool cancelTimer(size_t id) {
        // Your code here
        if (id >= kTimerCount || !timers_[id].active) {
            return false;
        }
        timers_[id].active = false;
        return true;
    }

    std::vector<size_t> pollExpired(uint32_t now) {
        // Your code here
        vector<size_t> rst;
        for (int i = 0; i < kTimerCount; i ++) {
            if (!timers_[i].active) {
                continue;
            }
            uint32_t elapsed = now - timers_[i].start;
            if (elapsed >= timers_[i].timeout) {
                timers_[i].active = false;
                rst.push_back(i);
            }
        }
        return rst;
    }

    bool isActive(size_t id) const {
        // Your code here
        if (id >= kTimerCount) {
            return false;
        }
        return timers_[id].active;
    }

private:
    struct Timer {
        bool active = false;
        uint32_t start = 0;
        uint32_t timeout = 0;
    };

    std::array<Timer, kTimerCount> timers_{};
};
```
