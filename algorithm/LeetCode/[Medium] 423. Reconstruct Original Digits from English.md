423. Reconstruct Original Digits from English

Given a **non-empty** string containing an out-of-order English representation of digits `0-9`, output the digits in ascending order.

**Note:**

1. Input contains only lowercase English letters.
1. Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
1. Input length is less than 50,000.

**Example 1:**
```
Input: "owoztneoer"

Output: "012"
```

**Example 2:**
```
Input: "fviefuro"

Output: "45"
```

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 44 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def originalDigits(self, s: str) -> str:
        names = [('zero','z','0'),('two','w','2'),('four','u','4'),('six','x','6'),('eight','g','8'),('one','o','1'),('three','t','3'),\
                 ('five','f','5'),('seven','s','7'),('nine','i','9')]
        result = []
        cnt = collections.Counter(s)
        for name in names:
            count = cnt[name[1]]
            if not count: continue
            for c in name[0]: cnt[c] -= count
            result.append(name[2]*count)
        return ''.join(sorted(result))
```

**Solution2: (Hash Table)**
```
Runtime: 32 ms
Memory Usage: 9.6 MB
```
```c++
class Solution {
public:
    string originalDigits(string s) {
        unordered_map<char, int>mp;
		for (auto c : s)
		{
			mp[c]++;
		}
		vector<int>count(10, 0);


		/*
			'e' : 0 1 3 5 7 8 9
			'f' : 4 5
			'g' : 8
			'h' : 3 8
			'i' : 5 6 8 9
			'n' : 1 7 9
			'o' : 0 1 2 4
			'r' : 0 3 4
			's' : 6 7
			't' : 2 3 8
			'u' : 4
			'v' : 5 7
			'w' : 2
			'x' : 6
			'z' : 0
		*/

		//8
		// How Many 'g' that many 8 in string
		while (mp['g'] > 0)
		{
			mp['e']--; mp['i']--; mp['g']--; mp['h']--; mp['t']--;
			count[8]++;
		}
		/*
			'e' : 0 1 3 5 7 9
			'f' : 4 5
			'h' : 3
			'i' : 5 6 9
			'n' : 1 7 9
			'o' : 0 1 2 4
			'r' : 0 3 4
			's' : 6 7
			't' : 2 3
			'u' : 4
			'v' : 5 7
			'w' : 2
			'x' : 6
			'z' : 0
		*/

		//3
		// How Many 'h' that many 3 in string
		while (mp['h'] > 0)
		{
			mp['t']--; mp['h']--; mp['r']--; mp['e']--; mp['e']--;
			count[3]++;
		}
		/*
			'e' : 0 1 5 7 9
			'f' : 4 5
			'i' : 5 6 9
			'n' : 1 7 9
			'o' : 0 1 2 4
			'r' : 0 4
			's' : 6 7
			't' : 2
			'u' : 4
			'v' : 5 7
			'w' : 2
			'x' : 6
			'z' : 0
		*/

		//2
		// How Many 't' that many 2 in string
		while (mp['t'] > 0)
		{
			mp['t']--; mp['w']--; mp['o']--;
			count[2]++;
		}
		/*
			'e' : 0 1 5 7 9
			'f' : 4 5
			'i' : 5 6 9
			'n' : 1 7 9
			'o' : 0 1 4
			'r' : 0 4
			's' : 6 7
			'u' : 4
			'v' : 5 7
			'x' : 6
			'z' : 0
		*/

		//4
		// How Many 'u' that many 4 in string
		while (mp['u'] > 0)
		{
			mp['f']--; mp['o']--; mp['u']--; mp['r']--;
			count[4]++;
		}
		/*
			'e' : 0 1 5 7 9
			'f' : 5
			'i' : 5 6 9
			'n' : 1 7 9
			'o' : 0 1
			'r' : 0
			's' : 6 7
			'v' : 5 7
			'x' : 6
			'z' : 0
		*/

		//5
		// How Many 'f' that many 5 in string
		while (mp['f'] > 0)
		{
			mp['f']--; mp['i']--; mp['v']--; mp['e']--;
			count[5]++;
		}
		/*
			'e' : 0 1 7 9
			'i' : 6 9
			'n' : 1 7 9
			'o' : 0 1
			'r' : 0
			's' : 6 7
			'v' : 7
			'x' : 6
			'z' : 0
		*/

		//0
		// How Many 'r' that many 0 in string
		while (mp['r'] > 0)
		{
			mp['z']--; mp['e']--; mp['r']--; mp['o']--;
			count[0]++;
		}
		/*
			'e' : 1 7 9
			'i' : 6 9
			'n' : 1 7 9
			'o' : 1
			's' : 6 7
			'v' : 7
			'x' : 6
		*/

		//1
		// How Many 'o' that many 1 in string
		while (mp['o'] > 0)
		{
			mp['o']--; mp['n']--; mp['e']--;
			count[1]++;
		}
		/*
			'e' : 7 9
			'i' : 6 9
			'n' : 7 9
			's' : 6 7
			'v' : 7
			'x' : 6
		*/

		//7
		// How Many 'v' that many 7 in string
		while (mp['v'] > 0)
		{
			mp['s']--; mp['e']--; mp['v']--; mp['e']--; mp['n']--;
			count[7]++;
		}
		/*
			'e' : 9
			'i' : 6 9
			'n' : 9
			's' : 6
			'x' : 6
		*/

		//9
		// How Many 'e' that many 9 in string
		while (mp['e'] > 0)
		{
			mp['n']--; mp['i']--; mp['n']--; mp['e']--;
			count[9]++;
		}
		/*
			'i' : 6
			's' : 6
			'x' : 6
		*/

		//6
		// How Many 'i' that many 6 in string
		while (mp['i'] > 0)
		{
			mp['s']--; mp['i']--; mp['x']--;
			count[6]++;
		}
		/*

		*/

		string ans = "";
		for (int i = 0; i <= 9; i++)
		{
			if (count[i])
			{
				ans += string(count[i], char(i + '0'));
			}
		}
		return ans;
    }
};
```
