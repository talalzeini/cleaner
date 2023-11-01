import os, json, glob
from helpers import get_root_username, replace_username

username = get_root_username()
cleaner_path = os.getcwd()
data_path = cleaner_path + "/data"
extensions_data = open(str(data_path) + "/extensions.json")
directories_data = open(str(data_path) + "/directories.json")
extensions = json.load(extensions_data)
directories = json.load(directories_data)

# essential
replace_username(directories)

cleaner = "Cleaner.app"
close_finder_windows_string = """
    tell application "Finder"
        close every window
    end tell"""
#
#
#
# Directories
root = directories["root"]
downloads = directories["downloads"]
desktop = directories["desktop"]
documents = directories["documents"]
developer = directories["developer"]
#
audio_path = directories["audio"]
videos_path = directories["videos"]
images_path = directories["images"]
files_path = directories["files"]
programming_path = directories["programming"]
installers_path = directories["installers"]
text_path = directories["text"]
screenshots_path = directories["screenshots"]
files_path = directories["files"]
recordings_path = directories["recordings"]
#
pdf_path = directories["pdf"]
doc_path = directories["doc"]
docx_path = directories["docx"]
#
archived = directories["archived"]
archived_files = directories["archived_files"]
archived_folders = directories["archived_folders"]
#
#
#
root_folders = directories["root_folders"]
desktop_folders = directories["desktop_folders"]
downloads_folders = [
    archived,
    audio_path,
    videos_path,
    images_path,
    files_path,
    programming_path,
    installers_path,
    text_path,
    screenshots_path,
    files_path,
    recordings_path,
]
documents_folders = directories["documents_folders"]
developer_folders = directories["developer_folders"]
icloud_drive_folders = directories["icloud_drive_folders"]
#
#
#
# Extensions
image_extensions = extensions["images"]
video_extensions = extensions["videos"]
audio_extensions = extensions["audios"]
file_extensions = extensions["files"]
programming_extensions = extensions["programming"]
installer_extensions = extensions["installers"]
text_extensions = extensions["text"]
#
#
#
downloads_extensions_unmerged = [
    image_extensions,
    video_extensions,
    audio_extensions,
    file_extensions,
    programming_extensions,
    installer_extensions,
    text_extensions,
]
downloads_extensions = [
    *image_extensions,
    *video_extensions,
    *audio_extensions,
    *file_extensions,
    *programming_extensions,
    *installer_extensions,
    *text_extensions,
]
downloads_paths = [
    images_path,
    videos_path,
    audio_path,
    files_path,
    programming_path,
    installers_path,
    text_path,
]
files_prefixes = directories["files_prefixes"]
screenshots_directory = directories["screenshots_directory"]
#
#
#
icloud_drive = directories["icloud_drive"]
macbook_applications = directories["macbook_applications"]
system_applications_file = macbook_applications + "/system.txt"
downloaded_applications_file = macbook_applications + "/downloaded.txt"
system_apps = list(glob.glob("/System/Applications/*"))
system_apps = list(
    map(
        lambda x: x.replace("/System/Applications/", "").replace(".app", ""),
        system_apps,
    )
)
system_apps.remove("Utilities")
downloaded_apps = list(glob.glob("/Applications/*"))
downloaded_apps = list(
    map(lambda x: x.replace("/Applications/", "").replace(".app", ""), downloaded_apps)
)
#
#
# 
extensions_folder = directories["extensions"]
visual_studio = directories["visual_studio"]
visual_studio_settings = directories["visual_studio_settings"]
essential_folders = [archived_files, archived_folders]
logs_file = directories["logs_file"]