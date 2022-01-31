import os
from os import path
from pprint import pprint

dirs = os.listdir("/home/suril/Training/code/python-cheatsheet/test")
print(dir)

dirs_and_files = os.walk("/home/suril/Training/code/python-cheatsheet/test")
pprint(list(dirs_and_files))

files = []
byte_size = 0
for cur_path, folder_list, file_list in os.walk("/home/suril/Training/code/python-cheatsheet/test"):
    files.extend(file_list)

    for file in file_list:
        byte_size += path.getsize(path.join(cur_path, file))

print(files)
print(byte_size)



with open("result.txt", "w+") as file:
    file.write(f"Total bytecount: {byte_size}\n")
    file.write(f"Files list:\n")
    file.write('-' * 10 + '\n')
    for item in files:
        file.write(item)
        file.write('\n')

