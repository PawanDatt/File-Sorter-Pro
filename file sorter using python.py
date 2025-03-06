# file sorter using python

# important libraries use for file sorter
import os
import shutil 

# Prompt user to enter the directory path
path = input("Enter the directory path to sort files: ").strip()


# to store a list of file present in the path 
file_name =  os.listdir(path) 

# folder creation if not present for the storing of different file type
folder_name = [
    'Image files', 'Text files', 'Audio files', 
    'Video Files', 'Programs Files', 'Compressed/Archive files', 'WebPages Files'
]

# loop for searching if folder exist or not if not than create
for folder in folder_name:
   folder_path = os.path.join(path, folder)
   if not os.path.exists(folder_path):
        print(f"Creating folder: {folder_path}")
        os.makedirs(folder_path)

# rearranging all the file to thier dedicated folder if not 
for file in file_name:
    file_path = os.path.join(path, file)
    
    # Skip directories
    if not os.path.isfile(file_path):
        continue
    
    # Get file extension
    _, ext = os.path.splitext(file)
    ext = ext.lower()  # Standardize extension comparison

    # for text file
    if ext in [".txt", ".doc", ".docx", ".pdf", ".csv", ".xls", ".xlsx", ".ppt", ".pptx", ".rtf", ".odt", ".ods", ".odp", ".md"]:
        shutil.move(os.path.join(path, file), os.path.join(path, "Text files", file))
    
    # For Image Files
    elif ext in [".png", ".jpeg", ".jpg", ".gif", ".bmp", ".tiff", ".svg", ".ico", ".webp", ".psd", ".ai", ".eps", ".raw"] and not os.path.exists(path + "Image files/" + file):
        shutil.move(path + file, path + "Image files/" + file)
    
    # For Audio Files
    elif ext in [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma", ".amr", ".aiff", ".alac"]:
        shutil.move(os.path.join(path, file), os.path.join(path, "Audio files", file))
    
    # For Vedio Files
    elif ext in [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv", ".webm", ".vob", ".3gp", ".mpeg", ".m4v", ".ts"]:
        shutil.move(os.path.join(path, file), os.path.join(path, "Video Files", file))
    
    # For Program Files
    elif ext in [".py", ".java", ".cpp", ".c", ".js", ".html", ".css", ".php", ".sql", ".rb", ".swift", ".go", ".sh", ".bat", ".json", ".yaml", ".xml", ".ini", ".asm", ".pl", ".kt", ".ts", ".cs", ".vb"]:
        shutil.move(os.path.join(path, file), os.path.join(path, "Programs Files", file))
     
    # For Compresses/Archive Files
    elif ext in [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".dmg", ".tgz", ".cab"]:
        shutil.move(os.path.join(path, file), os.path.join(path, "Compressed/Archive files", file))
    
    # For Webpages Files
    elif ext in [".html", ".htm", ".xml", ".json", ".asp", ".aspx", ".jsp", ".php", ".xhtml", ".css", ".js", ".yaml"]:
        shutil.move(os.path.join(path, file), os.path.join(path, "WebPages Files", file))
    
    # if file that are not moved print
    else:
        print(f"There are files in this path that were not moved: {file}")