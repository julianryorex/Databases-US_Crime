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
    print(f"Processed {lines} lines from file." )

def outputted(lines):
    print(f"Outputted {lines} lines to SQL." )

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
def output_SQL(table_name, data, path_to_file, enum = False):


    # array of arrays
    if type(data) == list and type(data[0]) == list:
        if enum:
            array_in_array(table_name, data, path_to_file, enumerate)
        else:
            array_in_array(table_name, data, path_to_file)

    elif type(data) == list:
        count = 0
        for index, item in enumerate(data, 1):
            file = f"{import_project_path()}/{path_to_file}"
            with open(file, "a") as output_file:
                line = f"INSERT INTO {table_name} VALUES({index}, '{item}');\n"
                output_file.write(line)
                count += 1
        outputted(count)

    # if the format is a dictionary in a list:
    elif len(data[0].keys()) > 1:
        output_multiple(table_name, data, path_to_file)




    # item is a dictionary
    elif type(data) == list:
        count = 0
        for index, item in enumerate(data, 1):
            for key in item:
                file = f"{import_project_path()}/{path_to_file}"
                with open(file, "a") as output_file:
                    line = f"INSERT INTO {table_name} VALUES({index}, '{key}', {item.get(key)});\n"
                    output_file.write(line)
                    count += 1
        outputted(count)


# for nested arrays (victim_offender)
def array_in_array(table_name, data, path_to_file, enum = False):
    count = 0
    if enum:
        for index, item in enumerate(data, 1):
            file = f"{import_project_path()}/{path_to_file}"
            with open(file, "a") as output_file:
                v = value_to_string(item)
                line = f"INSERT INTO {table_name} VALUES({index}, {v});\n"
                output_file.write(line)
                count += 1
    else:
        for item in data:
            file = f"{import_project_path()}/{path_to_file}"
            with open(file, "a") as output_file:
                v = value_to_string(item)
                line = f"INSERT INTO {table_name} VALUES({v});\n"
                output_file.write(line)
                count += 1
    outputted(count)

# temp function for multiple dictionary values (such as person)
# first get number of values in object
# then output item to SQL using new value array
def output_multiple(table_name, data, path_to_file):
    values = []
    for index, item in enumerate(data, 1): # item is a dictionary
        temp = []
        for key, value in item.items():
            temp.append(value)
        values.append(temp)
    print(values)

    count = 0 # number of lines outputted
    for item in values:
        file = f"{import_project_path()}/{path_to_file}"
        with open(file, "a") as output_file:
            v = value_to_string(item)
            line = f"INSERT INTO {table_name} VALUES({v});\n"
            print(line)
            #output_file.write(line)
            count += 1
    outputted(count)


def value_to_string(item):
    item = str(item)
    return item[1:-1]

def output_json(data, file_name, open_type = "w"):
    file = find_all(file_name)
    with open(file, open_type) as json_file:
        json.dump(data, json_file)
    print("JSON has been dumped.")
