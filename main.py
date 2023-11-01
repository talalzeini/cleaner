import os
import shutil
import os.path
from subprocess import call
from constants import *
from tests import *
from string import ascii_lowercase
from random import choices
from helpers import list_files, list_visible_folders, create_new_name, write_list_to_file

number_of_renamed_files = 0
number_of_renamed_folders = 0
number_of_moved_files = 0
number_of_moved_folders = 0

def create_directories(essential_folders):
    for folder in essential_folders:
        if not is_existing(folder):
            os.makedirs(folder)

def find_type_of_file(file_extension):
    for index, extension_group in enumerate(downloads_extensions_unmerged):
        if file_extension in extension_group:
            return index

def move_files(source):
    """
    Moves files from the source folder to the appropriate destination folder.

    Args:
        source (str): The path to the source folder.

    Returns:
        None
    """

    global number_of_renamed_files
    global number_of_moved_files

    files = list_files(source)  # Get a list of paths to files

    for file_path in files:
        # Get file info
        file_name, file_extension = os.path.splitext(file_path)
        file_name = os.path.basename(file_name)
        file_location = source + "/"
        file_extension_folder = file_extension[1:].upper()

        # Create new file name
        new_file_name = create_new_name(file_name, file_extension)
        new_file_path = os.path.join(file_location, new_file_name)

        # Rename the file only if the new file name has changed
        if file_path != new_file_path:
            os.rename(file_path, new_file_path)
            number_of_renamed_files += 1

        if file_extension in downloads_extensions:
            # Move to the corresponding downloads folder
            file_extension_index = find_type_of_file(file_extension)
            destination = os.path.join(downloads_paths[file_extension_index], file_extension_folder)
        else:
            # Move to the archived files folder
            destination = archived_files

        # Create the destination folder if it doesn't exist
        if not is_existing(destination):
            os.makedirs(destination)

        # Move the file to the destination folder
        shutil.move(new_file_path, os.path.join(destination, new_file_name))
        number_of_moved_files += 1

# returns a list of paths to folders
def list_folders_to_move(folder_path, original_folders):
    folders_to_move = []
    lst = list_visible_folders(folder_path)
    for folder in lst:
        if (
            (folder not in original_folders)
            and (cleaner not in folder)
            and ("." not in folder)
        ):
            folders_to_move.append(folder)
    return folders_to_move

def print_updates():
    global number_of_moved_folders
    global number_of_renamed_folders
    global number_of_moved_files
    global number_of_renamed_files

    response = ""
    changes = number_of_renamed_files + number_of_renamed_folders + number_of_moved_files + number_of_moved_folders
    if(number_of_renamed_files > 0):
        response += ("Renamed " + str(number_of_renamed_files) + " files\n")
    if(number_of_renamed_folders > 0):
        response += ("Renamed " + str(number_of_renamed_folders) + " folders\n")
    if(number_of_moved_files > 0):
        response += ("Moved " + str(number_of_moved_files) + " files\n")
    if(number_of_moved_folders > 0):
        response += ("Moved " + str(number_of_moved_folders) + " folders\n")
    if(changes == 0):
        response = "No changes made"
    else:
        response += ("Changes made: " + str(changes) + "\n")
    return response

def display_results():
    results = run_tests()
    if results == 0:
        print(print_updates())
    elif results == 1:
        print("1 failure found")
    else:
        print(str(results) + " failures found")

def close_all_finder_windows():
    """
    Closes all open Finder windows.
    
    Args:
        None

    Returns:
        None
    """
    call(["osascript", "-e", close_finder_windows_string])

def organize_screenshots():
    screenshot_paths = list_files(screenshots_directory)
    for screenshot_path in screenshot_paths:
        screenshot_name = os.path.basename(screenshot_path)
        if screenshot_name.startswith("SS "):
            screenshot_date_string = screenshot_name.split(" at ")[0][3:]  # Remove "SS " prefix
            screenshot_date = datetime.strptime(screenshot_date_string, "%Y-%m-%d")
            folder_name = screenshot_date.strftime("%m-%Y")
            destination_folder = os.path.join(screenshots_directory, folder_name)
            
            if not is_existing(destination_folder):
                os.makedirs(destination_folder, exist_ok=True)
            
            shutil.move(screenshot_path, os.path.join(destination_folder, screenshot_name))

root_structure = [(root, root_folders), (desktop, desktop_folders), (documents, documents_folders), (downloads, downloads_folders), (developer, developer_folders), (icloud_drive, icloud_drive_folders)]

def move_folders(folders):
    for folder in folders:
        folder_name = folder.split("/")[-1]
        folder_location = folder.split(folder_name)[0]
        new_folder_name = create_new_name(folder_name, "")
        if new_folder_name == ".":
            new_folder_name = folder_name
        new_folder_path = folder_location + new_folder_name
        if not is_existing(archived_folders):
            os.makedirs(archived_folders)

        if os.path.exists(new_folder_path):
            # Folder already exists in the destination directory,
            random_chars = ''.join(choices(ascii_lowercase, k=3))
            new_folder_path = os.path.join(folder_location, new_folder_name + random_chars)

        os.rename(folder, new_folder_path)
        shutil.move(new_folder_path, archived_folders)

def organize_essential_folder(path, fixed_folders):
    move_files(path)
    folders_to_move = list_folders_to_move(path, fixed_folders)
    move_folders(folders_to_move)

def organize_finder():
    for path, fixed_folders in root_structure:
        organize_essential_folder(path, fixed_folders)

def update_apps():
    write_list_to_file(system_applications_file, system_apps)
    write_list_to_file(downloaded_applications_file, downloaded_apps)

def start():
    organize_screenshots()
    create_directories(essential_folders)
    organize_finder()
    update_apps()
    display_results()
    close_all_finder_windows()

start()