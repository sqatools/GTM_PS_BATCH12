#Q1 write a python program to read two files data and store in third file.

def append_2_files_data_3rd_file(file1, file2, file3):
    # read file1 data
    with open(file1, "r") as abc:
        file1_data = abc.read()

    # read file2 data
    with open(file2, "r") as pqr:
        file2_data = pqr.read()

    # Append file1 and file2 data into third file.
    with open(file3, "a") as xyz:
        xyz.write(file1_data)
        xyz.write(file2_data)


#append_2_files_data_3rd_file("file1.txt", "file2.txt", "file3.txt")

#Q1 write a python program to read two files data and store in third file with alternate lines
# from file1 and file2



def append_2_files_data_3rd_file_alternatively(file1, file2, file3):
    # read file1 list of lines
    with open(file1, "r") as abc:
        file1_list = abc.readlines()

    # read file2 list of lines
    with open(file2, "r") as pqr:
        file2_list = pqr.readlines()

    with open(file3, "a") as xyz:
        for i in range(len(file1_list)):
            xyz.write(file1_list[i])
            xyz.write(file2_list[i])


#append_2_files_data_3rd_file_alternatively("file1.txt", "file2.txt", "file3_alternate.txt")


#Q3. write python program to replace specific word from target word.

def replace_word(file_path, word1, word2):
    with open(file_path, "r")as file:
        file_data = file.read()

    # replace word1 with word2 in existing content
    updated_data = file_data.replace(word1, word2)

    # overwrite updated content  to the file
    with open(file_path, "w") as file:
        file.write(updated_data)


replace_word("read_data.txt", "PYTHON", "JAVA")




