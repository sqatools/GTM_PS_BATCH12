"""
1. Read mode(r) :
2. Write mode (w):
3. Append mode (a):
"""

def read_text_file(file_path):
    # open file and get IO object
    file = open(file_path, "r")
    # use read method to read data
    data = file.read()
    # print file data
    print(data)
    # print file name
    print("filename :", file.name)  # filename : read_data.txt
    print("close status before closing file:", file.closed)  # close status : False
    file.close()
    print("close status after close :", file.closed)
    # close status after close : True

# read file from current location
#read_text_file("read_data.txt")

# read file from specific path
#read_text_file(r"E:\Filesdata\count_name.txt")

# read file which is not available
# read_text_file(r"E:\Filesdata\count_name1.txt")
# FileNotFoundError: [Errno 2] No such file or directory: 'E:\\Filesdata\\count_name1.txt'





########################## Write  content to the file ####################


def write_text_to_file(file_path, content):
    # open file and get IO object with write mode
    file = open(file_path, "w")
    # use write method to write data
    file.write(content)
    # print file data
    file.close()


file_content = """
1.  Welcome to python learning
2.  We will learn Python in easy way.
3.  Good Morning
"""

# 1.  Add content to non-existing file : It will create file and add content to the file.
#write_text_to_file("write_content.txt", file_content)


#2 . Add content to existing file : If file is already exist, it will overwrite the existing content
# of the file.
write_text_to_file("write_data2.txt", "Good Morning")

########################## append content to the file ##############

def append_text_to_file(file_path, content):
    # open file and get IO object with append mode
    file = open(file_path, "a")
    # use write method to write data
    file.write(content)
    # print file data
    file.close()

# 1. append content to non-existing file : It will create file and add content to file at the
# end of file lines.
# msg = "Its fun learning Programming fundamentals\n"
# append_text_to_file("append_data.txt", msg)


# 2. append content to existing file : It will data content to file at the
# end of file lines.
msg = "Its fun learning Programming fundamentals\n"
append_text_to_file("append_data.txt", msg)

print("_"*50)
#########################################################
# context manage : Context has its own enter and existing method internally, once the file
# is open in context manager, then no need to close file explicitly. Once user move output
# of the context of context manager, then will auto close the file.

def read_file_with_context_manager(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        print(data)
        print("close status inside context manager :", file.closed)
    print("close status outside context manager :", file.closed)


read_file_with_context_manager("read_data.txt")



