1618. Maximum Font to Fit a Sentence in a Screen

You are given a string `text`. We want to display text on a screen of width `w` and height `h`. You can choose any font size from array `fonts`, which contains the available font sizes **in ascending order**.

You can use the `FontInfo` interface to get the width and height of any character at any available font size.

The `FontInfo` interface is defined as such:
```
interface FontInfo {
  // Returns the width of character ch on the screen using font size fontSize.
  // O(1) per call
  public int getWidth(int fontSize, char ch);

  // Returns the height of any character on the screen using font size fontSize.
  // O(1) per call
  public int getHeight(int fontSize);
}
```

The calculated width of `text` for some `fontSize` is the sum of every `getWidth(fontSize, text[i])` call for each `0 <= i < text.length` (**0-indexed**). The calculated height of `text` for some fontSize is `getHeight(fontSize)`. Note that `text` is displayed on a **single line**.

It is guaranteed that `FontInfo` will return the same value if you call `getHeight` or `getWidth` with the same parameters.

It is also guaranteed that for any font size `fontSize` and any character `ch`:

* `getHeight(fontSize) <= getHeight(fontSize+1)`
* `getWidth(fontSize, ch) <= getWidth(fontSize+1, ch)`

Return the maximum font size you can use to display `text` on the screen. If `text` cannot fit on the display with any font size, return `-1`.

 

**Example 1:**
```
Input: text = "helloworld", w = 80, h = 20, fonts = [6,8,10,12,14,16,18,24,36]
Output: 6
```

**Example 2:**
```
Input: text = "leetcode", w = 1000, h = 50, fonts = [1,2,4]
Output: 4
```

**Example 3:**
```
Input: text = "easyquestion", w = 100, h = 100, fonts = [10,15,20,25]
Output: -1
```

**Constraints:**

1. `1 <= text.length <= 50000`
1. `text` contains only lowercase English letters.
1. `1 <= w <= 10^7`
1. `1 <= h <= 10^4`
1. `1 <= fonts.length <= 10^5`
1. `1 <= fonts[i] <= 10^5`
1. `fonts` is sorted in ascending order and does not contain duplicates.

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 874 ms
Memory Usage: 25.6 MB
```
```python
# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        
        def check(fs):
            
            # check height
            if fontInfo.getHeight(fs) > h:
                return False
            
            # check total width
            summ = 0
            for c in text:
                summ += fontInfo.getWidth(fs, c)
                if summ > w:
                    return False
            
            return True

        
        # Binary Search
		# we need to consider which the range of the result is
        left = 0
        right = len(fonts) - 1
        
        # the benefit to write left + 1 < right is that, crossing border case will never happen
        while left + 1 < right:
            
            # standard writing to get mid
            # if you write mid = (left + right) // 2, when left and right are too big, this will cost too much
            mid = left + (right - left) // 2
            
            if check(fonts[mid]):
                left = mid
                
            # when we see a value that can not be obtained as our result, we can exclude it in the next time's binary search
            # the difference between writing mid + 1 and mid is that, whether this value will be considered as a result
            # For example, 1 3 5, we want to get 3, then after checking 5 and we confirm that 5 is not ok, then 
            # we can execute right = mid - 1 instead right = mid, more accurate.
            else:
                right = mid - 1
        
        # side effect of left + 1 < right.
		# That is, left and right all can be the result that we want to get
		# so we need to confirm them seperately, but this process is a template process
		# we just do this after every binary search without any thinking
		# But the benefit is too good, that is, crossing border will never happen
        if check(fonts[right]):
            return fonts[right]
        
        elif check(fonts[left]):
            return fonts[left]
        
        else:
            return -1
```
