import json, glob

data_path = "/Users/talalzeini/Library/.Access/Cleaner/data"
extensions_data = open(str(data_path) + '/extensions.json')
directories_data = open(str(data_path) + '/directories.json') 
extensions = json.load(extensions_data)
directories = json.load(directories_data)

limit_of_projects = 15
automater_of_this = "Cleaner.app"
library_documents = "/Users/talalzeini/Library/Access/Documents"
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
junk = directories["junk"]
junk_files = directories["junk_files"]
junk_folders = directories["junk_folders"]
junk_projects = directories["junk_projects"]
trash = directories["trash"]
#
#
#
root_folders = directories["root_folders"]
desktop_folders = directories["desktop_folders"]
downloads_folders = [audio_path, videos_path, images_path, files_path,programming_path, installers_path, text_path, screenshots_path, files_path, recordings_path]
documents_folders = directories["documents_folders"]
#
#
#
# Extensions
image_extensions = extensions['images']
video_extensions = extensions['videos']
audio_extensions = extensions['audios']
file_extensions = extensions['files']
programming_extensions = extensions['programming']
installer_extensions = extensions["installers"]
text_extensions = extensions["text"]
#
#
#
automater_of_this = "Cleaner.app"
downloads_extensions_unmerged = [image_extensions, video_extensions, audio_extensions, file_extensions, programming_extensions, installer_extensions, text_extensions]
downloads_extensions = [*image_extensions, *video_extensions, *audio_extensions, *file_extensions, *programming_extensions, *installer_extensions, *text_extensions]
downloads_paths = [images_path, videos_path, audio_path, files_path, programming_path, installers_path, text_path]
files_prefixes = directories["files_prefixes"]
virtual_files = directories["virtual_files"]
accepted_projects = directories["projects"]
#
#
#
icloud_drive = directories["icloud_drive"]
macbook_applications = directories["macbook_applications"]
system_applications_file = macbook_applications + "/system.txt"
downloaded_applications_file  = macbook_applications + "/downloaded.txt"
system_apps = list(glob.glob("/System/Applications/*"))
system_apps = list(map(lambda x: x.replace('/System/Applications/', '').replace('.app', ''), system_apps))
system_apps.remove("Utilities")
downloaded_apps = list(glob.glob("/Applications/*"))
downloaded_apps = list(map(lambda x: x.replace('/Applications/','').replace('.app', ''), downloaded_apps))
#
#
#
apple_music = directories["apple_music"]
music_backup = icloud_drive + "/Tech/Backups/Music"
artists_path = music_backup + "/artists.txt"
songs_path = music_backup + "/songs.txt"
all_path = music_backup + "/all.txt"
#
#
#
compress = directories["compress"]
compress_dist_info = directories["compress_dist_info"]