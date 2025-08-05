# python data types
# 1.Number
#   *Integer
#   *Float
#   *complex number
# 2.Sequential
#   *String
#   *list
#   *Tuple
# 3.Dictionary
# 4.Set
# 5.Boolean

# * Integer properties:
# / Integer data type if immutable data types
# / there is no limit for integers data types
# / Integer only contains whole numbers both +ve and -ve

var1=0
var2=123
var3=987456799456
var4=-4534
print(var1, type(var1))
# 0 <class 'int'>
print(var2, type(var2))
# 123 <class 'int'>
print(var3, type(var3))
# 987456799456 <class 'int'>
print(var4, type(var4))
# -4534 <class 'int'>

print("_"*50)
# *Float properties
# / Float data type if immutable data types
# / there is no limit for float data types
# / Float only contains pointer numbers both +ve and -ve

f1=0.0
f2=0.34
f3=7894.56123
f4=-582369
print("f1:", f1, type(f1))
# f1: 0.0 <class 'float'>
print("_"*50)
print("f2:", f2, type(f2))
# f2: 0.34 <class 'float'>
print("_"*50)
print(f3, type(f3))
# 7894.56123 <class 'float'>
print("f3:", f3, type(f3))
# f3: 7894.56123 <class 'float'>
print("_"*50)
print("f4:", f4, type(f4))
# f4: -582369 <class 'int'>

print("_"*50)
# * Complex numbers properties
# / comples is immutable data types
# / complex data type if combination of 2values real and imaginary
#    eg: x+yj, x=real y=imaginary
# / complex data can +ve and -ve both
p1=10+20j
print(p1,type(p1))
# (10+20j) <class 'complex'>
print("real value:", p1.real)
# real value: 10.0
print("imaginary value:", p1.imag)
# imaginary value: 20.0
print("_"*50)
p2=-50-40j
print(p2, type(p2))
# (-50-40j) <class 'complex'>

add_complex_number=p1+p2
print(add_complex_number)
# (-40-20j)