def read_file_write_contex_manager(filepath, ):
    with open(filepath, "r") as file:
        data + file.read()
        print(data)
        print("close status inside contex manager :", file.close)
    print("close status outside contex manager:",)