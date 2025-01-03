import os, getpass
from tcompress import list_directories

def get_root_username():
    return str(getpass.getuser())

def replace_username(dictionary):
    username = get_root_username()
    for key, value in dictionary.items():
        if type(value) != list:
            value = value.replace("{username}", username)
            dictionary[key] = value
        else:
            for i in range(len(value)):
                value[i] = value[i].replace("{username}", username)
                dictionary[key] = value

def list_files(folder_path):
    """
    Lists and returns a list of file paths within a given directory path.
    
    Args:
        path (str): The path to the directory.

    Returns:
        list: A list of file paths within the given directory path.
    """
    files = []
    directory = os.listdir(folder_path)
    for content in directory:
        isFile = os.path.isfile(folder_path + "/" + content)
        if (isFile and content[0] != "."):
            files.append(folder_path + "/" + content)
    return files

def create_new_name(file_name, file_extension):
    """
    Creates a new file name based on the original file name and file extension.
    
    Args:
        file_name (str): The original file name.
        file_extension (str): The file extension (including the dot).

    Returns:
        str: The new file name generated by removing digits, spaces, dashes, and underscores from the original file name,
             appending the file extension, and converting the new file name to lowercase.
    """
    new_file_name = "".join([i for i in file_name if not i.isdigit()])
    new_file_name = new_file_name.replace(" ", "")
    new_file_name = new_file_name.replace("-", "")
    new_file_name = new_file_name.replace("_", "") + file_extension
    new_file_name = new_file_name.lower()
    return new_file_name

def list_visible_folders(folder_path):
    """
    Lists and returns a list of visible folder paths within a given folder path.
    
    Args:
        folder_path (str): The path to the folder.

    Returns:
        list: A list of visible folder paths within the given folder path.
    """
    visible_folders = []
    subfolders = list_directories(folder_path)
    for subfolder_path in subfolders:
        subfolder_name = subfolder_path.split("/")[-1]
        if subfolder_name[0] != ".":
            visible_folders.append(subfolder_path)
    return visible_folders

def write_list_to_file(path, lst):
    """
    Writes a list of items to a file, with each item on a new line.
    
    Args:
        path (str): The path to the file.
        lst (list): The list of items to write to the file.

    Returns:
        None
    """
    with open(path, "w") as file:
        for item in lst:
            file.write(item + "\n")