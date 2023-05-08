# Name: Prem Atul Jethwa
# Stud ID: 1001861810
# Language: Python 3 version 3.10.8
# OS: Mac OS (Python 3 not compatible on Omega)

import os       # os module to get the size of the file

# Path of the folder whose size is to be determine


def get_size(p):
    size = 0        # initialize size variable as 0
    with os.scandir(p) as i:
        for file in i:      # recursion to get the size of all file inside the folder
            if file.is_file():      # check if the iterated file is file or a directory
                # add the size of that file to the initialize variable
                size += file.stat().st_size
            elif file.is_dir():
                size += get_size(file.path)
    return size


# printing the size of the folder
print(get_size(p='.'))

##### ...Try Python 2 code to run on Omega...######
# Path of the folder whose size is to be determine
# def get_size(p):
#    Size = 0        # initialize size variable as 0
#    i = os.listdir(p)
#    for file in i:      # recursion to get the size of all file inside the folder
#        if os.path.isfile(file):  # check if the iterated file is file or a directory
# add the size of that file to the initialize variable
#            Size = os.path.getsize(file)
#        else:
#            Size += get_size(file.path)
#    return Size


# printing the size of the folder
# print(get_size(p='.'))

# Name:- Prem Atul Jethwa
# Sutdent ID:- 1001861810

# ####################################.Lab01 Question and Answer.####################################

# 1) Was one language easier or faster to write the code for this? If so, describe in detail why, as in what about
# the language made that the case.
# -> According to me, Python is the most convenient language to develop for this code.
# -> Python syntax is much more easier to grasp, and there are no need of references to be considered.
# -> Python is a very simple and easy to understand programming language.
# -> It was a easy to write a code in Python as we don't have to deal with pointers like we used in C.


# 2) Even though a language may not (e.g. FORTRAN) does not support recursion, describe how you could write
# a program to produce the same results without using recursion. Would that approach have any limitations and if
# so, what would they be?
# -> One may develop a software that calls a function manually for each route.
# -> The constraint is that you must be aware of the path and the number of files included inside it.
# -> If another user adds a file, you must manually add a function call to that file.
# Limitations:
# -> This is time-consuming and must be updated everytime the files are changed.
# -> Because we're saving all the file/directory paths, program's space complexity will be rather high.
