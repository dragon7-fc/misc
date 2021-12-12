535. Encode and Decode TinyURL

>Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`.

Design the `encode` and `decode` methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# Submissions
---
**Solution 1: (Math, Base64, Hash Table)**
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

**Solution 2: (Math, Count, Hash Table)**
```
Runtime: 36 ms
Memory Usage: 13.9 MB
```
```python
class Codec:
    def __init__(self):
        self.url_map = {}
        self.count = 1

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if self.url_map.get(longUrl):
            return
        self.url_map[self.count] = longUrl
        self.count += 1
        
        return self.count - 1

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_map[int(shortUrl)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```

**Solution 3: (Hash Table)**
```
Runtime: 3 ms
Memory Usage: 6 MB
```
```c
void strcopy(char* src, char* dest){
    int i;
    for(i=0;src[i];i++){
        dest[i]=src[i];
    }
    dest[i]=src[i];
}
char lUrl[10000];
char base62[65]= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

/** Encodes a URL to a shortened URL. */
char* encode(char* longUrl) {
    int i;
    char* s = (char*)malloc(sizeof(char)*10);
    for(i=0;i<=7;i++){
        s[i]=base62[longUrl[i]%62];
    }
    s[i]='\0';
    strcopy(longUrl,lUrl);
    return s;
}

/** Decodes a shortened URL to its original URL. */
char* decode(char* shortUrl) {
    return lUrl;
}

// Your functions will be called as such:
// char* s = encode(s);
// decode(s);
```
