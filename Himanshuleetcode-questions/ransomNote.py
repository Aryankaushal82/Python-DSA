# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

def canConstruct(ransomNote, magazine):
    d1={}
    for i in range(len(magazine)):
        if(magazine[i]) in d1:
            d1[magazine[i]]+=1
        else:
            d1[magazine[i]]=1
    for j in range(len(ransomNote)):
        if(ransomNote[j]) not in d1:
            return False
        else:
            d1[ransomNote[j]]-=1
    for k in d1.keys():
        if d1[k]<0:
            return False
    return True
print(canConstruct("aa","aab"))                