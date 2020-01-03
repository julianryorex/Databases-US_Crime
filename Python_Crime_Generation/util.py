'''
This is a utility file that does common things.
Keep adding methods as I go
'''
import os
import json

# gets the current path
def get_current_path():
    return os.getcwd()

# returns the root path of this project
def import_project_path():
    return "/Users/myfatduck/OneDrive/Programs/Databases/Databases-US_Crime"

# prints number of lines processed
def process(lines):
    print(f"Processed {lines} lines." )

# gets type of $item
def t(item):
    print(f"Type: {type(item)}")

# Finds all files from the root directory of the project
def find_all(name):
    result = []
    for root, dirs, files in os.walk(import_project_path()):
        if name in files:
            result.append(os.path.join(root, name))

    if len(result) == 1:
        return result[0]
    else:
        return result

# Pretty prints lists!
def print_all(iterable):
    if type(iterable) is dict:
        print_dict(iterable)
    elif type(iterable) is list:
        for index, item in enumerate(iterable):
            print(f"Index {index}:\t{item}")

# pretty prints dictionaries
def print_dict(dictionary):
    for key, value in dictionary:
        print(f"Key: {key}\tValue: {value}")

# function that creates SQL output
# assumes a nested dictionary if data is type list
def output_SQL(table_name, data, path_to_file):
    if type(data) == list:
        for index, item in enumerate(data, 1): # item is a dictionary
            for key in item:
                file = f"{import_project_path()}/{path_to_file}"
                with open(file, "a") as output_file:
                    line = f"INSERT INTO {table_name} VALUES({index}, '{key}', {item.get(key)});\n"
                    output_file.write(line)

def output_json(data, file_name, open_type = "w"):
    file = find_all(file_name)
    with open(file, open_type) as json_file:
        json.dump(data, json_file)
