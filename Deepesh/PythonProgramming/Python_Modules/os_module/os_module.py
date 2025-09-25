import os
import shutil

# get current work directory path
print("current path :", os.getcwd())
# E:\Trainings\GTM_PS_Batch12_July25\GTM_PS_BATCH12\Deepesh\PythonProgramming\Python_Modules\os_module

# create directory in specified path
# os.mkdir("folder1")  # create folder in current directory

#os.mkdir(r"E:\Filesdata\Batch12")  # create folder on specific path

# create a folder tree
#os.makedirs(r"E:\Filesdata\Batch12\f1\f2\f3\f4\f5")


################################  Remove Folder ##########

#os.rmdir("folder1")  # remove from current location
#os.removedirs(r"E:\Filesdata\Batch12\f1\f2\f3\f4\f5")  # remove complete folder tree

##################### GET LIST OF FILES AND FOLDERS ################

# get list of files and folder
folder_data = os.listdir(r"E:\Filesdata")
print("Total Files and folder :", len(folder_data))
for data in folder_data:
    print(data)

print("_"*50)
######################## PATH OPERATION ###############
# check path or not

print(os.path.exists(r"E:\Filesdata\Batch12\count_name.txt")) # True
print(os.path.exists(r"E:\Filesdata\Batch13\count_name.txt")) # False

# Check given path is file or folder
print("check path is file :", os.path.isfile(r"E:\Filesdata\Batch12\count_name.txt"))  # True
print("check path is file :", os.path.isfile(r"E:\Filesdata\Batch12")) # False
print("check path is folder :", os.path.isdir(r"E:\Filesdata\Batch12"))  # True

# JOIN TWO PATH:

src1 = r"E:\Filesdata\Batch12"
file_name = "count_name.txt"
file_path = os.path.join(src1, file_name)
print("File Path :", file_path)  # E:\Filesdata\Batch12\count_name.txt



print("_"*50)
######################################
# write a python script to get list of files and folder.
src_path = r"E:\Filesdata"
folder_data = os.listdir(src_path)
print("Total Files and folder :", len(folder_data))
# create files_list and folder_list empty list
files_list = []
folder_list = []
# Loop through each data of file.
for data in folder_data:
    data_path = os.path.join(src_path, data)
    if os.path.isfile(data_path):
        files_list.append(data)
    elif os.path.isdir(data_path):
        folder_list.append(data)


print("Files List :", len(files_list), files_list) # 40
print("Folder list :", len(folder_list), folder_list) # 23

print("_"*50)
################################################################

file_path = r"E:\Filesdata\test_data.xlsx"
tar_path = r"E:\Filesdata\Batch12\test_data.xlsx"
tar_path2 = r"E:\Filesdata\Batch12\test_data_updated.xlsx"

# copy file with same name
shutil.copy(file_path, tar_path)
# copy file with different name
shutil.copy(file_path, tar_path2)