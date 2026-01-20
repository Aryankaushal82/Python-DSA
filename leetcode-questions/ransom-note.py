
def canConstruct( ransomNote, magazine):
    map  = {}
    for i in range(len(magazine)):
        if(magazine[i] in map):
            map[magazine[i]]+=1
        else:
            map[magazine[i]]=1
    
    for i in range(len(ransomNote)):
        if map.get(ransomNote[i], 0) > 0:
            map[ransomNote[i]]-=1
        else:
            return False
    return True