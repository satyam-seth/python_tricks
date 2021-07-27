import os
folder_path = input('Enter folder path:')
for file_name in os.listdir(folder_path):
    new_name=" ".join(file_name.split()[2:])
    os.rename(os.path.join(folder_path,file_name),os.path.join(folder_path,new_name))