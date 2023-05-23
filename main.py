import os
import shutil
import os.path
from constants import *
import compress as cs
from datetime import datetime
import getpass

now = datetime.now()
hour = now.strftime("%H")
dt_string = now.strftime("%H:%M:%S %d/%m/%Y")

destination_folder = documents + "/Personal/Downloads"

def backup_downloads():
    shutil.rmtree(destination_folder, ignore_errors=True) # Remove the destination folder if it already exists
    shutil.copytree(downloads, destination_folder) # Use shutil to copy the original folder to the destination folder

def get_root_username():
    return str(getpass.getuser())

def track_history(results):
    file = open("history.txt", "a")  
    if(int(hour) == 5):
        file.write("Automated - " + str(dt_string) + " - " + str(results) + " Failures\n")
    else:
        file.write("Manual - " + str(dt_string) + " - " + str(results) + " Failures\n")


test_results = []
all = {}
songs = []

# music = [cs.list_directories(apple_music)]
# artists = list(itertools.chain.from_iterable(music))

def create_directories(essential_folders):
    for folder in essential_folders:
        if not cs.is_existing(folder):
            os.makedirs(folder)




def clean_subdirectories_in(folder):
    folders = cs.list_directories(folder)
    for subfolder in folders:
        move_files_in(subfolder)
    return folders



def clean_directories(list):
    for item in range(len(list)):
        list[item] = list[item].split("/")[-1]
        all[list[item]] = []
    return list

# artists = clean_directories(artists)

# def handle_music(path, list):
#     if(path is not all_path):
#         with open(path, "w") as f:
#             for app in range(len(list)):
#                 title = str(app+1) + ". " + str(list[app]) + "\n"
#                 f.write(title)
#     else:
#         with open(all_path, "w") as f:
#             for artist in all:
#                 f.write(artist + "\n\t-  " + '\n\t-  '.join(all[artist]) + "\n\n\n")
        
# def prepare_songs():
#     for dirpath, _, filenames in os.walk(apple_music):
#         for i, filename in enumerate([f for f in filenames if f.endswith(".m4p")]):
#             song = str(filename.split(" ", 1)[-1])
#             artist = str(dirpath.split("/")[-2])
#             songs.append(song)
#             all[artist].append(song)

def update_compress():
    if(os.path.exists(compress)):
        shutil.rmtree(compress)
    if(os.path.exists(compress_dist_info)):
        shutil.rmtree(compress_dist_info)
    os.system("python3 -m pip install git+https://github.com/talalzeini/compress.git")

def notify(title):
    title = """ " """ + title + """ " """
    message = """'tell application "Finder" to display alert """"" + str(title) + """'"""
    os.system("""
              osascript -e """ + str(message))

def test_folder_existence(folder_path, number):
    try:
        if cs.is_existing(folder_path):
            print("Test " + str(number) + ": Passed\n")
            test_results.append(True)
        else:
            raise Exception("Test " + str(number) + ": Failed\n")
    except Exception as e:
        print(e)

def test_folder_emptiness(folder_path, number):
    try:
        list_of_files = find_files_in(folder_path)
        if len(list_of_files) == 0:
            print("Test " + str(number) + ": Passed\n")
            test_results.append(True)
        else:
            raise Exception("Test " + str(number) + ": Failed\n")
    except Exception as e:
        print(e)

def validate_setup(folder_path, original_folders, number):
    try:
        folders = list_all_real_folders(folder_path)
        for folder in folders:
            if folder not in original_folders:
                raise Exception("Test " + str(number) + ": Failed\n")
        print("Test " + str(number) + ": Passed\n")
        test_results.append(True)
    except Exception as e:
        print(e)

def check_capitalization(folder_path, number):
    try:
        folders = cs.list_directories(folder_path)
        for folder in folders:
            folder_name = folder.split("/")[-1]
            if folder_name[0].islower():
                raise Exception("Test " + str(number) + ": Failed\n")
        print("Test " + str(number) + ": Passed\n")
        test_results.append(True)
    except Exception as e:
        print("Test " + str(number) + ": Failed")
        print(str(e) + "\n")

def test_length_of(folder_path, number):
    try:
        folders = cs.list_directories(folder_path)
        size = len(folders)
        if size > limit_of_projects:
            raise Exception("Test " + str(number) + ": Failed\n")
        else:
            print("Test " + str(number) + ": Passed\n")
            test_results.append(True)
    except Exception as e:
        print(e)



def get_results(passed, number_of_tests):
    return number_of_tests - passed


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
    print("Test 14: Checking if there's any extra folders in the 'Developer' folder")
    test_length_of(developer, 14)
    results = get_results(len(test_results), 14)
    print("\n" +str(results) + " tests failed.\n\n")
    track_history(results)
    if results == 0:
        notify("Successfully cleaned Finder")
    elif results == 1:
        notify("1 failure found")
    else:
        notify(str(results) + "1 failure found")

def find_files_in(path):
    files = []
    directory = os.listdir(path)
    for content in directory:
        isFile = os.path.isfile(path + "/" + content)
        if((isFile) and (content not in virtual_files) and (content[0] != ".") and not (path == desktop and content == "New Document.webloc") and not (path == desktop and content == "Tasks.webloc") and not (path == desktop and content == "Tasks")):
            files.append(path + "/" + content)
    return files

def create_new(file_name, file_extension): 
    new_file_name = ''.join([i for i in file_name if not i.isdigit()])
    new_file_name = new_file_name.replace(" ", "") 
    new_file_name = new_file_name.replace("-", "")
    new_file_name = new_file_name.replace("_", "") + cs.random_string(5) + file_extension
    new_file_name = new_file_name.lower()
    return new_file_name.capitalize()

def find_type_of_file(file_extension):
    for index, extension_group in enumerate(downloads_extensions_unmerged):
        if file_extension in extension_group:
            return index


def handle_screen_actions(f, path, type):
    destination = path
    if not cs.is_existing(destination):
        os.makedirs(destination)
    new_file_name = cs.get_file_info(f)[0].split(type)[1]
    new_file_path = f.split(cs.get_file_info(f)[0])[0] + new_file_name
    os.rename(f, new_file_path)
    shutil.move(new_file_path, destination + "/" + new_file_name)

def move_files_in(source):
    files = find_files_in(source) # returns a list of paths to files

    for file_path in files:
        file = cs.get_file_info(file_path)
        file_full_name = file[0]                                # example.txt
        file_extension = file[1]                                # .txt

        if "Screenshot" in file_full_name:
            handle_screen_actions(file_path, screenshots_path, "Screenshot")
        elif "Screen Recording" in file_full_name:
            handle_screen_actions(file_path, recordings_path, "Screen Recording")
        else:
            if "." in file_full_name:
                file_name = file_full_name.split(file_extension)[0]  # example
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

def clean_projects():
    folders = list_all_real_folders(developer)
    if len(folders) > limit_of_projects:
        for folder in folders:
            folder_name = folder.split("/")[-1]
            if folder_name not in accepted_projects:
                new_folders = list_all_real_folders(developer)
                size = len(new_folders)
                duplicate = junk_projects + "/" + folder_name
                if (size > limit_of_projects) and (not cs.is_existing(duplicate)):
                    shutil.move(folder, junk_projects)

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


def write_in(path, list):
    with open(path, "w") as f:
        for app in list:
            f.truncate()
            f.write(app + "\n")

def move_folders():
    move_folders_in(root_folders_to_move)
    move_folders_in(desktop_folders_to_move)
    move_folders_in(documents_folders_to_move)
    move_folders_in(downloads_folders_to_move)

def move_files():
    move_files_in(root)
    move_files_in(desktop)
    move_files_in(developer)
    move_files_in(documents)
    move_files_in(downloads) 

def clean_subdirectories():
    clean_subdirectories_in(desktop)
    clean_subdirectories_in(documents)
    clean_subdirectories_in(downloads)


def update_apps():
    write_in(system_applications_file, system_apps)
    write_in(downloaded_applications_file, downloaded_apps)

# def update_songs():
#     prepare_songs()
#     handle_music(artists_path, artists)
#     handle_music(songs_path, songs)
#     handle_music(all_path, songs)

def start():
    backup_downloads()
    clean_subdirectories()
    create_directories(essential_folders)
    move_folders()
    move_files()
    clean_projects()
    update_apps()
    # update_songs()
    # update_compress()
    run_tests()
    

start()