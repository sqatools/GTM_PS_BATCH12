#anagram


s1="python"
s2="yonthp"
anagram = True
for char in s1:
    print(char)

    if char in s2:
        continue
    else:
        anagram=False
        break

if anagram==True and len(s1) == len(s2):
    print("these string is anagram: ", s1, s2)
else:
    print("these strings are not anagram:", s1, s2)