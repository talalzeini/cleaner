#!/usr/local/bin/python
import os
import shutil
import random
import string
from time import sleep
from os import scandir, rename
import logging
import sys
from constants import *


def random_integer(n):
    characters = string.digits
    password = ''.join(random.choice(characters) for i in range(n))
    return password

def new_name(index):
    return str(files_prefixes[index]) + "_" + random_integer(10)

def new_folder_name():
    return "FOLDER" + "_" + random_integer(10)

def find_files_in(path):
    files = []
    directory = os.listdir(path)
    for content in directory:
        isFile = os.path.isfile(path + "/" + content)
        if(isFile and content not in virtual_files):
            files.append(path + "/" + content)
    return files

def get_file(path):
    split_path = os.path.splitext(path)
    file_name = path.split("/")[-1]
    file_extension = split_path[1]
    return [file_name, file_extension]

def folder_existence(path):
    existing = os.path.exists(path)
    return existing

def move_file(source):
    source_files = find_files_in(source)
    for file_full_path in source_files:
        f = get_file(file_full_path)
        file_location = file_full_path.split(f[0])[0]
        file_extension = f[1]
        for index, array in enumerate(range(len(downloads_extensions))):
            if(file_extension in downloads_extensions[array]):
                destination = (downloads_paths[index])
                new_file_name = new_name(index) + file_extension
                new_file_path = file_location + new_file_name
                os.rename(file_full_path, new_file_path)
                if not folder_existence(destination):
                    os.makedirs(destination)
                shutil.move(new_file_path, destination + "/" + new_file_name)

def empty_trash():
    os.chdir(trash)
    if len(sys.argv) >= 2:
        if sys.argv[1] == '-t' or sys.argv[1] == '-T':
            os.system("tree ./")
        elif sys.argv[1] == '-l' or sys.argv[1] == '-L':
            os.system("ls -al")
        else:
            print("Nothing in the bin to delete")
    os.system("rm -rf *")


def listdirs(folder):
    return [
        d for d in (os.path.join(folder, d1) for d1 in os.listdir(folder))
        if os.path.isdir(d)
    ]

all_user_folders = listdirs(root)

main_folders_to_move = []
def get_junk_folders():
    for folder in all_user_folders:
        if folder not in root_folders and "." not in folder:
            main_folders_to_move.append(folder)
    return main_folders_to_move

def list_desktop_folders():
    folders_to_move = []
    lst = listdirs(desktop)
    for folder in lst:
        # making sure ["SJSU Focus", "Focus", "LeetCode"] are not removed
        if (folder not in desktop_folders) and (automater_of_this not in folder):
            folders_to_move.append(folder)
    return folders_to_move

desktop_folders_to_move = list_desktop_folders()
main_junk_folders = get_junk_folders()

def move_folder(folders):
    for folder in folders:
        new_folder = new_folder_name()
        os.rename(folder, new_folder)
        shutil.move(new_folder, documents)

move_folder(desktop_folders_to_move)
move_folder(main_junk_folders)
move_file(root)
move_file(downloads)
move_file(desktop)
move_file(documents) 
empty_trash()