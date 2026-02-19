def are_anagrams(str1, str2):
   
    if len(str1) != len(str2):
        return False
    
    
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  
print(are_anagrams("hello", "world"))