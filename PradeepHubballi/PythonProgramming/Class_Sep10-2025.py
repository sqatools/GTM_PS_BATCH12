str1="very good Morning Learning Python"
output={}
Word_list = str1.split(" ")
print(Word_list)
for word in Word_list:
    print(word,":",word[0])
    first_char=word[0]
    last_char=word[-1]
    output[f"{first_char},{last_char}"]= word

print("output:",output)