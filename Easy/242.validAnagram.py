def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    if len(s) != len(t):
        return False
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True
    
    # s_dict = {}
    # for c in s:
    #     if c in s_dict:
    #         s_dict[c] += 1
    #     else:
    #         s_dict[c] = 1

    # for c in t:
    #     if c in s_dict:
    #         s_dict[c] -= 1
    #     else:
    #         return False
    
    # for count in s_dict.values():
    #     if count != 0:
    #         return False

    # return True 

    # countS = {}

    # for c in s:
    #     countS[c] = 1 + countS.get(c, 0)
    # return countS # {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
    # Both also work
    # for i in range(len(s)):
    #     countS[s[i]] = 1 + countS.get(s[i], 0)
    # # return countS # {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
    
    # for c in t:
    #     if c in countS:
    #         countS[c] -= 1
    #     else:
    #         return False
    
    # for count in countS.values():
    #     if count != 0:
    #         return False
    # return True



print(isAnagram("anagram", "nagaram")) # True
print(isAnagram("rat", "car")) # False
print(isAnagram("lol", "oll")) # True
print(isAnagram("aacc", "ccac")) # Flase
