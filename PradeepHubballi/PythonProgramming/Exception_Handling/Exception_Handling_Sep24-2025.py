

def exception_handling (n1,n2):
    try :
        add = n1+n2
        print("addition of values :",add)
    except Exception as e:
        print(e)
        print("can not add integer with string")

#exception_handling(40,1000)
#print("good morning")

#####################Raise exception explicity ############################################################


def exception_handling (n1,n2):
    try :
        add = n1+n2
        print("addition of values :",add)
    except Exception as e:
        print(e)
        print("can not add integer with string")
        raise





exception_handling(40,100)
print("good morning")

