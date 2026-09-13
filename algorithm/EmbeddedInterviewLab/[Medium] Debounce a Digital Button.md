Debounce a Digital Button

A GPIO button is sampled at a fixed interval. Raw samples are 0 or 1, but mechanical bounce can briefly alternate between them.

Implement:
```
std::vector<uint8_t> debounce(const std::vector<uint8_t>& samples,
                              size_t stableCount);
```

The debounced state starts at `0`. It changes only after seeing `stableCount` consecutive samples equal to the opposite state. Return the debounced state after every input sample. `stableCount >= 1`.

Example:
```
samples     = [0,1,1,1,0,1,0,0,0]
stableCount = 3
output      = [0,0,0,1,1,1,1,1,0]
```
A sample equal to the current debounced state cancels any pending opposite-state run.

# Submissions
---
**Solution 1: (Greedy, previous and current sample value)**
```c++
std::vector<uint8_t> debounce(const std::vector<uint8_t>& samples,
                              size_t stableCount) {
    // Your code here
    std::vector<uint8_t> ans;

    int pre = -1;      // Tracks the most recent sample value seen
    size_t k = 0;      // Tracks consecutive count of 'pre'
    uint8_t state = 0;     // Current debounced state (starts at 0)

    for (const auto &sample : samples) {
        // 1. If sample equals current debounced state, cancel any pending opposite run
        if (sample == state) {
            pre = sample;
            k = 0;
        } 
        // 2. If sample changed from previous sample, start a new run of length 1
        else if (sample != pre) {
            pre = sample;
            k = 1;
        } 
        // 3. Otherwise, sample == pre (and sample != state): increment consecutive run
        else {
            k += 1;
        }

        // 4. Update state when stableCount consecutive opposite-state samples are reached
        if (k >= stableCount) {
            state = pre;
            k = 0;
        }

        ans.push_back(state);
    }

    return ans;
}
```

**Solution 2: (Greedy, sample -> candidate -> stable answer)**
```c++
std::vector<uint8_t> debounce(const std::vector<uint8_t>& samples,
                              size_t stableCount) {
    // Your code here
    vector<uint8_t> ans;
    uint8_t stable = 0;
    uint8_t candidate = stable;
    size_t k = 0;
    for (const auto &sample: samples) {
        if (sample == stable) {
            candidate = stable;
            k = 0;
        } else if (sample != candidate) {
            candidate = sample;
            k = 1;
        } else {
            // sample != stable && sample == candidate
            k += 1;
        }

        if (k >= stableCount) {
            stable = candidate;
            k = 0;
        }
        ans.push_back(stable);
    }
    return ans;
}
```
