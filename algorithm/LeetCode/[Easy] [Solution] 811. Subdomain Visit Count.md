811. Subdomain Visit Count

A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list `cpdomains` of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

**Example 1:**
```
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.
```

**Example 2:**
```
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
```

**Notes:**

* The length of cpdomains will not exceed `100`. 
* The length of each domain name will not exceed `100`.
* Each address will have either `1` or `2` `"."` characters.
* The input count in any count-paired domain will not exceed `10000`.
* The answer output can be returned in any order.

# Solution
---
## Approach #1: Hash Map [Accepted]
**Intuition and Algorithm**

The algorithm is straightforward: we just do what the problem statement tells us to do.

For an address like `a.b.c`, we will count `a.b.c`, `b.c`, and `c`. For an address like `x.y`, we will count `x.y` and `y`.

To count these strings, we will use a hash map. To split the strings into the required pieces, we will use library `split` functions.

```python
class Solution(object):
    def subdomainVisits(self, cpdomains):
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in xrange(len(frags)):
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of cpdomains, and assuming the length of `cpdomains[i]` is fixed.

* Space Complexity: $O(N)$, the space used in our count.

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 52 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
```

**Solution 2: (uthash)**
```
Runtime: 4 ms
Memory Usage: 12.7 MB
```
```c
#define STRLENTH 110

typedef struct{
    char domain[STRLENTH];
    int count;
    UT_hash_handle hh;
}my_hash;

void add_domain(my_hash **webs,char name[STRLENTH],int num)
{
    my_hash *s;
    HASH_FIND_STR(*webs,name,s);
    if (s!=NULL)
    {
        s->count+=num;
    }
    else
    {
        s=malloc(sizeof(my_hash));
        s->count=num;
        strcpy(s->domain,name);
        HASH_ADD_STR(*webs,domain,s);
    }
} 

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** subdomainVisits(char ** cpdomains, int cpdomainsSize, int* returnSize){
    my_hash *webs=NULL;
    my_hash *s,*tmp;
    int i,j,l,c,d,num;
    char cut[STRLENTH]="";
    char **result;
    for (i=0;i<cpdomainsSize;i++)
    {
        l=strlen(cpdomains[i]);
        c=0;
        j=0;
        while (cpdomains[i][j]!='\0')
        {
            if ((cpdomains[i][j]==' ')&&(c==0))
            {
                c=j;
                memcpy(cut,cpdomains[i],c);
                num=atoi(cut);
                d=j+1;
                memcpy(cut,cpdomains[i]+d,l-d+1);
                add_domain(&webs,cut,num);
            }
            if (cpdomains[i][j]=='.')
            {
                d=j+1;
                memcpy(cut,cpdomains[i]+d,l-d+1);
                add_domain(&webs,cut,num);
            }
            j++;
        }
    }
    result=(char**)malloc(sizeof(char*)*cpdomainsSize*3);
    for (i=0;i<cpdomainsSize*3;i++)
        result[i]=(char*)malloc(sizeof(char)*STRLENTH);  
    i=0;
    HASH_ITER(hh,webs,s,tmp)
    {
        sprintf(cut,"%d %s",s->count,s->domain);
        strcpy(result[i],cut);
        i++;
    }
    *returnSize=i;
    return result;
}
```

**Solution 3: (Hash Table, String)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 16.49 MB, Beats 30.51%
```
```c++
class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        int i, k;
        string s;
        unordered_map<string,int> cnt;
        vector<string> ans;
        for (auto domain: cpdomains) {
            stringstream ss(domain);
            getline(ss, s, ' ');
            k = stoi(s);
            getline(ss, s);
            cnt[s] += k;
            for (i = 1; i < s.length(); i ++) {
                if (s[i] == '.') {
                    cnt[s.substr(i+1)] += k;
                }
            }
        }
        for (auto [cs, ck]: cnt) {
            ans.push_back(to_string(ck) + " " + cs);
        }
        return ans;

    }
};
```
