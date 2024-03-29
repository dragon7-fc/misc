929. Unique Email Addresses

Every email consists of a local name and a domain name, separated by the `@` sign.

For example, in `alice@leetcode.com`, `alice` is the local name, and `leetcode.com` is the domain name.

Besides lowercase letters, these emails may contain `'.'`s or `'+'`s.

If you add periods (`'.'`) between some characters in the **local name** part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, `"alice.z@leetcode.com"` and `"alicez@leetcode.com"` forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus (`'+'`) in the **local name**, everything after the first plus sign will be **ignored**. This allows certain emails to be filtered, for example `m.y+name@email.com` will be forwarded to `my@email.com`.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

 

**Example 1:**
```
Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
```

**Note:**

* `1 <= emails[i].length <= 100`
* `1 <= emails.length <= 100`
* Each `emails[i]` contains exactly one `'@'` character.
* All local and domain names are non-empty.
* Local names do not start with a `'+'` character.

# Solution
---
## Approach 1: Canonical Form
**Intuition and Algorithm**

For each email address, convert it to the canonical address that actually receives the mail. This involves a few steps:

* Separate the email address into a `local` part and the `rest` of the address.

* If the local part has a `'+'` character, remove it and everything beyond it from the `local` part.

* Remove all the zeros from the `local` part.

* The canonical address is `local + rest`.

After, we can count the number of unique canonical addresses with a `Set` structure.

```python
class Solution(object):
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)
```

**Complexity Analysis**

* Time Complexity: $O(\mathcal{C})$, where $\mathcal{C}$ is the total content of emails.

* Space Complexity: $O(\mathcal{C})$.

# Submissions
---
**Solution 1: (Canonical Form)**
```
Runtime: 40 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)
```

**Solution 2: (Set)**
```
Runtime: 24 ms
Memory Usage: 14.1 MB
```
```c++
class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> unique_emails;
        for(auto & email:emails)
        {
            int pos = email.find('@');
            string domain = email.substr(pos);
            string local_name=email.substr(0,pos);
            if((pos=local_name.find('+'))!=string::npos)
               local_name.erase(pos);
            pos=-1;
            while((pos=local_name.find('.',pos+1))!=string::npos)
               local_name.erase(pos,1);
            unique_emails.insert(local_name+domain);
        }
        return unique_emails.size();
    }
};
```
