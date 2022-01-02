with open("file.txt", "w+") as file:
    file.write("hello\n")
    file.write("hello\n")

print(file.mode)

with open("file.txt", "r") as file:
    content = file.read()
    print(content)

    print('read line')
    file.seek(0)
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline())

'''
w+
a+
r
'''

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

print(os.name)
print(path.exists("file.txt"))
print(path.isfile("file.txt"))
print(path.isdir("file.txt"))
print(path.realpath("file.txt"))
print(path.split(path.realpath("file.txt")))

t = time.ctime(path.getmtime("file.txt"))
print(t)
print(datetime.datetime.fromtimestamp(path.getmtime("file.txt")))

# modified time
td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("file.txt"))
print(td)
print(td.total_seconds())

import shutil

# copy file
src = "file.txt"
dest = "file_back.txt"
shutil.copy(src, dest)

# rename file
old = "file.txt"
new = "new_file.txt"
os.rename(old, new)

# create archive
from shutil import make_archive

root_dir, tail = path.split(path.realpath("file.txt"))
make_archive("archive", "zip", root_dir)

# adding specific file to archive
from zipfile import ZipFile

with ZipFile("test.zip", "w") as newzip:
    newzip.write("file.txt")
    newzip.write("textfile.txt.bak")
