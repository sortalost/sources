import os
import shutil

source_folder = f"{os.getcwd()}/"
destination_folder = "./flags/"
i=0
# fetch all files
for file_name in os.listdir(os.getcwd()):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # move only files
    if file_name.endswith("png"):
        shutil.move(source, destination)
        i+=1

print(i)
