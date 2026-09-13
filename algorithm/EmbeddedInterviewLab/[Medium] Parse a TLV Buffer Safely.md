Parse a TLV Buffer Safely

Parse a byte buffer containing consecutive **TLV** records.

Each record uses:
```
1 byte TYPE | 1 byte LENGTH | LENGTH bytes VALUE
```

C++ types:
```
struct Tlv {
    uint8_t type;
    std::vector<uint8_t> value;
};

bool parseTlv(const std::vector<uint8_t>& data, std::vector<Tlv>& out);
```

Return `true` only if the entire input is a valid sequence of TLVs. Empty input is valid and produces an empty result. On malformed input, return `false` and leave out empty.

Example:
```
Input:  [0x01,0x02,0xAA,0xBB, 0x02,0x01,0x05]
Output: [{type:1,value:[0xAA,0xBB]}, {type:2,value:[0x05]}]
```

Bounds checks must occur before reading the declared value length.

# Submissions
---
**Solution 1: (Brute Force)**
```c++
struct Tlv {
    uint8_t type;
    std::vector<uint8_t> value;
};

bool parseTlv(const std::vector<uint8_t>& data, std::vector<Tlv>& out) {
    std::vector<Tlv> parsed;
    size_t pos = 0;
    while (pos < data.size()) {
        if (data.size() - pos < 2) {
            out.clear();
            return false;
        }
        uint8_t type = data[pos++];
        size_t length = data[pos++];
        if (length > data.size() - pos) {
            out.clear();
            return false;
        }
        Tlv item;
        item.type = type;
        item.value.assign(data.begin() + pos, data.begin() + pos + length);
        parsed.push_back(std::move(item));
        pos += length;
    }
    out = std::move(parsed);
    return true;
}
```

**Solution 2: (Brute Force)**
```c++
struct Tlv {
    uint8_t type;
    std::vector<uint8_t> value;
};

bool parseTlv(const std::vector<uint8_t>& data, std::vector<Tlv>& out) {
    // Your code here
    std::vector<Tlv> parsed;

    size_t i = 0;
    const size_t n = data.size();

    while (i < n)
    {
        // Every TLV requires at least:
        // 1 byte type + 1 byte length
        if (n - i < 2)
        {
            return false;
        }

        const uint8_t type = data[i];
        const uint8_t length = data[i + 1];

        // Check that the complete value is available.
        // Use subtraction to avoid potential size_t overflow.
        if (n - i - 2 < length)
        {
            return false;
        }

        Tlv tlv;
        tlv.type = type;
        tlv.value.assign(data.begin() + i + 2,
                         data.begin() + i + 2 + length);

        parsed.push_back(std::move(tlv));

        i += 2 + length;
    }

    // Only modify out after the entire input is valid.
    out = std::move(parsed);

    return true;
}
```
