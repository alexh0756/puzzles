def ransom(ransomNote, magazine):
    
    chars = {}
    for char in magazine:
        if char not in chars: 
            chars[char] = 1
        else: 
            chars[char] += 1

    for char in ransomNote:
        if char in chars and chars[char] > 0: 
            chars[char] -= 1
        else: 
            return False
    
    return True

print(ransom(ransomNote = "a", magazine = "b"))
print(ransom(ransomNote = "aa", magazine = "ab"))
print(ransom(ransomNote = "aa", magazine = "aab"))