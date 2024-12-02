import os

def list_files_and_folders(path):
    for i in os.listdir(path):
        i_path = os.path.join(path, i)
        
        if os.path.isdir(i_path):
            print("Folder name: " + i_path)
            list_files_and_folders(i_path)
        else:
            print("File path: " + i_path)

path = "/Users/jessi/Documents/Infnet/4E24/Velocidade"
list_files_and_folders(path)
