import os
def find_files(directory):
    files_list = search_files_recursive(directory)
    return files_list

def search_files_recursive(directory):
    files_list = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            files_list.append(file_path)

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            files_list.extend(search_files_recursive(dir_path))

    return files_list
