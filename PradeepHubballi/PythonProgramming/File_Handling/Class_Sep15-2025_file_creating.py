def read_file_with_context_manager(filepath):
    with open(filepath,"r") as file:
        data = file.read()
        print(data)
        print("close status inside context manager:",file.closed)
    print("close status outside  context manager:", file.closed)

read_file_with_context_manager("Data_Read.txt")
