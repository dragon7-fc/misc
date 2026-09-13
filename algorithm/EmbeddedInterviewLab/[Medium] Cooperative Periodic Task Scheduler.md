Cooperative Periodic Task Scheduler

A cooperative firmware loop runs periodic tasks from a wrapping 32-bit tick counter. Each task stores its period and the tick of its next scheduled release.
```
struct PeriodicTask {
    uint32_t period;
    uint32_t nextRun;
};

uint32_t pollTask(PeriodicTask& task, uint32_t now);
```

Return how many releases are due at `now`, and advance `nextRun` to the **first scheduled release strictly after** `now`. If nothing is due, return 0 and do not modify `nextRun`.

Important: preserve the original schedule. Advance from the previous deadline, not from `now`, so late execution does not cause long-term drift.

Assumptions: `period > 0`; comparisons occur within the standard signed half-range (`< 2^31` ticks from the relevant deadline).

Example:
```
period=10, nextRun=100, now=103 -> returns 1, nextRun=110
period=10, nextRun=100, now=135 -> returns 4, nextRun=140
```

The logic must continue to work when `nextRun`/`now` wrap around `UINT32_MAX`.

# Submissions
---
**Solution 1: (Brute Force)**
```c++
#include <cstdint>

struct PeriodicTask {
    uint32_t period;
    uint32_t nextRun;
};

uint32_t pollTask(PeriodicTask& task, uint32_t now) {
    if (static_cast<int32_t>(now - task.nextRun) < 0) return 0;
    uint32_t elapsed = now - task.nextRun;
    uint32_t due = elapsed / task.period + 1u;
    task.nextRun += due * task.period;
    return due;
}
```
