numbers = list(range(1,101))

result = [n for n in numbers if n % 2 ==0 and n % 3== 0 and  n % 5==0]

print("Number divisible by  2, 3 and 5 from 1 to 100 are:",)
print(result)

#####################################################################

str1="We aRe LeArNing PytHon PrograMming"

result = "".join([ch for ch in str1 if ch.isupper()])

print(result)
# WRLANPHPM




