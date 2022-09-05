#!/usr/local/bin/python
import os
import shutil
import random
import string
from time import sleep
from os import scandir, rename
import logging
import sys

main_user_folders = ["/Users/talalzeini/Music",
"/Users/talalzeini/Pictures",
"/Users/talalzeini/Desktop",
"/Users/talalzeini/Library",
"/Users/talalzeini/Public",
"/Users/talalzeini/Movies",
"/Users/talalzeini/Documents",
"/Users/talalzeini/Downloads"]
main_desktop_folders = ["SJSU Focus", "Development", "LeetCode"]
automater_of_this = "Manage.app"
virtual_files = [".DS_Store", ".localized"]

main = "/Users/talalzeini"
downloads = "/Users/talalzeini/Downloads"
desktop = "/Users/talalzeini/Desktop"
documents = "/Users/talalzeini/Documents"

pdf_path = "/Users/talalzeini/Documents/PDF"
doc_path = "/Users/talalzeini/Documents/DOC"
docx_path = "/Users/talalzeini/Documents/DOCX"

music_path = "/Users/talalzeini/Downloads/Music"
videos_path = "/Users/talalzeini/Downloads/Videos"
images_path = "/Users/talalzeini/Downloads/Images"
documents_path = "/Users/talalzeini/Downloads/Documents"
programming_path = "/Users/talalzeini/Downloads/Programming"
installers_path = "/Users/talalzeini/Downloads/Installers"
text_path = "/Users/talalzeini/Downloads/Text"

junk = "/Users/talalzeini/Downloads/Junk"
trash = "/Users/talalzeini/.Trash"

# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# ? supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# ? supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
programming_extensions = [".py", ".cpp", ".c",
                       ".html", ".css", ".js", ".java"]
installer_extensions = [".dmg"]
text_extensions = [".txt", ".rtf"]

downloads_extensions = [image_extensions, video_extensions, audio_extensions, document_extensions, programming_extensions, installer_extensions, text_extensions]
downloads_paths = [images_path, videos_path, music_path, documents_path, programming_path, installers_path, text_path]
file_prefix = ["IMG", "VID", "MUS", "DOC", "PRO", "INST", "TXT"]

def random_integer(n):
    characters = string.digits
    password = ''.join(random.choice(characters) for i in range(n))
    return password

def new_name(index):
    return str(file_prefix[index]) + "_" + random_integer(10)

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

all_user_folders = listdirs(main)

main_folders_to_move = []
def get_junk_folders():
    for folder in all_user_folders:
        if folder not in main_user_folders and "." not in folder:
            main_folders_to_move.append(folder)
    return main_folders_to_move

def list_desktop_folders():
    folders_to_move = []
    lst = listdirs(desktop)
    for folder in lst:
        excluded_folders = folder.split(str(desktop) + "/")[1] 
        if (excluded_folders not in main_desktop_folders) and (excluded_folders != automater_of_this):
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
move_file(main)
move_file(downloads)
move_file(desktop)
move_file(documents) 
empty_trash()