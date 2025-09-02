s3 = "Hello, good morning, how are you doing"
vowels = "aeiou"
vowels_count = 0
for char in s3:
    if char in vowels:
        vowels_count = vowels_count + 1
    else:
        continue

print("all vowels:", vowels_count)

