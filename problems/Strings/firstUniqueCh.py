"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""


import collections
def firstUniqueCh(s:str)->int:
    count = collections.Counter(s)
    for idx, val in enumerate(s):
        if count[val] == 1:
            return idx
    return -1


if __name__=='__main__':
    print (firstUniqueCh('leetcode'))
    print (firstUniqueCh('loveleetcode'))



"""
in java script:
function firstUniqChar(s) {
  const count = new Map();
  
  // Build hash map: character and how often it appears
  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    count.set(ch, (count.get(ch) || 0) + 1);
  }
  
  // Find the index
  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    if (count.get(ch) === 1) {
      return i;
    }
  }
  
  return -1;
}

"""