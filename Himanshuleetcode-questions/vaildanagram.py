# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

def isAnagram(s, t):
    if len(s)!=len(t):
        return False
    freq1=[0]*26
    freq2=[0]*26
    for ch in s:
        freq1[ord(ch)-ord('a')]+=1
    for ch in t:
        freq2[ord(ch)-ord('a')]+=1
    return freq1==freq2
print(isAnagram("anagram","nagaram"))