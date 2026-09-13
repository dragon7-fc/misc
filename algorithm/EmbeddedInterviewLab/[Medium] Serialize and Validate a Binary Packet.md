Serialize and Validate a Binary Packet

Implement serialization and parsing for a compact binary packet. Multi-byte fields use **network byte order (big-endian)**.

Packet format:
```
byte 0      : version          (uint8_t)
byte 1      : flags            (uint8_t)
bytes 2-3   : sequence         (uint16_t, big-endian)
bytes 4-5   : payloadLength    (uint16_t, big-endian)
next P bytes: payload          (P = payloadLength, maximum 256)
last byte   : checksum
```

The checksum is the low 8 bits of the sum of all preceding serialized bytes (the 6-byte header plus payload).

C++ API:
```
struct Packet {
    uint8_t version;
    uint8_t flags;
    uint16_t sequence;
    std::vector<uint8_t> payload;
};

bool serializePacket(const Packet& packet, std::vector<uint8_t>& out);
bool deserializePacket(const std::vector<uint8_t>& bytes, Packet& out);
Rules:
```

* `serializePacket` returns `false` when payload size exceeds `256`. On failure, out must be empty.
* `deserializePacket` rejects packets shorter than `7` bytes.
* Decode `payloadLength` from the packet itself and require the total input size to be exactly `7 + payloadLength`.
* Reject `payloadLength > 256`.
* Verify the checksum before modifying `out`.
* On any deserialize failure, leave `out` unchanged.
* Do not `memcpy` or cast a C/C++ struct directly onto the wire buffer; padding, alignment, and host endianness are not protocol formats.

Example:
```
Packet{version=1, flags=0xA5, sequence=0x1234, payload=[0x10,0x20]}
-> [01,A5,12,34,00,02,10,20,1E]
```

Here the checksum is `(0x01 + 0xA5 + 0x12 + 0x34 + 0x00 + 0x02 + 0x10 + 0x20) & 0xFF = 0x1E`.

# Submissions
---
**Solution 1: (Brute Force)**
```c++
struct Packet {
    uint8_t version;
    uint8_t flags;
    uint16_t sequence;
    std::vector<uint8_t> payload;
};

bool serializePacket(const Packet& packet, std::vector<uint8_t>& out) {
    // Your code here
    if (packet.payload.size() > 256) {
        return false;
    }
    vector<uint8_t> bytes;
    uint32_t sum = 0;
    bytes.push_back(packet.version);
    sum += bytes.back();
    bytes.push_back(packet.flags);
    sum += bytes.back();
    bytes.push_back(packet.sequence >> 8);
    sum += bytes.back();
    bytes.push_back((uint8_t)packet.sequence);
    sum += bytes.back();
    bytes.push_back(packet.payload.size() >> 8);
    sum += bytes.back();
    bytes.push_back((uint8_t)packet.payload.size());
    sum += bytes.back();
    for (const auto& byte: packet.payload) {
        bytes.push_back(byte);
        sum += byte;
    }
    bytes.push_back((uint8_t)sum);
    out = move(bytes);
    return true;
}

bool deserializePacket(const std::vector<uint8_t>& bytes, Packet& out) {
    // Your code here
    if (bytes.size() < 7) {
        return false;
    }
    uint16_t length = bytes[4] << 8;
    length += bytes[5];
    if (length > 256 || length + 7 != bytes.size()) {
        return false;
    }
    Packet packet;
    uint32_t sum = 0;
    packet.version = bytes[0];
    sum += bytes[0];
    packet.flags = bytes[1];
    sum += bytes[1];
    packet.sequence = bytes[2] << 8;
    sum += bytes[2];
    packet.sequence += bytes[3];
    sum += bytes[3];
    sum += bytes[4];
    sum += bytes[5];
    for (int j = 6; j < 6 + length; j ++) {
        packet.payload.push_back(bytes[j]);
        sum += bytes[j];
    }
    if ((uint8_t)sum == bytes.back()) {
        out = move(packet);
        return true;
    } else {
        return false;
    }
}
```

**Solution 2: (Brute Force)**
```c++
struct Packet {
    uint8_t version;
    uint8_t flags;
    uint16_t sequence;
    std::vector<uint8_t> payload;
};

bool serializePacket(const Packet& packet, std::vector<uint8_t>& out) {
    out.clear();
    if (packet.payload.size() > 256) return false;

    uint16_t length = static_cast<uint16_t>(packet.payload.size());
    out.reserve(7 + length);
    out.push_back(packet.version);
    out.push_back(packet.flags);
    out.push_back(static_cast<uint8_t>(packet.sequence >> 8));
    out.push_back(static_cast<uint8_t>(packet.sequence & 0xFFu));
    out.push_back(static_cast<uint8_t>(length >> 8));
    out.push_back(static_cast<uint8_t>(length & 0xFFu));
    out.insert(out.end(), packet.payload.begin(), packet.payload.end());

    uint32_t sum = 0;
    for (uint8_t byte : out) sum += byte;
    out.push_back(static_cast<uint8_t>(sum & 0xFFu));
    return true;
}

bool deserializePacket(const std::vector<uint8_t>& bytes, Packet& out) {
    if (bytes.size() < 7) return false;

    uint16_t length = static_cast<uint16_t>(
        (static_cast<uint16_t>(bytes[4]) << 8) |
        static_cast<uint16_t>(bytes[5]));

    if (length > 256) return false;
    if (bytes.size() != static_cast<size_t>(7) + length) return false;

    uint32_t sum = 0;
    for (size_t i = 0; i + 1 < bytes.size(); ++i) sum += bytes[i];
    if (static_cast<uint8_t>(sum & 0xFFu) != bytes.back()) return false;

    Packet parsed;
    parsed.version = bytes[0];
    parsed.flags = bytes[1];
    parsed.sequence = static_cast<uint16_t>(
        (static_cast<uint16_t>(bytes[2]) << 8) |
        static_cast<uint16_t>(bytes[3]));
    parsed.payload.assign(bytes.begin() + 6, bytes.end() - 1);

    out = std::move(parsed);
    return true;
}
```
