def exception_handling(n1, n2):
    try:
        add = n1 + n2
        print("add:", add)
    except Exception as e:
        print(e)
        print("cannot add integer with string")
    else:
        print("code execution is successful")


exception_handling(40, 'python')

print("_" *50)

def exception_hand(n1, n2):
    try:
        add = n1+n2
        print("add:", add)
    except Exception as e:
        print(e)
        print("cannot add integer")
