Watchdog Task Health Monitor

A firmware system should kick its hardware watchdog only when every required software task has reported a recent heartbeat.

Each task stores the tick of its last heartbeat and the maximum allowed age:
```
struct TaskHealth {
    uint32_t lastHeartbeat;
    uint32_t timeout;
};

bool shouldKickWatchdog(const vector<TaskHealth>& tasks, uint32_t now);
```

A task is healthy when:

`(now - lastHeartbeat) <= timeout`

using 32-bit unsigned modular arithmetic. A task exactly at the timeout boundary is still healthy. Return true only if all tasks are healthy. An empty task list returns true.

Assumption: the true elapsed time since each heartbeat is less than `2^32` ticks, so unsigned subtraction represents that elapsed interval correctly.

Example:
```
now = 1050
[{last=1000, timeout=100}, {last=1030, timeout=50}] -> true
[{last=900,  timeout=100}, {last=1030, timeout=50}] -> false
```

# Submissions
---
**Solution 1: (Brute Force)**
```c++
#include <cstdint>
#include <vector>
#include <algorithm>

struct TaskHealth {
    uint32_t lastHeartbeat;
    uint32_t timeout;
};

bool shouldKickWatchdog(const std::vector<TaskHealth>& tasks, uint32_t now) {
    // Your code here
    if (all_of(tasks.begin(), tasks.end(), [&](const auto& task){return now - task.lastHeartbeat <= task.timeout;})) {
        return true;
    }
    return false;
}
```
