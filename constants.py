import json

data_path = "/Users/talalzeini/Library/.Access/Cleaner/cleaner/data"
extensions_data = open(str(data_path) + '/extensions.json')
directories_data = open(str(data_path) + '/directories.json') 
extensions = json.load(extensions_data)
directories = json.load(directories_data)

automater_of_this = "Cleaner.app"
virtual_files = [".DS_Store", ".localized"]
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
music_path = directories["music"]
videos_path = directories["videos"]
images_path = directories["images"]
files_path = directories["files"]
programming_path = directories["programming"]
installers_path = directories["installers"]
text_path = directories["text"]
screenshots_path = directories["screenshots"]
files_path = directories["files"]
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
downloads_folders = [music_path, music_path, videos_path, images_path, files_path,programming_path, installers_path, text_path, screenshots_path, files_path]
documents_folders = directories["documents_folders"]


# Extensions
image_extensions = [i for i in extensions['images']]
video_extensions = [i for i in extensions['videos']]
audio_extensions = [i for i in extensions['audios']]
file_extensions = [i for i in extensions['files']]
programming_extensions = [i for i in extensions['programming']]
installer_extensions = [".dmg", ".pkg"]
text_extensions = [".txt", ".rtf"]

automater_of_this = "Cleaner.app"
downloads_extensions = [image_extensions, video_extensions, audio_extensions, file_extensions, programming_extensions, installer_extensions, text_extensions]
downloads_paths = [images_path, videos_path, music_path, files_path, programming_path, installers_path, text_path]
files_prefixes = directories["files_prefixes"]
virtual_files = directories["virtual_files"]