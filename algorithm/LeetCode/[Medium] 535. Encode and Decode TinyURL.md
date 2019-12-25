535. Encode and Decode TinyURL

>Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`.

Design the `encode` and `decode` methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# Submissions
---
**Solution 1:**
```
Runtime: 20 ms
Memory Usage: 12.1 MB
```
```python
import base64

class Codec:
    encoded = {}
    decoded = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.encoded:
            hashed_value = base64.b16encode(longUrl)
            self.encoded[longUrl] = hashed_value
        return 'http://tinyurl.com/{}'.format(self.encoded[longUrl])

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        hashed_value = shortUrl.rsplit("/")[-1]
        if hashed_value not in self.decoded:
            self.decoded[hashed_value] = base64.b16decode(hashed_value)
        return self.decoded[hashed_value]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```