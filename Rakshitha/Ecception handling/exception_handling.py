def exception_handling(n1, n2):
    try:
        add = n1+n2
        print("addition of values:",add)
    except Exception as e:
        print(e)
        print("can not add integer with string")

exception_handling(40, "hello")
# unsupported operand type(s) for +: 'int' and 'str'
# can not add integer with string
print("good morning")  #good morning