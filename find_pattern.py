#!/usr/bin/env python2
import os, re
import fnmatch
import matplotlib.pyplot as plt

dir_name    = []
num_of_file = []
found_file  = []
dict_name   = {}

search_option = ""
root_dir = ""
Pattern = ""

"""
Program name: os_walk.py
Input parameters:
     1.  'p' searching the pattern in all sub-dir files.
         'f' searching the file name with the pattern in all sub-dir.
     2.  Pattern to search.
     3.  Root directory to search.

# Asked user to enter the search for the file name or pattern in all directory tree
# Count number of files that contain key_word in each subdir
# All results should be saved in a key:value array with key being subdir string
# value being counts of file containing "key word" in this sub dir

"""

def init_array(dir_name, num_of_file):
    '''Create a dictionary with all sub-dirs that are the keys.
          used an emty list to get all sub-dirs names for the list.
          used set to eliminate all duplicated elements in the list.
       Initial all keys in the dict with 0.
          walked thru all elements in the list to create a dict with initial 0.
    '''
    print(root_dir, dir_name, dict_name)
    for rootdir, subdirs, filenames in os.walk(root_dir):
        if subdirs:
            for x in subdirs:
                d_name = os.path.join(rootdir, x)
                dir_name.append(d_name)
                num_of_file.append(0)
    dir_name = list(set(dir_name))
    for i in range(len(dir_name)):
        dict_name[dir_name[i]] = num_of_file[i]

    print("\nInitialize all key dictionary with 0")
    print(dict_name)


def find_file_name_with_ext():
    '''Find the file name with the specific extension
    '''
    for rootdir, subdirs, filenames in os.walk(root_dir):
        for x in filenames:
            if x.endswith("uts_*") == True:
                found_file.append[x]
    print(found_file)


def find_file_name_with_pattern():
    '''Find the file names in the tree that have the file name's pattern.
       Count the file names that have the matched pattern.
       Save the number of the matched file names in keys:value.
    '''
    for rootdir, subdirs, filenames in os.walk(root_dir):
        file_match = 0
        print("============================================================")
        for x in fnmatch.filter(filenames, pattern):
            found_file.append(os.path.join(rootdir,x))
            file_match += 1
            print(x)
            print(file_match)
        print(rootdir)
        dict_name[rootdir] = file_match
        print("This %s has %s files matched" %(rootdir, dict_name[rootdir]))


def find_pattern(file_name, pattern):
    '''Open a file and search for the pattern
       Return True if the pattern matched
       Encoding difference between 2 and 3 on python
    '''
    with open(file_name, 'r') as fObj:
        match = False
        for line in fObj:
            if match :
                return True
            for match in re.finditer(pattern, line):
                print("Found %s: ---->>> %s" %(file_name, match.group()))
                match = True

def find_file_name_has_pattern():
    '''Find the file names in the tree that have the pattern.
       Count the number of files that have the matched pattern.
       Save the number of files in keys:value.
    '''
    for rootdir, subdirs, filenames in os.walk(root_dir):
        if filenames:
            file_match = 0
            print("============================================================")
            for file in filenames:
                file_name = os.path.join(rootdir, file)
                print("Check file >>> %s: " %file_name)
                if find_pattern(file_name, pattern):
                   file_match += 1
                   print(file_match)

            print(rootdir)
            dict_name[rootdir] = file_match
            print("This %s has %s files matched" %(rootdir, dict_name[rootdir]))


if __name__ == "__main__":

    search_option = raw_input("\nPlease enter 'f' to search for file name or 'p' for pattern: ")
    root_dir = raw_input("\nPlease enter the root directory that you like to search. Ex '/mnt/c/Users/Owner/NUX':  ")
    pattern  = raw_input("\nPlease enter the key_word that you like to search. Ex: '^[a-zA-Z+_TESTResult.*':  ")

    # root_dir = "/mnt/c/Users/Owner/NUX/bin"
    # pattern = ("result")

    init_array(dir_name, num_of_file)

    if str(search_option) == 'p':
        find_file_name_has_pattern()
    elif str(search_option) == 'f':
        find_file_name_with_pattern()
    else:
        print("\nThe search option should be 'p' for pattern or 'f' for file name. You entered: %s " %search_option)
        print("\nPython 2 required the quote between the input string")
        exit
    
    print("\nThe result is stored in the dictionary with the keys are sub-dirs and the values are the number of files/patterns found")
    print(dict_name)

    The Plot requires the matplotlib installed.
 
    plt.xlabel('Directory Name')
    plt.ylabel('Num of matched file')

    plt.title('Graph of directory with match files')
    plt.plot(*zip(*sorted(dict_name.items())))
    plt.show()
