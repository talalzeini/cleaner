import os
import shutil
import compress as cs
from constants import *

def test_folder_existence(folder_path, number):
    if cs.is_existing(folder_path):
        print("Test " + str(number) + ": Passed\n")
    else:
        print("Test " + str(number) + ": Failed\n")

def test_folder_emptiness(folder_path, number):
    list_of_files = find_files_in(folder_path)
    if len(list_of_files) == 0:
        print("Test " + str(number) + ": Passed\n")
    else:
        print("Test " + str(number) + ": Failed\n")

def validate_setup(folder_path, original_folders, number):
    folders = list_all_real_folders(folder_path)
    for folder in folders:
        if folder not in original_folders:
            print("Test " + str(number) + ": Failed\n")
            return
    print("Test " + str(number) + ": Passed\n")

def check_capitalization(folder_path, number):
    folders = list_all_real_folders(folder_path)
    for folder in folders:
        folder_name = folder.split("/")[-1]
        if folder_name[0].islower():
            print("Test " + str(number) + ": Failed\n")
            return
    print("Test " + str(number) + ": Passed\n")



def run_tests():
    print("\n\n")
    print("Test 1: Checking if 'Developer' folder still exists")
    test_folder_existence(developer, 1)

    print("Test 2: Checking if 'Focus' folder still exists")
    test_folder_existence(desktop_folders[0], 2)
    print("Test 3: Checking if 'SJSU Focus' folder still exists")
    test_folder_existence(desktop_folders[1], 3)
    print("Test 4: Checking if 'LeetCode Focus' folder still exists")
    test_folder_existence(desktop_folders[2], 4)
    print("Test 5: Checking if there's any files in the root directory")
    test_folder_emptiness(root, 5)
    print("Test 6: Checking if there's any files in the Documents folder")
    test_folder_emptiness(documents, 6)
    print("Test 7: Checking if there's any files in the Downloads folder")
    test_folder_emptiness(downloads, 7)
    print("Test 8: Checking if there's any junk folders in the root folder")
    validate_setup(root, root_folders, 8)
    print("Test 9: Checking if there's any junk folders in the 'Documents' folder")
    validate_setup(documents, documents_folders, 9)
    print("Test 10: Checking if there's any junk folders in the 'Downloads' folder")
    validate_setup(downloads, downloads_folders, 10)
    print("Test 11: Checking if all junk folders are capitalized")
    check_capitalization(junk_folders, 11)
    print("Test 12: Checking if all junk files are capitalized")
    check_capitalization(junk_files, 12)
    print("Test 13: Checking if there's any files in the junk folders")
    test_folder_emptiness(junk_folders, 13)

def find_files_in(path):
    files = []
    directory = os.listdir(path)
    for content in directory:
        isFile = os.path.isfile(path + "/" + content)
        if(isFile and content not in virtual_files and content[0] != "."):
            files.append(path + "/" + content)
    return files

def create_new(file_name, file_extension): 
    new_file_name = ''.join([i for i in file_name if not i.isdigit()])
    new_file_name = new_file_name.replace(" ", "") + cs.random_string(5) + file_extension
    new_file_name = new_file_name.lower()
    return new_file_name.capitalize()



def find_type_of_file(file_extension):
    for index, extension_group in enumerate(downloads_extensions_unmerged):
        if file_extension in extension_group:
            return index

def move_files_in(source):
    files = find_files_in(source) # returns a list of paths to files

    for file_path in files:
        file = cs.get_file(file_path)
        file_full_name = file[0]                                # example.txt
        file_extension = file[1]                                # .txt
        if "." in file_full_name:
            file_name = file_full_name.split(file_extension)  # example
        else:
            file_name = file_full_name
        file_location = source + "/"                            # /Users/talalzeini/
        file_extension_folder = file_extension[1:].upper()      # TXT

        new_file_name = create_new(file_name, file_extension)
        new_file_path = file_location + new_file_name
        os.rename(file_path, new_file_path)

        if file_extension in downloads_extensions:
            type = find_type_of_file(file_extension)
            destination = (downloads_paths[type] + "/" + file_extension_folder)
            if not cs.is_existing(destination):
                os.makedirs(destination)
            shutil.move(new_file_path, destination + "/" + new_file_name)
        else:
            destination = junk_files
            if not cs.is_existing(destination):
                os.makedirs(destination)
            shutil.move(new_file_path, destination + "/" + new_file_name)

def list_all_real_folders(folder):
    final_list = []
    folders = cs.list_directories(folder)
    for folder in folders:
        folder_name = folder.split("/")[-1]
        if(folder_name[0] != "."):
            final_list.append(folder)
    return final_list

# returns a list of paths to folders
def list_folders_to_move(folder_path, original_folders):
    folders_to_move = []
    lst = list_all_real_folders(folder_path)
    for folder in lst:
        if (folder not in original_folders) and (automater_of_this not in folder) and ("." not in folder):
            folders_to_move.append(folder)
    return folders_to_move

root_folders_to_move = list_folders_to_move(root, root_folders)
desktop_folders_to_move = list_folders_to_move(desktop, desktop_folders)
documents_folders_to_move = list_folders_to_move(documents, documents_folders)
downloads_folders_to_move = list_folders_to_move(downloads, downloads_folders)

def move_folders_in(folders):
    for folder in folders:
        folder_name = folder.split("/")[-1]
        folder_location = folder.split(folder_name)[0]
        new_folder_name = create_new(folder_name, "")
        new_folder_path = folder_location + new_folder_name
        os.rename(folder, new_folder_path)
        if not cs.is_existing(junk_folders):
            os.makedirs(junk_folders)
        shutil.move(new_folder_path, junk_folders)

def move_folders():
    move_folders_in(root_folders_to_move)
    move_folders_in(desktop_folders_to_move)
    move_folders_in(documents_folders_to_move)
    move_folders_in(downloads_folders_to_move)

def move_files():
    move_files_in(root)
    move_files_in(downloads)
    move_files_in(desktop)
    move_files_in(documents) 

def start():
    move_folders()
    move_files()
    run_tests()

start()